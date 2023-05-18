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
from asana_preview.model.create_time_tracking_entry201_response import CreateTimeTrackingEntry201Response
from asana_preview.model.create_time_tracking_entry_request import CreateTimeTrackingEntryRequest
from asana_preview.model.delete_attachment200_response import DeleteAttachment200Response
from asana_preview.model.error_response import ErrorResponse
from asana_preview.model.get_time_tracking_entries_for_task200_response import GetTimeTrackingEntriesForTask200Response
from asana_preview.model.update_time_tracking_entry_request import UpdateTimeTrackingEntryRequest


class TimeTrackingEntriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_time_tracking_entry_endpoint = _Endpoint(
            settings={
                'response_type': (CreateTimeTrackingEntry201Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/tasks/{task_gid}/time_tracking_entries',
                'operation_id': 'create_time_tracking_entry',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_gid',
                    'create_time_tracking_entry_request',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'task_gid',
                    'create_time_tracking_entry_request',
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

                        "CREATED_BY": "created_by",
                        "DURATION_MINUTES": "duration_minutes",
                        "ENTERED_ON": "entered_on",
                        "CREATED_AT": "created_at",
                        "TASK": "task"
                    },
                },
                'openapi_types': {
                    'task_gid':
                        (str,),
                    'create_time_tracking_entry_request':
                        (CreateTimeTrackingEntryRequest,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'task_gid': 'task_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'task_gid': 'path',
                    'create_time_tracking_entry_request': 'body',
                    'opt_pretty': 'query',
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
                'content_type': [
                    'application/json; charset=UTF-8'
                ]
            },
            api_client=api_client
        )
        self.delete_time_tracking_entry_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteAttachment200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/time_tracking_entries/{time_tracking_entry_gid}',
                'operation_id': 'delete_time_tracking_entry',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'time_tracking_entry_gid',
                    'opt_pretty',
                ],
                'required': [
                    'time_tracking_entry_gid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'time_tracking_entry_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                },
                'attribute_map': {
                    'time_tracking_entry_gid': 'time_tracking_entry_gid',
                    'opt_pretty': 'opt_pretty',
                },
                'location_map': {
                    'time_tracking_entry_gid': 'path',
                    'opt_pretty': 'query',
                },
                'collection_format_map': {
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
        self.get_time_tracking_entries_for_task_endpoint = _Endpoint(
            settings={
                'response_type': (GetTimeTrackingEntriesForTask200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/tasks/{task_gid}/time_tracking_entries',
                'operation_id': 'get_time_tracking_entries_for_task',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_gid',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'opt_fields',
                ],
                'required': [
                    'task_gid',
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

                        "CREATED_BY": "created_by",
                        "DURATION_MINUTES": "duration_minutes",
                        "ENTERED_ON": "entered_on"
                    },
                },
                'openapi_types': {
                    'task_gid':
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
                    'task_gid': 'task_gid',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'task_gid': 'path',
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
        self.get_time_tracking_entry_endpoint = _Endpoint(
            settings={
                'response_type': (CreateTimeTrackingEntry201Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/time_tracking_entries/{time_tracking_entry_gid}',
                'operation_id': 'get_time_tracking_entry',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'time_tracking_entry_gid',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'time_tracking_entry_gid',
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

                        "CREATED_BY": "created_by",
                        "DURATION_MINUTES": "duration_minutes",
                        "ENTERED_ON": "entered_on",
                        "CREATED_AT": "created_at",
                        "TASK": "task"
                    },
                },
                'openapi_types': {
                    'time_tracking_entry_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'time_tracking_entry_gid': 'time_tracking_entry_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'time_tracking_entry_gid': 'path',
                    'opt_pretty': 'query',
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
        self.update_time_tracking_entry_endpoint = _Endpoint(
            settings={
                'response_type': (CreateTimeTrackingEntry201Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/time_tracking_entries/{time_tracking_entry_gid}',
                'operation_id': 'update_time_tracking_entry',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'time_tracking_entry_gid',
                    'update_time_tracking_entry_request',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'time_tracking_entry_gid',
                    'update_time_tracking_entry_request',
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

                        "CREATED_BY": "created_by",
                        "DURATION_MINUTES": "duration_minutes",
                        "ENTERED_ON": "entered_on",
                        "CREATED_AT": "created_at",
                        "TASK": "task"
                    },
                },
                'openapi_types': {
                    'time_tracking_entry_gid':
                        (str,),
                    'update_time_tracking_entry_request':
                        (UpdateTimeTrackingEntryRequest,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'time_tracking_entry_gid': 'time_tracking_entry_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'time_tracking_entry_gid': 'path',
                    'update_time_tracking_entry_request': 'body',
                    'opt_pretty': 'query',
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
                'content_type': [
                    'application/json; charset=UTF-8'
                ]
            },
            api_client=api_client
        )

    def create_time_tracking_entry(
        self,
        task_gid,
        create_time_tracking_entry_request,
        **kwargs
    ):
        """Create a time tracking entry  # noqa: E501

        Creates a time tracking entry on a given task.  Returns the record of the newly created time tracking entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_time_tracking_entry(task_gid, create_time_tracking_entry_request, async_req=True)
        >>> result = thread.get()

        Args:
            task_gid (str): The task to operate on.
            create_time_tracking_entry_request (CreateTimeTrackingEntryRequest): Information about the time tracking entry.

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
            CreateTimeTrackingEntry201Response
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
        kwargs['task_gid'] = \
            task_gid
        kwargs['create_time_tracking_entry_request'] = \
            create_time_tracking_entry_request
        return self.create_time_tracking_entry_endpoint.call_with_http_info(**kwargs)

    def delete_time_tracking_entry(
        self,
        time_tracking_entry_gid,
        **kwargs
    ):
        """Delete a time tracking entry  # noqa: E501

        A specific, existing time tracking entry can be deleted by making a `DELETE` request on the URL for that time tracking entry.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_time_tracking_entry(time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        Args:
            time_tracking_entry_gid (str): Globally unique identifier for the time tracking entry.

        Keyword Args:
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
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
            DeleteAttachment200Response
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
        kwargs['time_tracking_entry_gid'] = \
            time_tracking_entry_gid
        return self.delete_time_tracking_entry_endpoint.call_with_http_info(**kwargs)

    def get_time_tracking_entries_for_task(
        self,
        task_gid,
        **kwargs
    ):
        """Get time tracking entries for a task  # noqa: E501

        Returns time tracking entries for a given task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_time_tracking_entries_for_task(task_gid, async_req=True)
        >>> result = thread.get()

        Args:
            task_gid (str): The task to operate on.

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
            GetTimeTrackingEntriesForTask200Response
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
        kwargs['task_gid'] = \
            task_gid
        return self.get_time_tracking_entries_for_task_endpoint.call_with_http_info(**kwargs)

    def get_time_tracking_entry(
        self,
        time_tracking_entry_gid,
        **kwargs
    ):
        """Get a time tracking entry  # noqa: E501

        Returns the complete time tracking entry record for a single time tracking entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_time_tracking_entry(time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        Args:
            time_tracking_entry_gid (str): Globally unique identifier for the time tracking entry.

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
            CreateTimeTrackingEntry201Response
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
        kwargs['time_tracking_entry_gid'] = \
            time_tracking_entry_gid
        return self.get_time_tracking_entry_endpoint.call_with_http_info(**kwargs)

    def update_time_tracking_entry(
        self,
        time_tracking_entry_gid,
        update_time_tracking_entry_request,
        **kwargs
    ):
        """Update a time tracking entry  # noqa: E501

        A specific, existing time tracking entry can be updated by making a `PUT` request on the URL for that time tracking entry. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated time tracking entry record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_time_tracking_entry(time_tracking_entry_gid, update_time_tracking_entry_request, async_req=True)
        >>> result = thread.get()

        Args:
            time_tracking_entry_gid (str): Globally unique identifier for the time tracking entry.
            update_time_tracking_entry_request (UpdateTimeTrackingEntryRequest): The updated fields for the time tracking entry.

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
            CreateTimeTrackingEntry201Response
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
        kwargs['time_tracking_entry_gid'] = \
            time_tracking_entry_gid
        kwargs['update_time_tracking_entry_request'] = \
            update_time_tracking_entry_request
        return self.update_time_tracking_entry_endpoint.call_with_http_info(**kwargs)

