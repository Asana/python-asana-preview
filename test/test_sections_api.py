"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.sections_api import SectionsApi  # noqa: E501


class TestSectionsApi(unittest.TestCase):
    """SectionsApi unit test stubs"""

    def setUp(self):
        self.api = SectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sections_for_project(self):
        """Test case for get_sections_for_project

        Get sections in a project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
