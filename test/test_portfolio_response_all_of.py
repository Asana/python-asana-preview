"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.custom_field_compact import CustomFieldCompact
from asana_preview.model.custom_field_setting_response import CustomFieldSettingResponse
from asana_preview.model.project_template_compact import ProjectTemplateCompact
from asana_preview.model.user_compact import UserCompact
globals()['CustomFieldCompact'] = CustomFieldCompact
globals()['CustomFieldSettingResponse'] = CustomFieldSettingResponse
globals()['ProjectTemplateCompact'] = ProjectTemplateCompact
globals()['UserCompact'] = UserCompact
from asana_preview.model.portfolio_response_all_of import PortfolioResponseAllOf


class TestPortfolioResponseAllOf(unittest.TestCase):
    """PortfolioResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPortfolioResponseAllOf(self):
        """Test PortfolioResponseAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PortfolioResponseAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()