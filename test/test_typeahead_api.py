"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.typeahead_api import TypeaheadApi  # noqa: E501


class TestTypeaheadApi(unittest.TestCase):
    """TypeaheadApi unit test stubs"""

    def setUp(self):
        self.api = TypeaheadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_typeahead_for_workspace(self):
        """Test case for typeahead_for_workspace

        Get objects via typeahead  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()