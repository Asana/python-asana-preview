"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.tag_base_all_of import TagBaseAllOf
from asana_preview.model.tag_compact import TagCompact
globals()['TagBaseAllOf'] = TagBaseAllOf
globals()['TagCompact'] = TagCompact
from asana_preview.model.tag_base import TagBase


class TestTagBase(unittest.TestCase):
    """TagBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTagBase(self):
        """Test TagBase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TagBase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()