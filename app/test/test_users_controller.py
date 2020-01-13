# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.request_user import RequestUser  # noqa: E501
from app.models.user import User  # noqa: E501
from app.test import BaseTestCase, token


test_user = {
    "username": "admin123",
    "plain_password": "fie8T3m0!fvA",
    "email": "admin@uibank.com",
    "first_name": "John",
    "last_name": "Admin"
    }

headers = {"Authorization" : "Bearer {0}".format(token)}

class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        Add a new admin user
        """
        body = RequestUser.from_dict(test_user)
        print(headers)
        print(json.dumps(body))
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Returns user information
        """
        user_id = "123456"
        response = self.client.open(
            '/users/{user_id}'.format(user_id=user_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
