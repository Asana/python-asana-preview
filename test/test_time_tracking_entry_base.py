"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.task_compact import TaskCompact
from asana_preview.model.time_tracking_entry_base_all_of import TimeTrackingEntryBaseAllOf
from asana_preview.model.time_tracking_entry_compact import TimeTrackingEntryCompact
from asana_preview.model.user_compact import UserCompact
globals()['TaskCompact'] = TaskCompact
globals()['TimeTrackingEntryBaseAllOf'] = TimeTrackingEntryBaseAllOf
globals()['TimeTrackingEntryCompact'] = TimeTrackingEntryCompact
globals()['UserCompact'] = UserCompact
from asana_preview.model.time_tracking_entry_base import TimeTrackingEntryBase


class TestTimeTrackingEntryBase(unittest.TestCase):
    """TimeTrackingEntryBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeTrackingEntryBase(self):
        """Test TimeTrackingEntryBase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeTrackingEntryBase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
