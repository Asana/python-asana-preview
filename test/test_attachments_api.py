# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import asana_preview
from asana_preview.api.attachments_api import AttachmentsApi  # noqa: E501
from asana_preview.rest import ApiException


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_attachment_for_object(self):
        """Test case for create_attachment_for_object

        Upload an attachment  # noqa: E501
        """
        pass

    def test_delete_attachment(self):
        """Test case for delete_attachment

        Delete an attachment  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Get an attachment  # noqa: E501
        """
        pass

    def test_get_attachments_for_object(self):
        """Test case for get_attachments_for_object

        Get attachments from an object  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
