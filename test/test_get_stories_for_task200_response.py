"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.next_page import NextPage
from asana_preview.model.story_compact import StoryCompact
globals()['NextPage'] = NextPage
globals()['StoryCompact'] = StoryCompact
from asana_preview.model.get_stories_for_task200_response import GetStoriesForTask200Response


class TestGetStoriesForTask200Response(unittest.TestCase):
    """GetStoriesForTask200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetStoriesForTask200Response(self):
        """Test GetStoriesForTask200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetStoriesForTask200Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
