# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class RequestTransaction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amount: float=None, transaction_type: str=None, description: str=None, account: str=None):  # noqa: E501
        """RequestTransaction - a model defined in Swagger

        :param amount: The amount of this RequestTransaction.  # noqa: E501
        :type amount: float
        :param transaction_type: The transaction_type of this RequestTransaction.  # noqa: E501
        :type transaction_type: str
        :param description: The description of this RequestTransaction.  # noqa: E501
        :type description: str
        :param account: The account of this RequestTransaction.  # noqa: E501
        :type account: str
        """
        self.swagger_types = {
            'amount': float,
            'transaction_type': str,
            'description': str,
            'account': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'transaction_type': 'transaction_type',
            'description': 'description',
            'account': 'account'
        }
        self._amount = amount
        self._transaction_type = transaction_type
        self._description = description
        self._account = account

    @classmethod
    def from_dict(cls, dikt) -> 'RequestTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestTransaction of this RequestTransaction.  # noqa: E501
        :rtype: RequestTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> float:
        """Gets the amount of this RequestTransaction.


        :return: The amount of this RequestTransaction.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this RequestTransaction.


        :param amount: The amount of this RequestTransaction.
        :type amount: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def transaction_type(self) -> str:
        """Gets the transaction_type of this RequestTransaction.

        Transaction type  # noqa: E501

        :return: The transaction_type of this RequestTransaction.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        """Sets the transaction_type of this RequestTransaction.

        Transaction type  # noqa: E501

        :param transaction_type: The transaction_type of this RequestTransaction.
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
    def description(self) -> str:
        """Gets the description of this RequestTransaction.


        :return: The description of this RequestTransaction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this RequestTransaction.


        :param description: The description of this RequestTransaction.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def account(self) -> str:
        """Gets the account of this RequestTransaction.


        :return: The account of this RequestTransaction.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account: str):
        """Sets the account of this RequestTransaction.


        :param account: The account of this RequestTransaction.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account
