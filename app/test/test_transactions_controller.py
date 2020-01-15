# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.request_transaction import RequestTransaction  # noqa: E501
from app.models.transaction import Transaction  # noqa: E501
from app.models.request_customer import RequestCustomer  # noqa: E501
from app.models.request_account import RequestAccount  # noqa: E501
from app.test import BaseTestCase, token

test_cust = {
    "first_name": "John",
    "last_name": "Doe",
    "middle_name": "string",
    "title": "mr",
    "gender": "male",
    "email": "john.doe@uibank.com",
    "date_of_birth": "2020-01-13",
    "employment_status": "permanent",
    "residence_status": "resident",
    "addresses": [
        {
            "date_start": "2020-01-13",
            "date_end": "2020-01-13",
            "address1": "No 120 Spencer Street",
            "address2": "Level 20",
            "town": "Melbourne",
            "state": "Victoria",
            "postcode": "3000"
        }
    ],
    "plain_password": "string"
}

test_account = {
    "date_start": "2020-01-13",
    "friendly_name": "Debit account",
    "account_type": "checking"
}

test_transact = {
    "amount": 0,
    "transaction_type": "debit",
    "description": "return loan",
    "account": "1001001234"
}

headers = {"Authorization" : "Bearer {0}".format(token)}

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
            '/accounts/{account_id}/transactions'.format(account_id=response.json['id']),
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
        response = self.client.open(
            '/transactions/{transaction_id}'.format(
                transaction_id='transaction_id_example'),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_transactions(self):
        """Test case for list_transactions

        Return all transactions for an account
        """
        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(account_id=789),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
