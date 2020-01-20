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
from app.test.test_customers_controller import generate_customer
from app.test.test_accounts_controller import generate_account

fake = Faker()


def generate_transaction():
    return {
        "amount": random.uniform(10, 1000),
        "transaction_type": random.choice(["debit", "credit"]),
        "description": fake.sentence(nb_words=5, variable_nb_words=True),
        "account": ''.join([random.choice(string.digits) for n in range(10)])
    }


test_cust = generate_customer()
test_account = generate_account()
test_transact = generate_transaction()

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
            '/accounts/{account_id}/transactions'.format(
                account_id=account_id),
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
            '/accounts/{account_id}/transactions'.format(
                account_id=account_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(len(response.json), 1)
        self.compare_response(test_transact, response.json[0])


if __name__ == '__main__':
    import unittest
    unittest.main()
