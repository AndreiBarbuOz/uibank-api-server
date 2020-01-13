# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.request_transaction import RequestTransaction  # noqa: E501
from app.models.transaction import Transaction  # noqa: E501
from app.test import BaseTestCase, token

transact = {
    "amount": 0,
    "transaction_type": "debit",
    "description": "return loan",
    "account": "1001001234"
}

headers = {"Authorization" : "Bearer {0}".format(token)}

class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_add_transaction(self):
        """Test case for add_transaction

        Returns one transaction data
        """
        body = RequestTransaction.from_dict(transact)
        response = self.client.open(
            '/accounts/{account_id}/transactions'.format(account_id=789),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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
