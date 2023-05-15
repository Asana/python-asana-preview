"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.team_add_user_request import TeamAddUserRequest
globals()['TeamAddUserRequest'] = TeamAddUserRequest
from asana_preview.model.add_user_for_team_request import AddUserForTeamRequest


class TestAddUserForTeamRequest(unittest.TestCase):
    """AddUserForTeamRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddUserForTeamRequest(self):
        """Test AddUserForTeamRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddUserForTeamRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
