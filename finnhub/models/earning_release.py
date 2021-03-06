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


class EarningRelease(object):
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
        'hour': 'str',
        'year': 'int',
        'quarter': 'int',
        'eps_estimate': 'float',
        'eps_actual': 'float',
        'revenue_estimate': 'int',
        'revenue_actual': 'int'
    }

    attribute_map = {
        'symbol': 'symbol',
        'date': 'date',
        'hour': 'hour',
        'year': 'year',
        'quarter': 'quarter',
        'eps_estimate': 'epsEstimate',
        'eps_actual': 'epsActual',
        'revenue_estimate': 'revenueEstimate',
        'revenue_actual': 'revenueActual'
    }

    def __init__(self, symbol=None, date=None, hour=None, year=None, quarter=None, eps_estimate=None, eps_actual=None, revenue_estimate=None, revenue_actual=None, local_vars_configuration=None):  # noqa: E501
        """EarningRelease - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._date = None
        self._hour = None
        self._year = None
        self._quarter = None
        self._eps_estimate = None
        self._eps_actual = None
        self._revenue_estimate = None
        self._revenue_actual = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if date is not None:
            self.date = date
        if hour is not None:
            self.hour = hour
        if year is not None:
            self.year = year
        if quarter is not None:
            self.quarter = quarter
        if eps_estimate is not None:
            self.eps_estimate = eps_estimate
        if eps_actual is not None:
            self.eps_actual = eps_actual
        if revenue_estimate is not None:
            self.revenue_estimate = revenue_estimate
        if revenue_actual is not None:
            self.revenue_actual = revenue_actual

    @property
    def symbol(self):
        """Gets the symbol of this EarningRelease.  # noqa: E501

        Symbol.  # noqa: E501

        :return: The symbol of this EarningRelease.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this EarningRelease.

        Symbol.  # noqa: E501

        :param symbol: The symbol of this EarningRelease.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def date(self):
        """Gets the date of this EarningRelease.  # noqa: E501

        Date.  # noqa: E501

        :return: The date of this EarningRelease.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EarningRelease.

        Date.  # noqa: E501

        :param date: The date of this EarningRelease.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def hour(self):
        """Gets the hour of this EarningRelease.  # noqa: E501

        Indicates whether the earnings is announced before market open(<code>bmo</code>), after market close(<code>amc</code>), or during market hour(<code>dmh</code>).  # noqa: E501

        :return: The hour of this EarningRelease.  # noqa: E501
        :rtype: str
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this EarningRelease.

        Indicates whether the earnings is announced before market open(<code>bmo</code>), after market close(<code>amc</code>), or during market hour(<code>dmh</code>).  # noqa: E501

        :param hour: The hour of this EarningRelease.  # noqa: E501
        :type: str
        """

        self._hour = hour

    @property
    def year(self):
        """Gets the year of this EarningRelease.  # noqa: E501

        Earnings year.  # noqa: E501

        :return: The year of this EarningRelease.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this EarningRelease.

        Earnings year.  # noqa: E501

        :param year: The year of this EarningRelease.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def quarter(self):
        """Gets the quarter of this EarningRelease.  # noqa: E501

        Earnings quarter.  # noqa: E501

        :return: The quarter of this EarningRelease.  # noqa: E501
        :rtype: int
        """
        return self._quarter

    @quarter.setter
    def quarter(self, quarter):
        """Sets the quarter of this EarningRelease.

        Earnings quarter.  # noqa: E501

        :param quarter: The quarter of this EarningRelease.  # noqa: E501
        :type: int
        """

        self._quarter = quarter

    @property
    def eps_estimate(self):
        """Gets the eps_estimate of this EarningRelease.  # noqa: E501

        EPS estimate.  # noqa: E501

        :return: The eps_estimate of this EarningRelease.  # noqa: E501
        :rtype: float
        """
        return self._eps_estimate

    @eps_estimate.setter
    def eps_estimate(self, eps_estimate):
        """Sets the eps_estimate of this EarningRelease.

        EPS estimate.  # noqa: E501

        :param eps_estimate: The eps_estimate of this EarningRelease.  # noqa: E501
        :type: float
        """

        self._eps_estimate = eps_estimate

    @property
    def eps_actual(self):
        """Gets the eps_actual of this EarningRelease.  # noqa: E501

        EPS actual.  # noqa: E501

        :return: The eps_actual of this EarningRelease.  # noqa: E501
        :rtype: float
        """
        return self._eps_actual

    @eps_actual.setter
    def eps_actual(self, eps_actual):
        """Sets the eps_actual of this EarningRelease.

        EPS actual.  # noqa: E501

        :param eps_actual: The eps_actual of this EarningRelease.  # noqa: E501
        :type: float
        """

        self._eps_actual = eps_actual

    @property
    def revenue_estimate(self):
        """Gets the revenue_estimate of this EarningRelease.  # noqa: E501

        Revenue estimate.  # noqa: E501

        :return: The revenue_estimate of this EarningRelease.  # noqa: E501
        :rtype: int
        """
        return self._revenue_estimate

    @revenue_estimate.setter
    def revenue_estimate(self, revenue_estimate):
        """Sets the revenue_estimate of this EarningRelease.

        Revenue estimate.  # noqa: E501

        :param revenue_estimate: The revenue_estimate of this EarningRelease.  # noqa: E501
        :type: int
        """

        self._revenue_estimate = revenue_estimate

    @property
    def revenue_actual(self):
        """Gets the revenue_actual of this EarningRelease.  # noqa: E501

        Revenue actual.  # noqa: E501

        :return: The revenue_actual of this EarningRelease.  # noqa: E501
        :rtype: int
        """
        return self._revenue_actual

    @revenue_actual.setter
    def revenue_actual(self, revenue_actual):
        """Sets the revenue_actual of this EarningRelease.

        Revenue actual.  # noqa: E501

        :param revenue_actual: The revenue_actual of this EarningRelease.  # noqa: E501
        :type: int
        """

        self._revenue_actual = revenue_actual

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
        if not isinstance(other, EarningRelease):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EarningRelease):
            return True

        return self.to_dict() != other.to_dict()
