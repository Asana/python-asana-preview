"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import asana_preview
from asana_preview.api.audit_log_api_api import AuditLogAPIApi  # noqa: E501


class TestAuditLogAPIApi(unittest.TestCase):
    """AuditLogAPIApi unit test stubs"""

    def setUp(self):
        self.api = AuditLogAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_audit_log_events(self):
        """Test case for get_audit_log_events

        Get audit log events  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()