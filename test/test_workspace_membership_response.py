"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.user_compact import UserCompact
from asana_preview.model.user_task_list_compact import UserTaskListCompact
from asana_preview.model.workspace_compact import WorkspaceCompact
from asana_preview.model.workspace_membership_compact import WorkspaceMembershipCompact
from asana_preview.model.workspace_membership_response_all_of import WorkspaceMembershipResponseAllOf
from asana_preview.model.workspace_membership_response_all_of_vacation_dates import WorkspaceMembershipResponseAllOfVacationDates
globals()['UserCompact'] = UserCompact
globals()['UserTaskListCompact'] = UserTaskListCompact
globals()['WorkspaceCompact'] = WorkspaceCompact
globals()['WorkspaceMembershipCompact'] = WorkspaceMembershipCompact
globals()['WorkspaceMembershipResponseAllOf'] = WorkspaceMembershipResponseAllOf
globals()['WorkspaceMembershipResponseAllOfVacationDates'] = WorkspaceMembershipResponseAllOfVacationDates
from asana_preview.model.workspace_membership_response import WorkspaceMembershipResponse


class TestWorkspaceMembershipResponse(unittest.TestCase):
    """WorkspaceMembershipResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkspaceMembershipResponse(self):
        """Test WorkspaceMembershipResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkspaceMembershipResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
