import connexion
import six
from bson.objectid import ObjectId

from app.models.customer import Customer  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app import util
from app import db
from datetime import date, datetime


def decorate_customer(customer): 
    customer['date_of_birth'] = str(customer['date_of_birth'].date())

    if 'addresses' in customer:
        for crt_address in customer['addresses']:
            crt_address['date_end'] = str(crt_address['date_end'].date())
            crt_address['date_start'] = str(crt_address['date_start'].date())

    ret = Customer.from_dict(customer).to_dict()
    ret["id"] = str(customer["_id"])
    ret["self_url"] = "/customers/{}".format(ret['id'])
    ret['accounts_url'] = "/customers/{}/accounts".format(ret['id'])

    return ret


def add_customer(body):  # noqa: E501
    """Add a new customer

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Customer
    """
    req = RequestCustomer.from_dict(body).to_dict()  # noqa: E501
    req["email_verified"] = False
    req['date_of_birth'] = datetime.combine(req['date_of_birth'], datetime.min.time())
    if 'addresses' in req:
        for crt_address in req['addresses']:
            crt_address['date_end'] = datetime.combine(crt_address['date_end'], datetime.min.time())
            crt_address['date_start'] = datetime.combine(crt_address['date_start'], datetime.min.time())

    db['Customer'].insert_one(req).inserted_id
    return decorate_customer(req)


def delete_customer(customer_id):  # noqa: E501
    """Delete a single customer

    Delete customer, based on customer_id # noqa: E501

    :param customer_id: Customer to be deleted
    :type customer_id: str

    :rtype: None
    """
    try:
        _id = ObjectId(customer_id)
    except Exception:
        return 'Not found', 404
    cust = db['Customer'].find_one({"_id": _id})
    if cust is None:
        return 'Not found', 404
    result = db['Customer'].delete_one({"_id": _id, "first_name": cust['first_name']})
    if result.deleted_count:
        return None, 200
    else:
        return "Not found", 404


def get_customer_details(customer_id):  # noqa: E501
    """Get customer details

    Retrieve the details of a customer # noqa: E501

    :param customer_id: The customer_id
    :type customer_id: str

    :rtype: Customer
    """
    try:
        _id = ObjectId(customer_id)
    except Exception:
        return 'Not found', 404
    cust = db['Customer'].find_one({"_id": _id})
    if cust is None:
        return 'Not found', 404

    return decorate_customer(cust)


def search_customer(first_name=None, last_name=None):  # noqa: E501
    """Search for Customers

    Search for customers using multiple search criteria # noqa: E501

    :param first_name: First name to filter by
    :type first_name: str
    :param last_name: Last name to filter by
    :type last_name: str

    :rtype: List[Customer]
    """
    cust_list = db['Customer'].find({"first_name": first_name, "last_name": last_name})
    if cust_list is None:
        return 'Not found', 404
    ret = []
    for cust in cust_list:
        cust['date_of_birth'] = str(cust['date_of_birth'].date())
        if 'addresses' in cust:
            for crt_address in cust['addresses']:
                crt_address['date_end'] = str(crt_address['date_end'].date())
                crt_address['date_start'] = str(crt_address['date_start'].date())
        crt_cust = Customer.from_dict(cust).to_dict()
        crt_cust["id"] = str(cust["_id"])
        crt_cust["self_url"] = "/customers/{}".format(crt_cust['id'])
        crt_cust['accounts_url'] = "/customers/{}/accounts".format(crt_cust['id'])
        ret.append(crt_cust)
    return ret


def update_customer(body, customer_id):  # noqa: E501
    """Update an existing customer

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes
    :param customer_id: The customer_id
    :type customer_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = RequestCustomer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
