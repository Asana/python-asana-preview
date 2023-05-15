"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.project_brief_base import ProjectBriefBase
from asana_preview.model.project_brief_response_all_of import ProjectBriefResponseAllOf
globals()['ProjectBriefBase'] = ProjectBriefBase
globals()['ProjectBriefResponseAllOf'] = ProjectBriefResponseAllOf
from asana_preview.model.project_brief_response import ProjectBriefResponse


class TestProjectBriefResponse(unittest.TestCase):
    """ProjectBriefResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectBriefResponse(self):
        """Test ProjectBriefResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectBriefResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
