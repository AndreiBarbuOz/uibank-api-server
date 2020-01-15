import connexion
import six
from bson.objectid import ObjectId
from datetime import date, datetime
import random
import string

from app.models.account import Account  # noqa: E501
from app.models.request_account import RequestAccount  # noqa: E501
from app import util
from app import db

def decorate_account(account, customer_id): 
    account['date_start'] = str(account['date_start'].date())
    ret = Account.from_dict(account).to_dict()
    ret['self_url'] = '/accounts/{}'.format(account['id'])
    ret['cards_url'] = '/accounts/{}/cards'.format(account['id'])
    ret['customer_url'] = '/accounts/{}'.format(customer_id)
    return ret

def create_account(body, customer_id):  # noqa: E501
    """Creates an account

     # noqa: E501

    :param body: List of user object
    :type body: dict | bytes
    :param customer_id: Owner of the accounts
    :type customer_id: int

    :rtype: Account
    """
    try:
        _id = ObjectId(customer_id)
    except Exception:
        return 'Not found', 404
    cust = db['Customer'].find_one({"_id": _id})
    if cust is None:
        return 'Not found', 404

    req = RequestAccount.from_dict(body).to_dict()  # noqa: E501
    req['date_start'] = datetime.combine(req['date_start'], datetime.min.time())
    req['id'] = ObjectId()
    req['account_number'] = ''.join([random.choice(string.digits) for n in range(10)])
    req['balance'] = float(0)

    db["Customer"].update_one({"_id": _id, "first_name": cust['first_name']}, {"$push": {"accounts": req}})
    return decorate_account(req, customer_id)


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

    Returns a single account, based on account_id # noqa: E501

    :param account_id: Id of account
    :type account_id: str

    :rtype: Account
    """
    try:
        _id = ObjectId(account_id)
    except Exception:
        return 'Not found', 404

    cust = db['Customer'].find_one({"accounts.id" : _id} )
    try:
        account = next(filter(lambda x: x["id"] == _id, cust['accounts']))
        return decorate_account(account, str(cust['_id']))
    except Exception:
        return "not found", 404


def list_accounts(customer_id):  # noqa: E501
    """List all customer accounts

    Return a list of all accounts belonging to a customer # noqa: E501

    :param customer_id: Owner of the accounts
    :type customer_id: str

    :rtype: List[Account]
    """
    return 'do some magic!'
