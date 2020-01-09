# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.customer import Customer  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app.test import BaseTestCase


class TestCustomersController(BaseTestCase):
    """CustomersController integration test stubs"""

    def test_add_customer(self):
        """Test case for add_customer

        Add a new customer
        """
        body = RequestCustomer()
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/customers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_customer(self):
        """Test case for delete_customer

        Delete a single customer
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/customers/{customerId}'.format(customer_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_details(self):
        """Test case for get_customer_details

        Get customer details
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/customers/{customerId}'.format(customer_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_customer(self):
        """Test case for search_customer

        Search for Customers
        """
        query_string = [('first_name', 'first_name_example'),
                        ('last_name', 'last_name_example')]
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/customers/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer(self):
        """Test case for update_customer

        Update an existing customer
        """
        body = RequestCustomer()
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/customers/{customerId}'.format(customer_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
