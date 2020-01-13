import connexion
import six

from app.models.request_transaction import RequestTransaction  # noqa: E501
from app.models.transaction import Transaction  # noqa: E501
from app import util


def add_transaction(account_id, body=None):  # noqa: E501
    """Returns one transaction data

    Returns one transaction data # noqa: E501

    :param account_id: Id of account
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = RequestTransaction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_transaction(transaction_id):  # noqa: E501
    """Returns one transaction data

    Returns one transaction data # noqa: E501

    :param transaction_id: Id of transaction
    :type transaction_id: str

    :rtype: Transaction
    """
    return 'do some magic!'


def list_transactions(account_id):  # noqa: E501
    """Return all transactions for an account

    List all transactions belonging to an account # noqa: E501

    :param account_id: Id of account
    :type account_id: str

    :rtype: List[Transaction]
    """
    return 'do some magic!'
