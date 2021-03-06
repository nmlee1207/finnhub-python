# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import finnhub
from finnhub.models.company_executive import CompanyExecutive  # noqa: E501
from finnhub.rest import ApiException

class TestCompanyExecutive(unittest.TestCase):
    """CompanyExecutive unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CompanyExecutive
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.company_executive.CompanyExecutive()  # noqa: E501
        if include_optional :
            return CompanyExecutive(
                symbol = '0', 
                executive = [
                    None
                    ]
            )
        else :
            return CompanyExecutive(
        )

    def testCompanyExecutive(self):
        """Test CompanyExecutive"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
