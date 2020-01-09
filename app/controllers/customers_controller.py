import connexion
import six

from app.models.customer import Customer  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app import util


def add_customer(body):  # noqa: E501
    """Add a new customer

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Customer
    """
    if connexion.request.is_json:
        body = RequestCustomer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_customer(customer_id):  # noqa: E501
    """Delete a single customer

    Delete customer, based on customerId # noqa: E501

    :param customer_id: Customer to be deleted
    :type customer_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_customer_details(customer_id):  # noqa: E501
    """Get customer details

    Retrieve the details of a customer # noqa: E501

    :param customer_id: The customerId
    :type customer_id: int

    :rtype: Customer
    """
    return 'do some magic!'


def search_customer(first_name=None, last_name=None):  # noqa: E501
    """Search for Customers

    Search for customers using multiple search criteria # noqa: E501

    :param first_name: First name to filter by
    :type first_name: str
    :param last_name: Last name to filter by
    :type last_name: str

    :rtype: List[Customer]
    """
    return 'do some magic!'


def update_customer(body, customer_id):  # noqa: E501
    """Update an existing customer

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes
    :param customer_id: The customerId
    :type customer_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = RequestCustomer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
