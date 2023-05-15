"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.custom_field_base import CustomFieldBase
from asana_preview.model.custom_field_compact_all_of_date_value import CustomFieldCompactAllOfDateValue
from asana_preview.model.custom_field_request_all_of import CustomFieldRequestAllOf
from asana_preview.model.enum_option import EnumOption
globals()['CustomFieldBase'] = CustomFieldBase
globals()['CustomFieldCompactAllOfDateValue'] = CustomFieldCompactAllOfDateValue
globals()['CustomFieldRequestAllOf'] = CustomFieldRequestAllOf
globals()['EnumOption'] = EnumOption
from asana_preview.model.custom_field_request import CustomFieldRequest


class TestCustomFieldRequest(unittest.TestCase):
    """CustomFieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomFieldRequest(self):
        """Test CustomFieldRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomFieldRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
