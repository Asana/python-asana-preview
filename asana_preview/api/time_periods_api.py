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
from asana_preview.model.get_time_period200_response import GetTimePeriod200Response
from asana_preview.model.get_time_periods200_response import GetTimePeriods200Response


class TimePeriodsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_time_period_endpoint = _Endpoint(
            settings={
                'response_type': (GetTimePeriod200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/time_periods/{time_period_gid}',
                'operation_id': 'get_time_period',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'time_period_gid',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'time_period_gid',
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

                        "PARENT": "parent",
                        "END_ON": "end_on",
                        "START_ON": "start_on",
                        "PERIOD": "period",
                        "DISPLAY_NAME": "display_name"
                    },
                },
                'openapi_types': {
                    'time_period_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'time_period_gid': 'time_period_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'time_period_gid': 'path',
                    'opt_pretty': 'query',
                    'opt_fields': 'query',
                },
                'collection_format_map': {
                    'opt_fields': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_time_periods_endpoint = _Endpoint(
            settings={
                'response_type': (GetTimePeriods200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/time_periods',
                'operation_id': 'get_time_periods',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'start_on',
                    'end_on',
                    'opt_fields',
                ],
                'required': [
                    'workspace',
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

                        "PARENT": "parent",
                        "END_ON": "end_on",
                        "START_ON": "start_on",
                        "PERIOD": "period",
                        "DISPLAY_NAME": "display_name"
                    },
                },
                'openapi_types': {
                    'workspace':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                    'start_on':
                        (date,),
                    'end_on':
                        (date,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'start_on': 'start_on',
                    'end_on': 'end_on',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'workspace': 'query',
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'start_on': 'query',
                    'end_on': 'query',
                    'opt_fields': 'query',
                },
                'collection_format_map': {
                    'opt_fields': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_time_period(
        self,
        time_period_gid,
        **kwargs
    ):
        """Get a time period  # noqa: E501

        Returns the full record for a single time period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_time_period(time_period_gid, async_req=True)
        >>> result = thread.get()

        Args:
            time_period_gid (str): Globally unique identifier for the time period.

        Keyword Args:
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
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
            GetTimePeriod200Response
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
        kwargs['time_period_gid'] = \
            time_period_gid
        return self.get_time_period_endpoint.call_with_http_info(**kwargs)

    def get_time_periods(
        self,
        workspace,
        **kwargs
    ):
        """Get time periods  # noqa: E501

        Returns compact time period records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_time_periods(workspace, async_req=True)
        >>> result = thread.get()

        Args:
            workspace (str): Globally unique identifier for the workspace.

        Keyword Args:
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): Results per page. The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'. [optional]
            start_on (date): ISO 8601 date string. [optional]
            end_on (date): ISO 8601 date string. [optional]
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
            GetTimePeriods200Response
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
        kwargs['workspace'] = \
            workspace
        return self.get_time_periods_endpoint.call_with_http_info(**kwargs)

