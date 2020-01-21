import connexion
import six

from app.models.auth import Auth  # noqa: E501
from app.models.request_auth import RequestAuth  # noqa: E501
from app import util, get_db
import jwt
import time
from connexion.apps.flask_app import flask
import os

JWT_ISSUER = 'uibank.azurewebsites.com'
JWT_LIFETIME_SECONDS = 3600
JWT_ALGORITHM = 'HS256'


def generate_token(user_id, exp=None):
    timestamp = int(time.time())
    if exp is None:
        exp = int(timestamp + JWT_LIFETIME_SECONDS)
    payload = {
        "iss": JWT_ISSUER,
        "exp": exp,
        "sub": str(user_id),
    }
    ret = jwt.encode(payload, flask.current_app.config['JWT_SECRET'], algorithm=JWT_ALGORITHM)
    return ret

def generate_response(token):
    ret = {}
    ret['access_token'] = token.decode('utf-8')
    ret['token_type'] = 'bearer'
    return ret

def auth(body):  # noqa: E501
    """Authenticate endpoint

    Return a bearer token to authenticate and authorize subsequent calls for resources # noqa: E501

    :param body: Request body to perform authentication
    :type body: dict | bytes

    :rtype: Auth
    """
    db = get_db()
    cust = db['Customer'].find_one({"email": body['username']})

    try:
        if cust is None:
            user = db['User'].find_one({"email": body['username']})
            if user is None:
                return "Auth failed", 401
            else:
                if user['plain_password'] == body['password']:
                    return generate_response(generate_token(str(user['_id'])))
        else:
            if cust['plain_password'] == body['password']:
                return generate_response(generate_token(str(cust['_id'])))
    except Exception as e:
        print (e)

    return "Auth failed", 401
