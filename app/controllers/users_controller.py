import connexion
import six

from app.models.request_user import RequestUser  # noqa: E501
from app.models.user import User  # noqa: E501
from app import util


def add_user(body):  # noqa: E501
    """Add a new admin user

     # noqa: E501

    :param body: User data to create
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = RequestUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """Returns user information

    Returns information about one user # noqa: E501

    :param user_id: Id of user
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'
