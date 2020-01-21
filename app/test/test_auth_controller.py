# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.auth import Auth  # noqa: E501
from app.models.request_auth import RequestAuth  # noqa: E501
from app.test import BaseTestCase
from app.controllers.authorization_controller import check_bearerAuth
from app.test import token, err_token
from app.test.test_customers_controller import generate_customer
from app.models.request_customer import RequestCustomer  # noqa: E501

user_id = '1234567890'
exp = 1580102280

payload = {
    "username": "admin123",
    "password": "fie8T3m0!fvA"
}

headers = {"Authorization": "Bearer {0}".format(token)}


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth(self):
        """Test case for auth

        Authenticate endpoint
        """
        test_cust = generate_customer()
        body = RequestCustomer.from_dict(test_cust)
        response = self.client.open(
            '/customers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.customer_id = response.json['id']

        body = RequestAuth.from_dict(
            {"username": test_cust['email'], "password": test_cust['plain_password']})
        response = self.client.open(
            '/auth',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

#    def test_encode(self):
#        t = auth.generate_token(user_id, exp=exp)
#        self.assertEqual(token,t.decode('utf-8'))

    def test_decode(self):
        t = check_bearerAuth(token)
        self.assertIn('iss', t)
        self.assertEqual(t['iss'], 'uibank.azurewebsites.com')
        self.assertIn('exp', t)
        self.assertEqual(t['exp'], exp)
        self.assertIn('sub', t)
        self.assertEqual(t['sub'], user_id)
        pass

    def test_decode_raise(self):
        with self.assertRaises(Exception):
            check_bearerAuth(err_token)


if __name__ == '__main__':
    import unittest
    unittest.main()
