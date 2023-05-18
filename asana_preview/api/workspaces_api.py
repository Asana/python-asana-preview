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
from asana_preview.model.add_user_for_workspace200_response import AddUserForWorkspace200Response
from asana_preview.model.add_user_for_workspace_request import AddUserForWorkspaceRequest
from asana_preview.model.delete_attachment200_response import DeleteAttachment200Response
from asana_preview.model.error_response import ErrorResponse
from asana_preview.model.get_workspace200_response import GetWorkspace200Response
from asana_preview.model.get_workspaces200_response import GetWorkspaces200Response
from asana_preview.model.remove_user_for_workspace_request import RemoveUserForWorkspaceRequest
from asana_preview.model.update_workspace_request import UpdateWorkspaceRequest


class WorkspacesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_user_for_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (AddUserForWorkspace200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/workspaces/{workspace_gid}/addUser',
                'operation_id': 'add_user_for_workspace',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_gid',
                    'add_user_for_workspace_request',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'workspace_gid',
                    'add_user_for_workspace_request',
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

                        "PHOTO": "photo",
                        "NAME": "name",
                        "EMAIL": "email"
                    },
                },
                'openapi_types': {
                    'workspace_gid':
                        (str,),
                    'add_user_for_workspace_request':
                        (AddUserForWorkspaceRequest,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_gid': 'workspace_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'workspace_gid': 'path',
                    'add_user_for_workspace_request': 'body',
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
        self.get_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (GetWorkspace200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/workspaces/{workspace_gid}',
                'operation_id': 'get_workspace',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_gid',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'workspace_gid',
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

                        "NAME": "name",
                        "IS_ORGANIZATION": "is_organization",
                        "EMAIL_DOMAINS": "email_domains"
                    },
                },
                'openapi_types': {
                    'workspace_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_gid': 'workspace_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'workspace_gid': 'path',
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
        self.get_workspaces_endpoint = _Endpoint(
            settings={
                'response_type': (GetWorkspaces200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/workspaces',
                'operation_id': 'get_workspaces',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'opt_pretty',
                    'limit',
                    'offset',
                    'opt_fields',
                ],
                'required': [],
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

                        "NAME": "name",
                        "IS_ORGANIZATION": "is_organization",
                        "EMAIL_DOMAINS": "email_domains"
                    },
                },
                'openapi_types': {
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
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
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
        self.remove_user_for_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteAttachment200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/workspaces/{workspace_gid}/removeUser',
                'operation_id': 'remove_user_for_workspace',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_gid',
                    'remove_user_for_workspace_request',
                    'opt_pretty',
                ],
                'required': [
                    'workspace_gid',
                    'remove_user_for_workspace_request',
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
                    'workspace_gid':
                        (str,),
                    'remove_user_for_workspace_request':
                        (RemoveUserForWorkspaceRequest,),
                    'opt_pretty':
                        (bool,),
                },
                'attribute_map': {
                    'workspace_gid': 'workspace_gid',
                    'opt_pretty': 'opt_pretty',
                },
                'location_map': {
                    'workspace_gid': 'path',
                    'remove_user_for_workspace_request': 'body',
                    'opt_pretty': 'query',
                },
                'collection_format_map': {
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
        self.update_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (GetWorkspace200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/workspaces/{workspace_gid}',
                'operation_id': 'update_workspace',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_gid',
                    'update_workspace_request',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'workspace_gid',
                    'update_workspace_request',
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

                        "NAME": "name",
                        "IS_ORGANIZATION": "is_organization",
                        "EMAIL_DOMAINS": "email_domains"
                    },
                },
                'openapi_types': {
                    'workspace_gid':
                        (str,),
                    'update_workspace_request':
                        (UpdateWorkspaceRequest,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_gid': 'workspace_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'workspace_gid': 'path',
                    'update_workspace_request': 'body',
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

    def add_user_for_workspace(
        self,
        workspace_gid,
        add_user_for_workspace_request,
        **kwargs
    ):
        """Add a user to a workspace or organization  # noqa: E501

        Add a user to a workspace or organization. The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_user_for_workspace(workspace_gid, add_user_for_workspace_request, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_gid (str): Globally unique identifier for the workspace or organization.
            add_user_for_workspace_request (AddUserForWorkspaceRequest): The user to add to the workspace.

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
            AddUserForWorkspace200Response
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
        kwargs['workspace_gid'] = \
            workspace_gid
        kwargs['add_user_for_workspace_request'] = \
            add_user_for_workspace_request
        return self.add_user_for_workspace_endpoint.call_with_http_info(**kwargs)

    def get_workspace(
        self,
        workspace_gid,
        **kwargs
    ):
        """Get a workspace  # noqa: E501

        Returns the full workspace record for a single workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_workspace(workspace_gid, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_gid (str): Globally unique identifier for the workspace or organization.

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
            GetWorkspace200Response
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
        kwargs['workspace_gid'] = \
            workspace_gid
        return self.get_workspace_endpoint.call_with_http_info(**kwargs)

    def get_workspaces(
        self,
        **kwargs
    ):
        """Get multiple workspaces  # noqa: E501

        Returns the compact records for all workspaces visible to the authorized user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_workspaces(async_req=True)
        >>> result = thread.get()


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
            GetWorkspaces200Response
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
        return self.get_workspaces_endpoint.call_with_http_info(**kwargs)

    def remove_user_for_workspace(
        self,
        workspace_gid,
        remove_user_for_workspace_request,
        **kwargs
    ):
        """Remove a user from a workspace or organization  # noqa: E501

        Remove a user from a workspace or organization. The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address. Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_user_for_workspace(workspace_gid, remove_user_for_workspace_request, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_gid (str): Globally unique identifier for the workspace or organization.
            remove_user_for_workspace_request (RemoveUserForWorkspaceRequest): The user to remove from the workspace.

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
        kwargs['workspace_gid'] = \
            workspace_gid
        kwargs['remove_user_for_workspace_request'] = \
            remove_user_for_workspace_request
        return self.remove_user_for_workspace_endpoint.call_with_http_info(**kwargs)

    def update_workspace(
        self,
        workspace_gid,
        update_workspace_request,
        **kwargs
    ):
        """Update a workspace  # noqa: E501

        A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged. Currently the only field that can be modified for a workspace is its name. Returns the complete, updated workspace record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_workspace(workspace_gid, update_workspace_request, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_gid (str): Globally unique identifier for the workspace or organization.
            update_workspace_request (UpdateWorkspaceRequest): The workspace object with all updated properties.

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
            GetWorkspace200Response
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
        kwargs['workspace_gid'] = \
            workspace_gid
        kwargs['update_workspace_request'] = \
            update_workspace_request
        return self.update_workspace_endpoint.call_with_http_info(**kwargs)
