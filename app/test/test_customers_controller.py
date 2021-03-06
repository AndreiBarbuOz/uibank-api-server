# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.customer import Customer  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app.test import BaseTestCase, token
from faker import Faker
import random
import string

fake = Faker()


def generate_customer():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "middle_name": "string",
        "title": "mr",
        "gender": "male",
        "email": fake.email(),
        "date_of_birth": fake.date_of_birth(minimum_age=20, maximum_age=50).strftime('%Y-%m-%d'),
        "employment_status": "permanent",
        "residence_status": "resident",
        "addresses": [
            {
                "date_start": fake.date(pattern='%Y-%m-%d', end_datetime='-5y'),
                "date_end": fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
                "address1": "No 120 Spencer Street",
                "address2": "Level 20",
                "town": "Melbourne",
                "state": "Victoria",
                "postcode": "3000"
            }
        ],
        "plain_password": ''.join([random.choice(string.digits + string.ascii_letters) for i in range(10)])
    }



headers = {"Authorization": "Bearer {0}".format(token)}


class TestCustomersController(BaseTestCase):
    """CustomersController integration test stubs"""

    def compare_response(self, customer_request, customer):
        for k, v in customer_request.items():
            if not k in ['addresses', 'plain_password']:
                self.assertIn(k, customer)
                self.assertEqual(v, customer[k])

    def setUp(self):
        test_cust = generate_customer()
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.customer_id = response.json['id']

    def tearDown(self):
        self.client.open(
            '/customers/{customer_id}'.format(customer_id=self.customer_id),
            headers=headers,
            method='DELETE')

    def test_add_customer(self):
        """Test case for add_customer

        Add a new customer
        """
        test_cust = generate_customer()
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_cust, response.json)

    def test_delete_customer(self):
        """Test case for delete_customer

        Delete a single customer
        """
        test_cust = generate_customer()
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        cust_id = response.json['id']
        response = self.client.open(
            '/customers/{customer_id}'.format(customer_id=cust_id),
            headers=headers,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        response = self.client.open(
            '/customers/{customer_id}'.format(customer_id=cust_id),
            headers=headers,
            method='GET')
        self.assert404(response, 'Response body is : ' +
                       response.data.decode('utf-8'))

    def test_get_customer_details(self):
        """Test case for get_customer_details

        Get customer details
        """
        test_cust = generate_customer()
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        cust_id = response.json['id']

        response = self.client.open(
            '/customers/{customer_id}'.format(customer_id=cust_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_cust, response.json)

    def test_search_customer(self):
        """Test case for search_customer

        Search for Customers
        """
        query_string = [('first_name', 'John'),
                        ('last_name', 'Doe')]
        response = self.client.open(
            '/customers/search',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer(self):
        """Test case for update_customer

        Update an existing customer
        """
        test_cust = generate_customer()
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers/{customer_id}'.format(customer_id=789),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
