# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.bank_card import BankCard  # noqa: E501
from app.test import BaseTestCase


class TestCardsController(BaseTestCase):
    """CardsController integration test stubs"""

    def test_add_bank_card(self):
        """Test case for add_bank_card

        Add a new bank card for an account
        """
        body = BankCard()
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/accounts/{accountId}/cards'.format(account_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_card(self):
        """Test case for get_card

        Return all bank cards for an account
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/cards/{cardId}'.format(card_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_bank_cards(self):
        """Test case for list_bank_cards

        Return all bank cards for an account
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/accounts/{accountId}/cards'.format(account_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
