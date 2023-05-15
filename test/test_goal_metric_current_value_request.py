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
from asana_preview.model.goal_metric_current_value_request_all_of import GoalMetricCurrentValueRequestAllOf
globals()['AsanaResource'] = AsanaResource
globals()['GoalMetricCurrentValueRequestAllOf'] = GoalMetricCurrentValueRequestAllOf
from asana_preview.model.goal_metric_current_value_request import GoalMetricCurrentValueRequest


class TestGoalMetricCurrentValueRequest(unittest.TestCase):
    """GoalMetricCurrentValueRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGoalMetricCurrentValueRequest(self):
        """Test GoalMetricCurrentValueRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GoalMetricCurrentValueRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
