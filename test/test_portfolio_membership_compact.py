"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.asana_resource import AsanaResource
from asana_preview.model.portfolio_compact import PortfolioCompact
from asana_preview.model.portfolio_membership_compact_all_of import PortfolioMembershipCompactAllOf
from asana_preview.model.user_compact import UserCompact
globals()['AsanaResource'] = AsanaResource
globals()['PortfolioCompact'] = PortfolioCompact
globals()['PortfolioMembershipCompactAllOf'] = PortfolioMembershipCompactAllOf
globals()['UserCompact'] = UserCompact
from asana_preview.model.portfolio_membership_compact import PortfolioMembershipCompact


class TestPortfolioMembershipCompact(unittest.TestCase):
    """PortfolioMembershipCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPortfolioMembershipCompact(self):
        """Test PortfolioMembershipCompact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PortfolioMembershipCompact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()