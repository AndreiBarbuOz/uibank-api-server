import connexion
import six

from app.models.auth import Auth  # noqa: E501
from app.models.request_auth import RequestAuth  # noqa: E501
from app import util


def auth(body):  # noqa: E501
    """Authenticate endpoint

    Return a bearer token to authenticate and authorize subsequent calls for resources # noqa: E501

    :param body: Request body to perform authentication
    :type body: dict | bytes

    :rtype: Auth
    """
    if connexion.request.is_json:
        body = RequestAuth.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
