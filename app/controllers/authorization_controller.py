from typing import List
import jwt
import time
import os
from connexion.apps import flask_app

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_bearerAuth(token):
    try:
        ret = jwt.decode(token, flask_app.flask.current_app.config['JWT_SECRET'], algorithms=['HS256'])
    except Exception as e:
        print(e)
        raise e
    return ret


