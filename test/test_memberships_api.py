"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.memberships_api import MembershipsApi  # noqa: E501


class TestMembershipsApi(unittest.TestCase):
    """MembershipsApi unit test stubs"""

    def setUp(self):
        self.api = MembershipsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_membership(self):
        """Test case for create_membership

        Create a membership  # noqa: E501
        """
        pass

    def test_delete_membership(self):
        """Test case for delete_membership

        Delete a membership  # noqa: E501
        """
        pass

    def test_get_memberships(self):
        """Test case for get_memberships

        Get multiple memberships  # noqa: E501
        """
        pass

    def test_update_membership(self):
        """Test case for update_membership

        Update a membership  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()