"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.asana_resource import AsanaResource
from asana_preview.model.custom_field_compact_all_of import CustomFieldCompactAllOf
from asana_preview.model.custom_field_compact_all_of_date_value import CustomFieldCompactAllOfDateValue
from asana_preview.model.enum_option import EnumOption
globals()['AsanaResource'] = AsanaResource
globals()['CustomFieldCompactAllOf'] = CustomFieldCompactAllOf
globals()['CustomFieldCompactAllOfDateValue'] = CustomFieldCompactAllOfDateValue
globals()['EnumOption'] = EnumOption
from asana_preview.model.custom_field_compact import CustomFieldCompact


class TestCustomFieldCompact(unittest.TestCase):
    """CustomFieldCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomFieldCompact(self):
        """Test CustomFieldCompact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomFieldCompact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
