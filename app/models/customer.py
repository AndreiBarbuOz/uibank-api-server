# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.address import Address  # noqa: F401,E501
from app import util


class Customer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, first_name: str=None, last_name: str=None, middle_name: str=None, title: str=None, gender: str=None, email_verified: bool=False, email: str=None, date_of_birth: date=None, employment_status: str=None, residence_status: str=None, addresses: List[Address]=None, accounts_url: str=None, self_url: str=None):  # noqa: E501
        """Customer - a model defined in Swagger

        :param id: The id of this Customer.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this Customer.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Customer.  # noqa: E501
        :type last_name: str
        :param middle_name: The middle_name of this Customer.  # noqa: E501
        :type middle_name: str
        :param title: The title of this Customer.  # noqa: E501
        :type title: str
        :param gender: The gender of this Customer.  # noqa: E501
        :type gender: str
        :param email_verified: The email_verified of this Customer.  # noqa: E501
        :type email_verified: bool
        :param email: The email of this Customer.  # noqa: E501
        :type email: str
        :param date_of_birth: The date_of_birth of this Customer.  # noqa: E501
        :type date_of_birth: date
        :param employment_status: The employment_status of this Customer.  # noqa: E501
        :type employment_status: str
        :param residence_status: The residence_status of this Customer.  # noqa: E501
        :type residence_status: str
        :param addresses: The addresses of this Customer.  # noqa: E501
        :type addresses: List[Address]
        :param accounts_url: The accounts_url of this Customer.  # noqa: E501
        :type accounts_url: str
        :param self_url: The self_url of this Customer.  # noqa: E501
        :type self_url: str
        """
        self.swagger_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'middle_name': str,
            'title': str,
            'gender': str,
            'email_verified': bool,
            'email': str,
            'date_of_birth': date,
            'employment_status': str,
            'residence_status': str,
            'addresses': List[Address],
            'accounts_url': str,
            'self_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'middle_name': 'middle_name',
            'title': 'title',
            'gender': 'gender',
            'email_verified': 'email_verified',
            'email': 'email',
            'date_of_birth': 'date_of_birth',
            'employment_status': 'employment_status',
            'residence_status': 'residence_status',
            'addresses': 'addresses',
            'accounts_url': 'accounts_url',
            'self_url': 'self_url'
        }
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._title = title
        self._gender = gender
        self._email_verified = email_verified
        self._email = email
        self._date_of_birth = date_of_birth
        self._employment_status = employment_status
        self._residence_status = residence_status
        self._addresses = addresses
        self._accounts_url = accounts_url
        self._self_url = self_url

    @classmethod
    def from_dict(cls, dikt) -> 'Customer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Customer of this Customer.  # noqa: E501
        :rtype: Customer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Customer.


        :param id: The id of this Customer.
        :type id: int
        """

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Customer.


        :return: The first_name of this Customer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Customer.


        :return: The last_name of this Customer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def middle_name(self) -> str:
        """Gets the middle_name of this Customer.


        :return: The middle_name of this Customer.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name: str):
        """Sets the middle_name of this Customer.


        :param middle_name: The middle_name of this Customer.
        :type middle_name: str
        """

        self._middle_name = middle_name

    @property
    def title(self) -> str:
        """Gets the title of this Customer.

        Title of customer  # noqa: E501

        :return: The title of this Customer.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Customer.

        Title of customer  # noqa: E501

        :param title: The title of this Customer.
        :type title: str
        """
        allowed_values = ["mr", "mrs", "miss", "ms", "doc"]  # noqa: E501
        if title not in allowed_values:
            raise ValueError(
                "Invalid value for `title` ({0}), must be one of {1}"
                .format(title, allowed_values)
            )

        self._title = title

    @property
    def gender(self) -> str:
        """Gets the gender of this Customer.

        Gender of customer  # noqa: E501

        :return: The gender of this Customer.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this Customer.

        Gender of customer  # noqa: E501

        :param gender: The gender of this Customer.
        :type gender: str
        """
        allowed_values = ["male", "female"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def email_verified(self) -> bool:
        """Gets the email_verified of this Customer.


        :return: The email_verified of this Customer.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified: bool):
        """Sets the email_verified of this Customer.


        :param email_verified: The email_verified of this Customer.
        :type email_verified: bool
        """

        self._email_verified = email_verified

    @property
    def email(self) -> str:
        """Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Customer.


        :param email: The email of this Customer.
        :type email: str
        """

        self._email = email

    @property
    def date_of_birth(self) -> date:
        """Gets the date_of_birth of this Customer.


        :return: The date_of_birth of this Customer.
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        """Sets the date_of_birth of this Customer.


        :param date_of_birth: The date_of_birth of this Customer.
        :type date_of_birth: date
        """

        self._date_of_birth = date_of_birth

    @property
    def employment_status(self) -> str:
        """Gets the employment_status of this Customer.


        :return: The employment_status of this Customer.
        :rtype: str
        """
        return self._employment_status

    @employment_status.setter
    def employment_status(self, employment_status: str):
        """Sets the employment_status of this Customer.


        :param employment_status: The employment_status of this Customer.
        :type employment_status: str
        """
        allowed_values = ["permanent", "unemployed", "consultant"]  # noqa: E501
        if employment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `employment_status` ({0}), must be one of {1}"
                .format(employment_status, allowed_values)
            )

        self._employment_status = employment_status

    @property
    def residence_status(self) -> str:
        """Gets the residence_status of this Customer.


        :return: The residence_status of this Customer.
        :rtype: str
        """
        return self._residence_status

    @residence_status.setter
    def residence_status(self, residence_status: str):
        """Sets the residence_status of this Customer.


        :param residence_status: The residence_status of this Customer.
        :type residence_status: str
        """
        allowed_values = ["resident", "foreigner"]  # noqa: E501
        if residence_status not in allowed_values:
            raise ValueError(
                "Invalid value for `residence_status` ({0}), must be one of {1}"
                .format(residence_status, allowed_values)
            )

        self._residence_status = residence_status

    @property
    def addresses(self) -> List[Address]:
        """Gets the addresses of this Customer.


        :return: The addresses of this Customer.
        :rtype: List[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses: List[Address]):
        """Sets the addresses of this Customer.


        :param addresses: The addresses of this Customer.
        :type addresses: List[Address]
        """

        self._addresses = addresses

    @property
    def accounts_url(self) -> str:
        """Gets the accounts_url of this Customer.


        :return: The accounts_url of this Customer.
        :rtype: str
        """
        return self._accounts_url

    @accounts_url.setter
    def accounts_url(self, accounts_url: str):
        """Sets the accounts_url of this Customer.


        :param accounts_url: The accounts_url of this Customer.
        :type accounts_url: str
        """

        self._accounts_url = accounts_url

    @property
    def self_url(self) -> str:
        """Gets the self_url of this Customer.


        :return: The self_url of this Customer.
        :rtype: str
        """
        return self._self_url

    @self_url.setter
    def self_url(self, self_url: str):
        """Sets the self_url of this Customer.


        :param self_url: The self_url of this Customer.
        :type self_url: str
        """

        self._self_url = self_url