"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.team_memberships_api import TeamMembershipsApi  # noqa: E501


class TestTeamMembershipsApi(unittest.TestCase):
    """TeamMembershipsApi unit test stubs"""

    def setUp(self):
        self.api = TeamMembershipsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_team_membership(self):
        """Test case for get_team_membership

        Get a team membership  # noqa: E501
        """
        pass

    def test_get_team_memberships(self):
        """Test case for get_team_memberships

        Get team memberships  # noqa: E501
        """
        pass

    def test_get_team_memberships_for_team(self):
        """Test case for get_team_memberships_for_team

        Get memberships from a team  # noqa: E501
        """
        pass

    def test_get_team_memberships_for_user(self):
        """Test case for get_team_memberships_for_user

        Get memberships from a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()