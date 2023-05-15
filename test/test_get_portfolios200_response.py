"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.portfolio_compact import PortfolioCompact
globals()['PortfolioCompact'] = PortfolioCompact
from asana_preview.model.get_portfolios200_response import GetPortfolios200Response


class TestGetPortfolios200Response(unittest.TestCase):
    """GetPortfolios200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPortfolios200Response(self):
        """Test GetPortfolios200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetPortfolios200Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
