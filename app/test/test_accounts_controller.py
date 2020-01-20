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

from app.test.test_customers_controller import generate_customer

fake = Faker()


def generate_account():
    return {
        "date_start": fake.date_this_decade(before_today=True, after_today=False).strftime('%Y-%m-%d'),
        "friendly_name": fake.sentence(nb_words=5, variable_nb_words=True),
        "account_type": random.choice(["checking", "savings"])
    }



headers = {"Authorization": "Bearer {0}".format(token)}


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    def compare_response(self, account_request, account):
        for k, v in account_request.items():
            if not k in ['addresses', 'plain_password']:
                self.assertIn(k, account)
                self.assertEqual(v, account[k])

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

    def test_create_account(self):
        """Test case for create_account

        Creates an account
        """
        test_account = generate_account()
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
        test_account = generate_account()
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

        response = self.client.open(
            '/accounts/{account_id}'.format(account_id=response.json['id']),
            headers=headers,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account(self):
        """Test case for get_account

        Get details for an account
        """
        test_account = generate_account()
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
            '/customer/{customer_id}/accounts'.format(
                customer_id=cust_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(response.json, [])

        test_account = generate_account()
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

        test_account2 = generate_account()
        body = RequestAccount.from_dict(test_account2)
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
        try:
            self.compare_response(test_account, response.json[0])
        except Exception:
            self.compare_response(test_account, response.json[1])
            self.compare_response(test_account2, response.json[0])
        else:
            self.compare_response(test_account2, response.json[1])


if __name__ == '__main__':
    import unittest
    unittest.main()
