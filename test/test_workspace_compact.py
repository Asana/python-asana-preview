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
from asana_preview.model.workspace_compact_all_of import WorkspaceCompactAllOf
globals()['AsanaResource'] = AsanaResource
globals()['WorkspaceCompactAllOf'] = WorkspaceCompactAllOf
from asana_preview.model.workspace_compact import WorkspaceCompact


class TestWorkspaceCompact(unittest.TestCase):
    """WorkspaceCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkspaceCompact(self):
        """Test WorkspaceCompact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkspaceCompact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
