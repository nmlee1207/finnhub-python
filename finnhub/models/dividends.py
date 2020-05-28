# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from finnhub.configuration import Configuration


class Dividends(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'symbol': 'str',
        'date': 'date',
        'amount': 'float',
        'pay_date': 'date',
        'record_date': 'date',
        'declaration_date': 'date',
        'currency': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'date': 'Date',
        'amount': 'Amount',
        'pay_date': 'payDate',
        'record_date': 'recordDate',
        'declaration_date': 'declarationDate',
        'currency': 'currency'
    }

    def __init__(self, symbol=None, date=None, amount=None, pay_date=None, record_date=None, declaration_date=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """Dividends - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._date = None
        self._amount = None
        self._pay_date = None
        self._record_date = None
        self._declaration_date = None
        self._currency = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if pay_date is not None:
            self.pay_date = pay_date
        if record_date is not None:
            self.record_date = record_date
        if declaration_date is not None:
            self.declaration_date = declaration_date
        if currency is not None:
            self.currency = currency

    @property
    def symbol(self):
        """Gets the symbol of this Dividends.  # noqa: E501

        Symbol.  # noqa: E501

        :return: The symbol of this Dividends.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Dividends.

        Symbol.  # noqa: E501

        :param symbol: The symbol of this Dividends.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def date(self):
        """Gets the date of this Dividends.  # noqa: E501

        Ex-Dividend date.  # noqa: E501

        :return: The date of this Dividends.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Dividends.

        Ex-Dividend date.  # noqa: E501

        :param date: The date of this Dividends.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this Dividends.  # noqa: E501

        Amount in local currency.  # noqa: E501

        :return: The amount of this Dividends.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Dividends.

        Amount in local currency.  # noqa: E501

        :param amount: The amount of this Dividends.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def pay_date(self):
        """Gets the pay_date of this Dividends.  # noqa: E501

        Pay date.  # noqa: E501

        :return: The pay_date of this Dividends.  # noqa: E501
        :rtype: date
        """
        return self._pay_date

    @pay_date.setter
    def pay_date(self, pay_date):
        """Sets the pay_date of this Dividends.

        Pay date.  # noqa: E501

        :param pay_date: The pay_date of this Dividends.  # noqa: E501
        :type: date
        """

        self._pay_date = pay_date

    @property
    def record_date(self):
        """Gets the record_date of this Dividends.  # noqa: E501

        Record date.  # noqa: E501

        :return: The record_date of this Dividends.  # noqa: E501
        :rtype: date
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this Dividends.

        Record date.  # noqa: E501

        :param record_date: The record_date of this Dividends.  # noqa: E501
        :type: date
        """

        self._record_date = record_date

    @property
    def declaration_date(self):
        """Gets the declaration_date of this Dividends.  # noqa: E501

        Declaration date.  # noqa: E501

        :return: The declaration_date of this Dividends.  # noqa: E501
        :rtype: date
        """
        return self._declaration_date

    @declaration_date.setter
    def declaration_date(self, declaration_date):
        """Sets the declaration_date of this Dividends.

        Declaration date.  # noqa: E501

        :param declaration_date: The declaration_date of this Dividends.  # noqa: E501
        :type: date
        """

        self._declaration_date = declaration_date

    @property
    def currency(self):
        """Gets the currency of this Dividends.  # noqa: E501

        Currency.  # noqa: E501

        :return: The currency of this Dividends.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Dividends.

        Currency.  # noqa: E501

        :param currency: The currency of this Dividends.  # noqa: E501
        :type: str
        """

        self._currency = currency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Dividends):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dividends):
            return True

        return self.to_dict() != other.to_dict()