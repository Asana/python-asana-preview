"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.membership_request import MembershipRequest
globals()['MembershipRequest'] = MembershipRequest
from asana_preview.model.update_membership_request import UpdateMembershipRequest


class TestUpdateMembershipRequest(unittest.TestCase):
    """UpdateMembershipRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateMembershipRequest(self):
        """Test UpdateMembershipRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateMembershipRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
