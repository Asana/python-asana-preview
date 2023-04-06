"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.custom_field_compact import CustomFieldCompact
from asana_preview.model.custom_field_setting_response import CustomFieldSettingResponse
from asana_preview.model.project_base import ProjectBase
from asana_preview.model.project_response_all_of import ProjectResponseAllOf
from asana_preview.model.user_compact import UserCompact
globals()['CustomFieldCompact'] = CustomFieldCompact
globals()['CustomFieldSettingResponse'] = CustomFieldSettingResponse
globals()['ProjectBase'] = ProjectBase
globals()['ProjectResponseAllOf'] = ProjectResponseAllOf
globals()['UserCompact'] = UserCompact
from asana_preview.model.project_response import ProjectResponse


class TestProjectResponse(unittest.TestCase):
    """ProjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectResponse(self):
        """Test ProjectResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
