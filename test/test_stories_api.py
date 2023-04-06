"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.stories_api import StoriesApi  # noqa: E501


class TestStoriesApi(unittest.TestCase):
    """StoriesApi unit test stubs"""

    def setUp(self):
        self.api = StoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_stories_for_task(self):
        """Test case for get_stories_for_task

        Get stories from a task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
