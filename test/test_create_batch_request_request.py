"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import asana_preview
from asana_preview.model.batch_request import BatchRequest
globals()['BatchRequest'] = BatchRequest
from asana_preview.model.create_batch_request_request import CreateBatchRequestRequest


class TestCreateBatchRequestRequest(unittest.TestCase):
    """CreateBatchRequestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateBatchRequestRequest(self):
        """Test CreateBatchRequestRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateBatchRequestRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()