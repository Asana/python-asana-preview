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
from asana_preview.model.goal_base_all_of import GoalBaseAllOf
globals()['AsanaResource'] = AsanaResource
globals()['GoalBaseAllOf'] = GoalBaseAllOf
from asana_preview.model.goal_base import GoalBase


class TestGoalBase(unittest.TestCase):
    """GoalBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGoalBase(self):
        """Test GoalBase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GoalBase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
