"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.task_add_tag_request import TaskAddTagRequest
globals()['TaskAddTagRequest'] = TaskAddTagRequest
from asana_preview.model.add_tag_for_task_request import AddTagForTaskRequest


class TestAddTagForTaskRequest(unittest.TestCase):
    """AddTagForTaskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddTagForTaskRequest(self):
        """Test AddTagForTaskRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddTagForTaskRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
