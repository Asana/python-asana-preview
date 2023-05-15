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
from asana_preview.model.typeahead_for_workspace200_response import TypeaheadForWorkspace200Response


class TypeaheadApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.typeahead_for_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (TypeaheadForWorkspace200Response,),
                'auth': [
                    'personalAccessToken'
                ],
                'endpoint_path': '/workspaces/{workspace_gid}/typeahead',
                'operation_id': 'typeahead_for_workspace',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_gid',
                    'resource_type',
                    'type',
                    'query',
                    'count',
                    'opt_pretty',
                    'opt_fields',
                ],
                'required': [
                    'workspace_gid',
                    'resource_type',
                ],
                'nullable': [
                ],
                'enum': [
                    'resource_type',
                    'type',
                    'opt_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('resource_type',): {

                        "CUSTOM_FIELD": "custom_field",
                        "PROJECT": "project",
                        "PROJECT_TEMPLATE": "project_template",
                        "PORTFOLIO": "portfolio",
                        "TAG": "tag",
                        "TASK": "task",
                        "USER": "user"
                    },
                    ('type',): {

                        "CUSTOM_FIELD": "custom_field",
                        "PORTFOLIO": "portfolio",
                        "PROJECT": "project",
                        "TAG": "tag",
                        "TASK": "task",
                        "USER": "user"
                    },
                    ('opt_fields',): {

                        "NAME": "name"
                    },
                },
                'openapi_types': {
                    'workspace_gid':
                        (str,),
                    'resource_type':
                        (str,),
                    'type':
                        (str,),
                    'query':
                        (str,),
                    'count':
                        (int,),
                    'opt_pretty':
                        (bool,),
                    'opt_fields':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_gid': 'workspace_gid',
                    'resource_type': 'resource_type',
                    'type': 'type',
                    'query': 'query',
                    'count': 'count',
                    'opt_pretty': 'opt_pretty',
                    'opt_fields': 'opt_fields',
                },
                'location_map': {
                    'workspace_gid': 'path',
                    'resource_type': 'query',
                    'type': 'query',
                    'query': 'query',
                    'count': 'query',
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

    def typeahead_for_workspace(
        self,
        workspace_gid,
        resource_type="user",
        **kwargs
    ):
        """Get objects via typeahead  # noqa: E501

        Retrieves objects in the workspace based via an auto-completion/typeahead search algorithm. This feature is meant to provide results quickly, so do not rely on this API to provide extremely accurate search results. The result set is limited to a single page of results with a maximum size, so you won’t be able to fetch large numbers of results.  The typeahead search API provides search for objects from a single workspace. This endpoint should be used to query for objects when creating an auto-completion/typeahead search feature. This API is meant to provide results quickly and should not be relied upon for accurate or exhaustive search results. The results sets are limited in size and cannot be paginated.  Queries return a compact representation of each object which is typically the gid and name fields. Interested in a specific set of fields or all of the fields?! Of course you are. Use field selectors to manipulate what data is included in a response.  Resources with type `user` are returned in order of most contacted to least contacted. This is determined by task assignments, adding the user to projects, and adding the user as a follower to tasks, messages, etc.  Resources with type `project` are returned in order of recency. This is determined when the user visits the project, is added to the project, and completes tasks in the project.  Resources with type `task` are returned with priority placed on tasks the user is following, but no guarantee on the order of those tasks.  Resources with type `project_template` are returned with priority placed on favorited project templates.  Leaving the `query` string empty or omitted will give you results, still following the resource ordering above. This could be used to list users or projects that are relevant for the requesting user's api token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.typeahead_for_workspace(workspace_gid, resource_type="user", async_req=True)
        >>> result = thread.get()

        Args:
            workspace_gid (str): Globally unique identifier for the workspace or organization.
            resource_type (str): The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `project`, `project_template`, `portfolio`, `tag`, `task`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported.. defaults to "user", must be one of ["user"]

        Keyword Args:
            type (str): *Deprecated: new integrations should prefer the resource_type field.*. [optional] if omitted the server will use the default value of "user"
            query (str): The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results.. [optional]
            count (int): The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned.. [optional]
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
            TypeaheadForWorkspace200Response
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
        kwargs['resource_type'] = \
            resource_type
        return self.typeahead_for_workspace_endpoint.call_with_http_info(**kwargs)

