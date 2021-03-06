# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class Account(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, account_number: int=None, date_start: date=None, friendly_name: str=None, account_type: str=None, self_url: str=None, customer_url: str=None, cards_url: str=None, balance: float=None):  # noqa: E501
        """Account - a model defined in Swagger

        :param id: The id of this Account.  # noqa: E501
        :type id: str
        :param account_number: The account_number of this Account.  # noqa: E501
        :type account_number: int
        :param date_start: The date_start of this Account.  # noqa: E501
        :type date_start: date
        :param friendly_name: The friendly_name of this Account.  # noqa: E501
        :type friendly_name: str
        :param account_type: The account_type of this Account.  # noqa: E501
        :type account_type: str
        :param self_url: The self_url of this Account.  # noqa: E501
        :type self_url: str
        :param customer_url: The customer_url of this Account.  # noqa: E501
        :type customer_url: str
        :param cards_url: The cards_url of this Account.  # noqa: E501
        :type cards_url: str
        :param balance: The balance of this Account.  # noqa: E501
        :type balance: float
        """
        self.swagger_types = {
            'id': str,
            'account_number': int,
            'date_start': date,
            'friendly_name': str,
            'account_type': str,
            'self_url': str,
            'customer_url': str,
            'cards_url': str,
            'balance': float
        }

        self.attribute_map = {
            'id': 'id',
            'account_number': 'account_number',
            'date_start': 'date_start',
            'friendly_name': 'friendly_name',
            'account_type': 'account_type',
            'self_url': 'self_url',
            'customer_url': 'customer_url',
            'cards_url': 'cards_url',
            'balance': 'balance'
        }
        self._id = id
        self._account_number = account_number
        self._date_start = date_start
        self._friendly_name = friendly_name
        self._account_type = account_type
        self._self_url = self_url
        self._customer_url = customer_url
        self._cards_url = cards_url
        self._balance = balance

    @classmethod
    def from_dict(cls, dikt) -> 'Account':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Account of this Account.  # noqa: E501
        :rtype: Account
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Account.


        :return: The id of this Account.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Account.


        :param id: The id of this Account.
        :type id: str
        """

        self._id = id

    @property
    def account_number(self) -> int:
        """Gets the account_number of this Account.


        :return: The account_number of this Account.
        :rtype: int
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: int):
        """Sets the account_number of this Account.


        :param account_number: The account_number of this Account.
        :type account_number: int
        """

        self._account_number = account_number

    @property
    def date_start(self) -> date:
        """Gets the date_start of this Account.


        :return: The date_start of this Account.
        :rtype: date
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: date):
        """Sets the date_start of this Account.


        :param date_start: The date_start of this Account.
        :type date_start: date
        """

        self._date_start = date_start

    @property
    def friendly_name(self) -> str:
        """Gets the friendly_name of this Account.


        :return: The friendly_name of this Account.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name: str):
        """Sets the friendly_name of this Account.


        :param friendly_name: The friendly_name of this Account.
        :type friendly_name: str
        """

        self._friendly_name = friendly_name

    @property
    def account_type(self) -> str:
        """Gets the account_type of this Account.


        :return: The account_type of this Account.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type: str):
        """Sets the account_type of this Account.


        :param account_type: The account_type of this Account.
        :type account_type: str
        """
        allowed_values = ["checking", "savings"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def self_url(self) -> str:
        """Gets the self_url of this Account.


        :return: The self_url of this Account.
        :rtype: str
        """
        return self._self_url

    @self_url.setter
    def self_url(self, self_url: str):
        """Sets the self_url of this Account.


        :param self_url: The self_url of this Account.
        :type self_url: str
        """

        self._self_url = self_url

    @property
    def customer_url(self) -> str:
        """Gets the customer_url of this Account.


        :return: The customer_url of this Account.
        :rtype: str
        """
        return self._customer_url

    @customer_url.setter
    def customer_url(self, customer_url: str):
        """Sets the customer_url of this Account.


        :param customer_url: The customer_url of this Account.
        :type customer_url: str
        """

        self._customer_url = customer_url

    @property
    def cards_url(self) -> str:
        """Gets the cards_url of this Account.


        :return: The cards_url of this Account.
        :rtype: str
        """
        return self._cards_url

    @cards_url.setter
    def cards_url(self, cards_url: str):
        """Sets the cards_url of this Account.


        :param cards_url: The cards_url of this Account.
        :type cards_url: str
        """

        self._cards_url = cards_url

    @property
    def balance(self) -> float:
        """Gets the balance of this Account.


        :return: The balance of this Account.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        """Sets the balance of this Account.


        :param balance: The balance of this Account.
        :type balance: float
        """

        self._balance = balance
