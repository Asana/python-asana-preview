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
from asana_preview.model.member_compact_all_of import MemberCompactAllOf
globals()['AsanaResource'] = AsanaResource
globals()['MemberCompactAllOf'] = MemberCompactAllOf
from asana_preview.model.member_compact import MemberCompact


class TestMemberCompact(unittest.TestCase):
    """MemberCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMemberCompact(self):
        """Test MemberCompact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MemberCompact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
