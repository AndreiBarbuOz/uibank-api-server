import connexion
import six

from app.models.auth import Auth  # noqa: E501
from app import util


def auth(body=None):  # noqa: E501
    """Authenticate endpoint

    Return a bearer token to authenticate and authorize subsequent calls for resources # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Auth
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
