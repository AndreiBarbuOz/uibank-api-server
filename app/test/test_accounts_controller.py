# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.account import Account  # noqa: E501
from app.models.request_account import RequestAccount  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app.test import BaseTestCase, token
from faker import Faker
import random
import string

fake = Faker()


headers = {"Authorization": "Bearer {0}".format(token)}

test_account = {
    "date_start": fake.date_this_decade(before_today=True, after_today=False).strftime('%Y-%m-%d'),
    "friendly_name": fake.sentence(nb_words=5, variable_nb_words=True),
    "account_type": random.choice(["checking", "savings"])
}

test_cust = {
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


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    def compare_response(self, account_request, account):
        for k, v in account_request.items():
            if not k in ['addresses', 'plain_password']:
                self.assertIn(k, account)
                self.assertEqual(v, account[k])

    def setUp(self):
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

    def test_create_account(self):
        """Test case for create_account

        Creates an account
        """
        body = RequestAccount.from_dict(test_account)
        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=self.customer_id),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_account, response.json)

    def test_delete_account(self):
        """Test case for delete_account

        Deletes an account
        """
        response = self.client.open(
            '/accounts/{account_id}'.format(account_id=789),
            headers=headers,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account(self):
        """Test case for get_account

        Get details for an account
        """
        body = RequestAccount.from_dict(test_account)
        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=self.customer_id),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')

        response = self.client.open(
            '/accounts/{account_id}'.format(account_id=response.json['id']),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_account, response.json)

    def test_list_accounts(self):
        """Test case for list_accounts

        List all customer accounts
        """
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        cust_id = response.json['id']

        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=cust_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(response.json, [])

        body = RequestAccount.from_dict(test_account)
        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=cust_id),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=cust_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(len(response.json), 1)
        self.compare_response(test_account, response.json[0])

        body = RequestAccount.from_dict(test_account)
        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=cust_id),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(
                customer_id=cust_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(len(response.json), 2)
        self.compare_response(test_account, response.json[0])
        self.compare_response(test_account, response.json[1])


if __name__ == '__main__':
    import unittest
    unittest.main()
