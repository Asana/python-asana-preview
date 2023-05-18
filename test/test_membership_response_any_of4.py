"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.custom_field_response_people_value_inner import CustomFieldResponsePeopleValueInner
from asana_preview.model.goal_response_workspace import GoalResponseWorkspace
from asana_preview.model.membership_response_any_of4_user_task_list import MembershipResponseAnyOf4UserTaskList
from asana_preview.model.workspace_membership_response_vacation_dates import WorkspaceMembershipResponseVacationDates
globals()['CustomFieldResponsePeopleValueInner'] = CustomFieldResponsePeopleValueInner
globals()['GoalResponseWorkspace'] = GoalResponseWorkspace
globals()['MembershipResponseAnyOf4UserTaskList'] = MembershipResponseAnyOf4UserTaskList
globals()['WorkspaceMembershipResponseVacationDates'] = WorkspaceMembershipResponseVacationDates
from asana_preview.model.membership_response_any_of4 import MembershipResponseAnyOf4


class TestMembershipResponseAnyOf4(unittest.TestCase):
    """MembershipResponseAnyOf4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMembershipResponseAnyOf4(self):
        """Test MembershipResponseAnyOf4"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MembershipResponseAnyOf4()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
