"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.error_response import ErrorResponse
from asana_preview.model.error_response5_xx_all_of import ErrorResponse5XXAllOf
from asana_preview.model.error_response5_xx_all_of_errors import ErrorResponse5XXAllOfErrors
globals()['ErrorResponse'] = ErrorResponse
globals()['ErrorResponse5XXAllOf'] = ErrorResponse5XXAllOf
globals()['ErrorResponse5XXAllOfErrors'] = ErrorResponse5XXAllOfErrors
from asana_preview.model.error_response5_xx import ErrorResponse5XX


class TestErrorResponse5XX(unittest.TestCase):
    """ErrorResponse5XX unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testErrorResponse5XX(self):
        """Test ErrorResponse5XX"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ErrorResponse5XX()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
