"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.rule_trigger_request import RuleTriggerRequest
globals()['RuleTriggerRequest'] = RuleTriggerRequest
from asana_preview.model.trigger_rule_request import TriggerRuleRequest


class TestTriggerRuleRequest(unittest.TestCase):
    """TriggerRuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTriggerRuleRequest(self):
        """Test TriggerRuleRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TriggerRuleRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()