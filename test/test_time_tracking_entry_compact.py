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
from asana_preview.model.time_tracking_entry_compact_all_of import TimeTrackingEntryCompactAllOf
from asana_preview.model.user_compact import UserCompact
globals()['AsanaResource'] = AsanaResource
globals()['TimeTrackingEntryCompactAllOf'] = TimeTrackingEntryCompactAllOf
globals()['UserCompact'] = UserCompact
from asana_preview.model.time_tracking_entry_compact import TimeTrackingEntryCompact


class TestTimeTrackingEntryCompact(unittest.TestCase):
    """TimeTrackingEntryCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeTrackingEntryCompact(self):
        """Test TimeTrackingEntryCompact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeTrackingEntryCompact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
