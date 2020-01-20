# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.request_transaction import RequestTransaction  # noqa: E501
from app.models.transaction import Transaction  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app.models.request_account import RequestAccount  # noqa: E501
from app.test import BaseTestCase, token
from faker import Faker
import random
import string

fake = Faker()


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

test_account = {
    "date_start": fake.date_this_decade(before_today=True, after_today=False).strftime('%Y-%m-%d'),
    "friendly_name": fake.sentence(nb_words=5, variable_nb_words=True),
    "account_type": random.choice(["checking", "savings"])
}

test_transact = {
    "amount": random.uniform(10, 1000),
    "transaction_type": random.choice(["debit", "credit"]),
    "description": fake.sentence(nb_words=5, variable_nb_words=True),
    "account": ''.join([random.choice(string.digits) for n in range(10)])
}

headers = {"Authorization": "Bearer {0}".format(token)}


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def compare_response(self, transact_request, transact):
        for k, v in transact_request.items():
            self.assertIn(k, transact)
            self.assertEqual(v, transact[k])

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

    def test_add_transaction(self):
        """Test case for add_transaction

        Returns one transaction data
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

        body = RequestTransaction.from_dict(test_transact)
        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(
                account_id=response.json['id']),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_transact, response.json)

    def test_get_transaction(self):
        """Test case for get_transaction

        Returns one transaction data
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
        account_id = response.json['id']

        body = RequestTransaction.from_dict(test_transact)
        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(
                account_id=account_id),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        response = self.client.open(
            '/transactions/{transaction_id}'.format(
                transaction_id=response.json['id']),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_transact, response.json)

    def test_list_transactions(self):
        """Test case for list_transactions

        Return all transactions for an account
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
        account_id = response.json['id']

        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(account_id=account_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(response.json, [])

        body = RequestTransaction.from_dict(test_transact)
        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(
                account_id=account_id),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(account_id=account_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(len(response.json), 1)
        self.compare_response(test_transact, response.json[0])



if __name__ == '__main__':
    import unittest
    unittest.main()
