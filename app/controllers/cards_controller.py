import connexion
import six

from app.models.bank_card import BankCard  # noqa: E501
from app import util


def add_bank_card(body, account_id):  # noqa: E501
    """Return all bank cards for an account

    Return all cards for the specified account # noqa: E501

    :param body: Bank card details
    :type body: dict | bytes
    :param account_id: Id of account
    :type account_id: int

    :rtype: BankCard
    """
    if connexion.request.is_json:
        body = BankCard.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_card(card_id):  # noqa: E501
    """Return all bank cards for an account

    Return all cards for the specified account # noqa: E501

    :param card_id: Id of the card
    :type card_id: int

    :rtype: BankCard
    """
    return 'do some magic!'


def list_bank_cards(account_id):  # noqa: E501
    """Return all bank cards for an account

    Return all cards for the specified account # noqa: E501

    :param account_id: Id of account
    :type account_id: int

    :rtype: List[BankCard]
    """
    return 'do some magic!'
