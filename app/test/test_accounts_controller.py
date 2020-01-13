# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.account import Account  # noqa: E501
from app.models.request_account import RequestAccount  # noqa: E501
from app.test import BaseTestCase, token

headers = {"Authorization": "Bearer {0}".format(token)}

account = {
    "date_start": 0,
    "friendly_name": "Debit account",
    "account_type": "checking"
}


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    def test_create_account(self):
        """Test case for create_account

        Creates an account
        """
        body = RequestAccount.from_dict(account)
        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(customer_id=789),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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
        response = self.client.open(
            '/accounts/{account_id}'.format(account_id=789),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_accounts(self):
        """Test case for list_accounts

        List all customer accounts
        """
        response = self.client.open(
            '/customer/{customer_id}/accounts'.format(customer_id=789),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
