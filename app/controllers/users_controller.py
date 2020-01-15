import connexion
import six
from bson.objectid import ObjectId

from app.models.request_user import RequestUser  # noqa: E501
from app.models.user import User  # noqa: E501
from app import util
from app import db

def add_user(body):  # noqa: E501
    """Add a new admin user

     # noqa: E501

    :param body: User data to create
    :type body: dict | bytes

    :rtype: User
    """
    req = RequestUser.from_dict(body).to_dict()  # noqa: E501
    req["email_canonical"] = req["email"].lower()
    req["username_canonical"] = req["username"].lower()
    user_id = db['User'].insert_one(req).inserted_id
    req["id"] = str(user_id)
    del req["_id"]
    return req


def get_user(user_id):  # noqa: E501
    """Returns user information

    Returns information about one user # noqa: E501

    :param user_id: Id of user
    :type user_id: str

    :rtype: User
    """
    try:
        _id = ObjectId(user_id)
    except Exception:
        return 'Not found', 404
    user = db['User'].find_one({"_id": _id})
    if user is None:
        return 'Not found', 404
    ret = User.from_dict(user).to_dict()
    ret["id"] = str(user["_id"])
    ret["self_url"] = "/users/{}".format(ret['id'])
    return ret
