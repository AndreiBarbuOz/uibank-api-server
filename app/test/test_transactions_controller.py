# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.transaction import Transaction  # noqa: E501
from app.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_add_transaction(self):
        """Test case for add_transaction

        Returns one transaction data
        """
        body = None
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/accounts/{accountId}/transactions'.format(account_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transaction(self):
        """Test case for get_transaction

        Returns one transaction data
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/transactions/{transactionId}'.format(transaction_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_transactions(self):
        """Test case for list_transactions

        Return all transactions for an account
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/accounts/{accountId}/transactions'.format(account_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
