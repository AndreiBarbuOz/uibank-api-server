# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.auth import Auth  # noqa: E501
from app.models.request_auth import RequestAuth  # noqa: E501
from app.test import BaseTestCase

payload = {
    "username": "admin123",
    "password": "fie8T3m0!fvA"
}


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth(self):
        """Test case for auth

        Authenticate endpoint
        """
        body = RequestAuth.from_dict(payload)
        response = self.client.open(
            '/auth',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
