"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.batch_api_api import BatchAPIApi  # noqa: E501


class TestBatchAPIApi(unittest.TestCase):
    """BatchAPIApi unit test stubs"""

    def setUp(self):
        self.api = BatchAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_batch_request(self):
        """Test case for create_batch_request

        Submit parallel requests  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()