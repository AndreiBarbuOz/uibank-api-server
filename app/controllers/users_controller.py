import connexion
import six

from app.models.user import User  # noqa: E501
from app import util


def add_user(body=None):  # noqa: E501
    """Add a new admin user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """Returns user information

    Returns information about one user # noqa: E501

    :param user_id: Id of user
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'
