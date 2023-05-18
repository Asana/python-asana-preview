"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from asana_preview.api_client import ApiClient, Endpoint as _Endpoint
from asana_preview.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from asana_preview.model.error_response import ErrorResponse
from asana_preview.model.get_custom_field_settings_for_project200_response import GetCustomFieldSettingsForProject200Response


class CustomFieldSettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_custom_field_settings_for_portfolio_endpoint = _Endpoint(
            settings={
                'response_type': (GetCustomFieldSettingsForProject200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/portfolios/{portfolio_gid}/custom_field_settings',
                'operation_id': 'get_custom_field_settings_for_portfolio',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'portfolio_gid',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'opt_fields',
                ],
                'required': [
                    'portfolio_gid',
                ],
                'nullable': [
                ],
                'enum': [
                    'opt_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('opt_fields',): {

                        "PROJECT": "project",
                        "IS_IMPORTANT": "is_important",
                        "CUSTOM_FIELD": "custom_field",
                        "PARENT": "parent"
                    },
                },
                'openapi_types': {
                    'portfolio_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'portfolio_gid': 'portfolio_gid',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'portfolio_gid': 'path',
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'opt_fields': 'query',
                },
                'collection_format_map': {
                    'opt_fields': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json; charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_custom_field_settings_for_project_endpoint = _Endpoint(
            settings={
                'response_type': (GetCustomFieldSettingsForProject200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/projects/{project_gid}/custom_field_settings',
                'operation_id': 'get_custom_field_settings_for_project',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_gid',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'opt_fields',
                ],
                'required': [
                    'project_gid',
                ],
                'nullable': [
                ],
                'enum': [
                    'opt_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('opt_fields',): {

                        "PROJECT": "project",
                        "IS_IMPORTANT": "is_important",
                        "CUSTOM_FIELD": "custom_field",
                        "PARENT": "parent"
                    },
                },
                'openapi_types': {
                    'project_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'project_gid': 'project_gid',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'project_gid': 'path',
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'opt_fields': 'query',
                },
                'collection_format_map': {
                    'opt_fields': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json; charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_custom_field_settings_for_portfolio(
        self,
        portfolio_gid,
        **kwargs
    ):
        """Get a portfolio's custom fields  # noqa: E501

        Returns a list of all of the custom fields settings on a portfolio, in compact form.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_custom_field_settings_for_portfolio(portfolio_gid, async_req=True)
        >>> result = thread.get()

        Args:
            portfolio_gid (str): Globally unique identifier for the portfolio.

        Keyword Args:
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): Results per page. The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'. [optional]
            opt_fields ([str]): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetCustomFieldSettingsForProject200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['portfolio_gid'] = \
            portfolio_gid
        return self.get_custom_field_settings_for_portfolio_endpoint.call_with_http_info(**kwargs)

    def get_custom_field_settings_for_project(
        self,
        project_gid,
        **kwargs
    ):
        """Get a project's custom fields  # noqa: E501

        Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [documentation for input/output options](https://developers.asana.com/docs/inputoutput-options) for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_custom_field_settings_for_project(project_gid, async_req=True)
        >>> result = thread.get()

        Args:
            project_gid (str): Globally unique identifier for the project.

        Keyword Args:
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): Results per page. The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'. [optional]
            opt_fields ([str]): This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetCustomFieldSettingsForProject200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_gid'] = \
            project_gid
        return self.get_custom_field_settings_for_project_endpoint.call_with_http_info(**kwargs)
