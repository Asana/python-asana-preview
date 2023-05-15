"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.workspace_compact import WorkspaceCompact
from asana_preview.model.workspace_response_all_of import WorkspaceResponseAllOf
globals()['WorkspaceCompact'] = WorkspaceCompact
globals()['WorkspaceResponseAllOf'] = WorkspaceResponseAllOf
from asana_preview.model.workspace_response import WorkspaceResponse


class TestWorkspaceResponse(unittest.TestCase):
    """WorkspaceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkspaceResponse(self):
        """Test WorkspaceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkspaceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
