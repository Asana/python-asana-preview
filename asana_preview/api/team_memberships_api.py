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
from asana_preview.model.get_team_membership200_response import GetTeamMembership200Response
from asana_preview.model.get_team_memberships200_response import GetTeamMemberships200Response


class TeamMembershipsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_team_membership_endpoint = _Endpoint(
            settings={
                'response_type': (GetTeamMembership200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/team_memberships/{team_membership_gid}',
                'operation_id': 'get_team_membership',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'team_membership_gid',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'team_membership_gid',
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

                        "IS_ADMIN": "is_admin",
                        "IS_GUEST": "is_guest",
                        "TEAM": "team",
                        "IS_LIMITED_ACCESS": "is_limited_access",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'team_membership_gid':
                        (str,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'team_membership_gid': 'team_membership_gid',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'team_membership_gid': 'path',
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
        self.get_team_memberships_endpoint = _Endpoint(
            settings={
                'response_type': (GetTeamMemberships200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/team_memberships',
                'operation_id': 'get_team_memberships',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'opt_pretty',
                    'limit',
                    'offset',
                    'team',
                    'user',
                    'workspace',
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

                        "IS_ADMIN": "is_admin",
                        "IS_GUEST": "is_guest",
                        "TEAM": "team",
                        "IS_LIMITED_ACCESS": "is_limited_access",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                    'team':
                        (str,),
                    'user':
                        (str,),
                    'workspace':
                        (str,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'team': 'team',
                    'user': 'user',
                    'workspace': 'workspace',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'team': 'query',
                    'user': 'query',
                    'workspace': 'query',
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
        self.get_team_memberships_for_team_endpoint = _Endpoint(
            settings={
                'response_type': (GetTeamMemberships200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/teams/{team_gid}/team_memberships',
                'operation_id': 'get_team_memberships_for_team',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'team_gid',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'opt_fields',
                ],
                'required': [
                    'team_gid',
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

                        "IS_ADMIN": "is_admin",
                        "IS_GUEST": "is_guest",
                        "TEAM": "team",
                        "IS_LIMITED_ACCESS": "is_limited_access",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'team_gid':
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
                    'team_gid': 'team_gid',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'team_gid': 'path',
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
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_team_memberships_for_user_endpoint = _Endpoint(
            settings={
                'response_type': (GetTeamMemberships200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/users/{user_gid}/team_memberships',
                'operation_id': 'get_team_memberships_for_user',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_gid',
                    'workspace',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'opt_fields',
                ],
                'required': [
                    'user_gid',
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

                        "IS_ADMIN": "is_admin",
                        "IS_GUEST": "is_guest",
                        "TEAM": "team",
                        "IS_LIMITED_ACCESS": "is_limited_access",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'user_gid':
                        (str,),
                    'workspace':
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
                    'user_gid': 'user_gid',
                    'workspace': 'workspace',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'user_gid': 'path',
                    'workspace': 'query',
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
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_team_membership(
        self,
        team_membership_gid,
        **kwargs
    ):
        """Get a team membership  # noqa: E501

        Returns the complete team membership record for a single team membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_membership(team_membership_gid, async_req=True)
        >>> result = thread.get()

        Args:
            team_membership_gid (str):

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
            GetTeamMembership200Response
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
        kwargs['team_membership_gid'] = \
            team_membership_gid
        return self.get_team_membership_endpoint.call_with_http_info(**kwargs)

    def get_team_memberships(
        self,
        **kwargs
    ):
        """Get team memberships  # noqa: E501

        Returns compact team membership records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_memberships(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): Results per page. The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'. [optional]
            team (str): Globally unique identifier for the team.. [optional]
            user (str): A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. This parameter must be used with the workspace parameter.. [optional]
            workspace (str): Globally unique identifier for the workspace. This parameter must be used with the user parameter.. [optional]
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
            GetTeamMemberships200Response
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
        return self.get_team_memberships_endpoint.call_with_http_info(**kwargs)

    def get_team_memberships_for_team(
        self,
        team_gid,
        **kwargs
    ):
        """Get memberships from a team  # noqa: E501

        Returns the compact team memberships for the team.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_memberships_for_team(team_gid, async_req=True)
        >>> result = thread.get()

        Args:
            team_gid (str): Globally unique identifier for the team.

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
            GetTeamMemberships200Response
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
        kwargs['team_gid'] = \
            team_gid
        return self.get_team_memberships_for_team_endpoint.call_with_http_info(**kwargs)

    def get_team_memberships_for_user(
        self,
        user_gid,
        workspace,
        **kwargs
    ):
        """Get memberships from a user  # noqa: E501

        Returns the compact team membership records for the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_memberships_for_user(user_gid, workspace, async_req=True)
        >>> result = thread.get()

        Args:
            user_gid (str): A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
            workspace (str): Globally unique identifier for the workspace.

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
            GetTeamMemberships200Response
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
        kwargs['user_gid'] = \
            user_gid
        kwargs['workspace'] = \
            workspace
        return self.get_team_memberships_for_user_endpoint.call_with_http_info(**kwargs)

