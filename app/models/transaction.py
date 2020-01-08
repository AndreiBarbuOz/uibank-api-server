# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class Transaction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, date_time: datetime=None, amount: float=None, transaction_type: str=None, reference: str=None, description: str=None, balance: str=None, dispute: str=None, self_url: str=None, account_url: str=None):  # noqa: E501
        """Transaction - a model defined in Swagger

        :param id: The id of this Transaction.  # noqa: E501
        :type id: int
        :param date_time: The date_time of this Transaction.  # noqa: E501
        :type date_time: datetime
        :param amount: The amount of this Transaction.  # noqa: E501
        :type amount: float
        :param transaction_type: The transaction_type of this Transaction.  # noqa: E501
        :type transaction_type: str
        :param reference: The reference of this Transaction.  # noqa: E501
        :type reference: str
        :param description: The description of this Transaction.  # noqa: E501
        :type description: str
        :param balance: The balance of this Transaction.  # noqa: E501
        :type balance: str
        :param dispute: The dispute of this Transaction.  # noqa: E501
        :type dispute: str
        :param self_url: The self_url of this Transaction.  # noqa: E501
        :type self_url: str
        :param account_url: The account_url of this Transaction.  # noqa: E501
        :type account_url: str
        """
        self.swagger_types = {
            'id': int,
            'date_time': datetime,
            'amount': float,
            'transaction_type': str,
            'reference': str,
            'description': str,
            'balance': str,
            'dispute': str,
            'self_url': str,
            'account_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'date_time': 'date_time',
            'amount': 'amount',
            'transaction_type': 'transaction_type',
            'reference': 'reference',
            'description': 'description',
            'balance': 'balance',
            'dispute': 'dispute',
            'self_url': 'self_url',
            'account_url': 'account_url'
        }
        self._id = id
        self._date_time = date_time
        self._amount = amount
        self._transaction_type = transaction_type
        self._reference = reference
        self._description = description
        self._balance = balance
        self._dispute = dispute
        self._self_url = self_url
        self._account_url = account_url

    @classmethod
    def from_dict(cls, dikt) -> 'Transaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Transaction of this Transaction.  # noqa: E501
        :rtype: Transaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Transaction.


        :return: The id of this Transaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Transaction.


        :param id: The id of this Transaction.
        :type id: int
        """

        self._id = id

    @property
    def date_time(self) -> datetime:
        """Gets the date_time of this Transaction.


        :return: The date_time of this Transaction.
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time: datetime):
        """Sets the date_time of this Transaction.


        :param date_time: The date_time of this Transaction.
        :type date_time: datetime
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")  # noqa: E501

        self._date_time = date_time

    @property
    def amount(self) -> float:
        """Gets the amount of this Transaction.


        :return: The amount of this Transaction.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.
        :type amount: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def transaction_type(self) -> str:
        """Gets the transaction_type of this Transaction.

        Transaction type  # noqa: E501

        :return: The transaction_type of this Transaction.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        """Sets the transaction_type of this Transaction.

        Transaction type  # noqa: E501

        :param transaction_type: The transaction_type of this Transaction.
        :type transaction_type: str
        """
        allowed_values = ["debit", "credit"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

    @property
    def reference(self) -> str:
        """Gets the reference of this Transaction.


        :return: The reference of this Transaction.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Transaction.


        :param reference: The reference of this Transaction.
        :type reference: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def description(self) -> str:
        """Gets the description of this Transaction.


        :return: The description of this Transaction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Transaction.


        :param description: The description of this Transaction.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def balance(self) -> str:
        """Gets the balance of this Transaction.


        :return: The balance of this Transaction.
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance: str):
        """Sets the balance of this Transaction.


        :param balance: The balance of this Transaction.
        :type balance: str
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def dispute(self) -> str:
        """Gets the dispute of this Transaction.

        If transaction is under dispute  # noqa: E501

        :return: The dispute of this Transaction.
        :rtype: str
        """
        return self._dispute

    @dispute.setter
    def dispute(self, dispute: str):
        """Sets the dispute of this Transaction.

        If transaction is under dispute  # noqa: E501

        :param dispute: The dispute of this Transaction.
        :type dispute: str
        """
        allowed_values = ["no", "reported", "under investigation"]  # noqa: E501
        if dispute not in allowed_values:
            raise ValueError(
                "Invalid value for `dispute` ({0}), must be one of {1}"
                .format(dispute, allowed_values)
            )

        self._dispute = dispute

    @property
    def self_url(self) -> str:
        """Gets the self_url of this Transaction.


        :return: The self_url of this Transaction.
        :rtype: str
        """
        return self._self_url

    @self_url.setter
    def self_url(self, self_url: str):
        """Sets the self_url of this Transaction.


        :param self_url: The self_url of this Transaction.
        :type self_url: str
        """
        if self_url is None:
            raise ValueError("Invalid value for `self_url`, must not be `None`")  # noqa: E501

        self._self_url = self_url

    @property
    def account_url(self) -> str:
        """Gets the account_url of this Transaction.


        :return: The account_url of this Transaction.
        :rtype: str
        """
        return self._account_url

    @account_url.setter
    def account_url(self, account_url: str):
        """Sets the account_url of this Transaction.


        :param account_url: The account_url of this Transaction.
        :type account_url: str
        """
        if account_url is None:
            raise ValueError("Invalid value for `account_url`, must not be `None`")  # noqa: E501

        self._account_url = account_url
