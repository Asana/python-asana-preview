"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.asana_resource import AsanaResource
from asana_preview.model.status_update_compact_all_of import StatusUpdateCompactAllOf
globals()['AsanaResource'] = AsanaResource
globals()['StatusUpdateCompactAllOf'] = StatusUpdateCompactAllOf
from asana_preview.model.status_update_compact import StatusUpdateCompact


class TestStatusUpdateCompact(unittest.TestCase):
    """StatusUpdateCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStatusUpdateCompact(self):
        """Test StatusUpdateCompact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StatusUpdateCompact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
