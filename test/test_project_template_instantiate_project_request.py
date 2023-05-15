"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.date_variable_request import DateVariableRequest
from asana_preview.model.requested_role_request import RequestedRoleRequest
globals()['DateVariableRequest'] = DateVariableRequest
globals()['RequestedRoleRequest'] = RequestedRoleRequest
from asana_preview.model.project_template_instantiate_project_request import ProjectTemplateInstantiateProjectRequest


class TestProjectTemplateInstantiateProjectRequest(unittest.TestCase):
    """ProjectTemplateInstantiateProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectTemplateInstantiateProjectRequest(self):
        """Test ProjectTemplateInstantiateProjectRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectTemplateInstantiateProjectRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
