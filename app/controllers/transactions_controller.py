import connexion
import six
from bson.objectid import ObjectId
from datetime import date, datetime
import random
import string


from app.models.request_transaction import RequestTransaction  # noqa: E501
from app.models.transaction import Transaction  # noqa: E501
from app import util
from app import db


def decorate_transaction(transaction, account_id):
    transaction['date_time'] = str(transaction['date_time'])
    ret = Transaction.from_dict(transaction).to_dict()
    ret['self_url'] = '/transactions/{}'.format(transaction['id'])
    ret['account_url'] = '/accounts/{}'.format(account_id)
    return ret


def add_transaction(account_id, body):  # noqa: E501
    """Returns one transaction data

    Returns one transaction data # noqa: E501

    :param account_id: Id of account
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        _id = ObjectId(account_id)
    except Exception:
        return 'Not found', 404
    cust = db['Customer'].find_one({"accounts.id": _id})
    try:
        next(filter(lambda x: x["id"] == _id, cust['accounts']))
    except Exception:
        return "Not found", 404

    req = RequestTransaction.from_dict(body).to_dict()  # noqa: E501
    req['id'] = ObjectId()
    req['date_time'] = datetime.now()
    req['reference'] = 'TRN' + \
        ''.join([random.choice(string.digits) for n in range(8)])
    req['balance'] = float(0)
    req['dispute'] = 'in progress'

    db["Customer"].update({"_id": cust['_id'], "first_name": cust['first_name'], "accounts.id": _id} , {
                              "$push": {"accounts.$.transactions": req}})
    return decorate_transaction(req, account_id)


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
