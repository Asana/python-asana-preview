"""
    Asana

    This is the interface for interacting with the Asana platform  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
from asana_preview.model.get_events401_response import GetEvents401Response
from asana_preview.model.get_events403_response import GetEvents403Response
from asana_preview.model.get_events404_response import GetEvents404Response
from asana_preview.model.get_events500_response import GetEvents500Response
from asana_preview.model.get_task200_response import GetTask200Response
from asana_preview.model.get_tasks_for_project200_response import GetTasksForProject200Response


class TasksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_subtasks_for_task_endpoint = _Endpoint(
            settings={
                'response_type': (GetTasksForProject200Response,),
                'auth': [
                    'personal_access_token'
                ],
                'endpoint_path': '/tasks/{task_gid}/subtasks',
                'operation_id': 'get_subtasks_for_task',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_gid',
                    'opt_fields',
                    'opt_pretty',
                    'limit',
                    'offset',
                ],
                'required': [
                    'task_gid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'task_gid':
                        (str,),
                    'opt_fields':
                        ([str],),
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                },
                'attribute_map': {
                    'task_gid': 'task_gid',
                    'opt_fields': 'opt_fields',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'task_gid': 'path',
                    'opt_fields': 'query',
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
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
        self.get_task_endpoint = _Endpoint(
            settings={
                'response_type': (GetTask200Response,),
                'auth': [
                    'personal_access_token'
                ],
                'endpoint_path': '/tasks/{task_gid}',
                'operation_id': 'get_task',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_gid',
                    'opt_fields',
                    'opt_pretty',
                ],
                'required': [
                    'task_gid',
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
                    'task_gid':
                        (str,),
                    'opt_fields':
                        ([str],),
                    'opt_pretty':
                        (bool,),
                },
                'attribute_map': {
                    'task_gid': 'task_gid',
                    'opt_fields': 'opt_fields',
                    'opt_pretty': 'opt_pretty',
                },
                'location_map': {
                    'task_gid': 'path',
                    'opt_fields': 'query',
                    'opt_pretty': 'query',
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
        self.get_tasks_endpoint = _Endpoint(
            settings={
                'response_type': (GetTasksForProject200Response,),
                'auth': [
                    'personal_access_token'
                ],
                'endpoint_path': '/tasks',
                'operation_id': 'get_tasks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'opt_fields',
                    'opt_pretty',
                    'limit',
                    'offset',
                    'assignee',
                    'project',
                    'section',
                    'workspace',
                    'completed_since',
                    'modified_since',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'opt_fields':
                        ([str],),
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                    'assignee':
                        (str,),
                    'project':
                        (str,),
                    'section':
                        (str,),
                    'workspace':
                        (str,),
                    'completed_since':
                        (datetime,),
                    'modified_since':
                        (datetime,),
                },
                'attribute_map': {
                    'opt_fields': 'opt_fields',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                    'assignee': 'assignee',
                    'project': 'project',
                    'section': 'section',
                    'workspace': 'workspace',
                    'completed_since': 'completed_since',
                    'modified_since': 'modified_since',
                },
                'location_map': {
                    'opt_fields': 'query',
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'assignee': 'query',
                    'project': 'query',
                    'section': 'query',
                    'workspace': 'query',
                    'completed_since': 'query',
                    'modified_since': 'query',
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
        self.get_tasks_for_project_endpoint = _Endpoint(
            settings={
                'response_type': (GetTasksForProject200Response,),
                'auth': [
                    'personal_access_token'
                ],
                'endpoint_path': '/projects/{project_gid}/tasks',
                'operation_id': 'get_tasks_for_project',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_gid',
                    'completed_since',
                    'opt_fields',
                    'opt_pretty',
                    'limit',
                    'offset',
                ],
                'required': [
                    'project_gid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_gid':
                        (str,),
                    'completed_since':
                        (str,),
                    'opt_fields':
                        ([str],),
                    'opt_pretty':
                        (bool,),
                    'limit':
                        (int,),
                    'offset':
                        (str,),
                },
                'attribute_map': {
                    'project_gid': 'project_gid',
                    'completed_since': 'completed_since',
                    'opt_fields': 'opt_fields',
                    'opt_pretty': 'opt_pretty',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'project_gid': 'path',
                    'completed_since': 'query',
                    'opt_fields': 'query',
                    'opt_pretty': 'query',
                    'limit': 'query',
                    'offset': 'query',
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

    def get_subtasks_for_task(
        self,
        task_gid,
        **kwargs
    ):
        """Get subtasks from a task  # noqa: E501

        Returns a compact representation of all of the subtasks of a task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_subtasks_for_task(task_gid, async_req=True)
        >>> result = thread.get()

        Args:
            task_gid (str): The task to operate on.

        Keyword Args:
            opt_fields ([str]): Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options.. [optional]
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request.. [optional]
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
            GetTasksForProject200Response
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
        return self.get_subtasks_for_task_endpoint.call_with_http_info(**kwargs)

    def get_task(
        self,
        task_gid,
        **kwargs
    ):
        """Get a task  # noqa: E501

        Returns the complete task record for a single task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_task(task_gid, async_req=True)
        >>> result = thread.get()

        Args:
            task_gid (str): The task to operate on.

        Keyword Args:
            opt_fields ([str]): Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options.. [optional]
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
            GetTask200Response
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
        return self.get_task_endpoint.call_with_http_info(**kwargs)

    def get_tasks(
        self,
        **kwargs
    ):
        """Get multiple tasks  # noqa: E501

        Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/reference/searchtasksforworkspace).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tasks(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            opt_fields ([str]): Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options.. [optional]
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request.. [optional]
            assignee (str): The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified.  *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.*. [optional]
            project (str): The project to filter tasks on.. [optional]
            section (str): The section to filter tasks on.. [optional]
            workspace (str): The workspace to filter tasks on.  *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.*. [optional]
            completed_since (datetime): Only return tasks that are either incomplete or that have been completed since this time.. [optional]
            modified_since (datetime): Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.*. [optional]
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
            GetTasksForProject200Response
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
        return self.get_tasks_endpoint.call_with_http_info(**kwargs)

    def get_tasks_for_project(
        self,
        project_gid,
        **kwargs
    ):
        """Get tasks from a project  # noqa: E501

        Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tasks_for_project(project_gid, async_req=True)
        >>> result = thread.get()

        Args:
            project_gid (str): Globally unique identifier for the project.

        Keyword Args:
            completed_since (str): Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.. [optional]
            opt_fields ([str]): Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options.. [optional]
            opt_pretty (bool): Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.. [optional]
            limit (int): The number of objects to return per page. The value must be between 1 and 100.. [optional]
            offset (str): Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request.. [optional]
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
            GetTasksForProject200Response
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
        return self.get_tasks_for_project_endpoint.call_with_http_info(**kwargs)

