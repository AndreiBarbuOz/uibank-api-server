import connexion
import six

from app.models.account import Account  # noqa: E501
from app import util


def create_account(body, customer_id):  # noqa: E501
    """Creates an account

     # noqa: E501

    :param body: List of user object
    :type body: dict | bytes
    :param customer_id: Owner of the accounts
    :type customer_id: int

    :rtype: Account
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_account(account_id):  # noqa: E501
    """Deletes an account

     # noqa: E501

    :param account_id: Id of account to delete
    :type account_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_account(account_id):  # noqa: E501
    """Get details for an account

    Returns a single account, based on accountId # noqa: E501

    :param account_id: Id of account
    :type account_id: int

    :rtype: Account
    """
    return 'do some magic!'


def list_accounts(customer_id):  # noqa: E501
    """List all customer accounts

    Return a list of all accounts belonging to a customer # noqa: E501

    :param customer_id: Owner of the accounts
    :type customer_id: int

    :rtype: List[Account]
    """
    return 'do some magic!'
