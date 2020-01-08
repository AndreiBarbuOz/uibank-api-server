# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.user import User  # noqa: E501
from app.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        Add a new admin user
        """
        body = None
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Returns user information
        """
        response = self.client.open(
            '/AndreiBarbuOz/ui-bank/1.0.0/users/{userId}'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
