# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.request_user import RequestUser  # noqa: E501
from app.models.user import User  # noqa: E501
from app.test import BaseTestCase, token

from faker import Faker
import random
import string

fake = Faker()


def generate_user():
    return {
        "username": fake.profile(fields=None)['username'],
        "plain_password": ''.join([random.choice(string.digits + string.ascii_letters) for i in range(10)]),
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name()
    }


headers = {"Authorization": "Bearer {0}".format(token)}


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def compare_response(self, user_request, user):
        for k, v in user_request.items():
            if not k in ['plain_password']:
                self.assertIn(k, user)
                self.assertEqual(v, user[k])

    def test_add_user(self):
        """Test case for add_user

        Add a new admin user
        """
        test_user = generate_user()
        body = RequestUser.from_dict(test_user)
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_user, response.json)

    def test_get_user(self):
        """Test case for get_user

        Returns user information
        """
        test_user = generate_user()
        body = RequestUser.from_dict(test_user)
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        user_id = response.json['id']

        response = self.client.open(
            '/users/{user_id}'.format(user_id=user_id),
            headers=headers,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.compare_response(test_user, response.json)


if __name__ == '__main__':
    import unittest
    unittest.main()
