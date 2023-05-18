"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.modify_dependents_request import ModifyDependentsRequest
globals()['ModifyDependentsRequest'] = ModifyDependentsRequest
from asana_preview.model.add_dependents_for_task_request import AddDependentsForTaskRequest


class TestAddDependentsForTaskRequest(unittest.TestCase):
    """AddDependentsForTaskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddDependentsForTaskRequest(self):
        """Test AddDependentsForTaskRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddDependentsForTaskRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()