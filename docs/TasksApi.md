# asana_preview.TasksApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subtasks_for_task**](TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
[**get_tasks_for_project**](TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project


# **get_subtasks_for_task**
> GetTasksForProject200Response get_subtasks_for_task(task_gid)

Get subtasks from a task

Returns a compact representation of all of the subtasks of a task.

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get subtasks from a task
        api_response = api_instance.get_subtasks_for_task(task_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_subtasks_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get subtasks from a task
        api_response = api_instance.get_subtasks_for_task(task_gid, opt_fields=opt_fields, opt_pretty=opt_pretty, limit=limit, offset=offset)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_subtasks_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request. | [optional]

### Return type

[**GetTasksForProject200Response**](GetTasksForProject200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task&#39;s subtasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> GetTask200Response get_task(task_gid)

Get a task

Returns the complete task record for a single task.

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get a task
        api_response = api_instance.get_task(task_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a task
        api_response = api_instance.get_task(task_gid, opt_fields=opt_fields, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**GetTask200Response**](GetTask200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> GetTasksForProject200Response get_tasks()

Get multiple tasks

Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/reference/searchtasksforworkspace).

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request. (optional)
    assignee = "14641" # str | The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified.  *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.* (optional)
    project = "321654" # str | The project to filter tasks on. (optional)
    section = "321654" # str | The section to filter tasks on. (optional)
    workspace = "321654" # str | The workspace to filter tasks on.  *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.* (optional)
    completed_since = dateutil_parser('2012-02-22T02:06:58.158Z') # datetime | Only return tasks that are either incomplete or that have been completed since this time. (optional)
    modified_since = dateutil_parser('2012-02-22T02:06:58.158Z') # datetime | Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* (optional)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get multiple tasks
        api_response = api_instance.get_tasks(opt_fields=opt_fields, opt_pretty=opt_pretty, limit=limit, offset=offset, assignee=assignee, project=project, section=section, workspace=workspace, completed_since=completed_since, modified_since=modified_since)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request. | [optional]
 **assignee** | **str**| The assignee to filter tasks on. If searching for unassigned tasks, assignee.any &#x3D; null can be specified.  *Note: If you specify &#x60;assignee&#x60;, you must also specify the &#x60;workspace&#x60; to filter on.* | [optional]
 **project** | **str**| The project to filter tasks on. | [optional]
 **section** | **str**| The section to filter tasks on. | [optional]
 **workspace** | **str**| The workspace to filter tasks on.  *Note: If you specify &#x60;workspace&#x60;, you must also specify the &#x60;assignee&#x60; to filter on.* | [optional]
 **completed_since** | **datetime**| Only return tasks that are either incomplete or that have been completed since this time. | [optional]
 **modified_since** | **datetime**| Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* | [optional]

### Return type

[**GetTasksForProject200Response**](GetTasksForProject200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved requested tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_project**
> GetTasksForProject200Response get_tasks_for_project(project_gid)

Get tasks from a project

Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    project_gid = "1331" # str | Globally unique identifier for the project.
    completed_since = "2012-02-22T02:06:58.158Z" # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. (optional)
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get tasks from a project
        api_response = api_instance.get_tasks_for_project(project_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_project: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tasks from a project
        api_response = api_instance.get_tasks_for_project(project_gid, completed_since=completed_since, opt_fields=opt_fields, opt_pretty=opt_pretty, limit=limit, offset=offset)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. |
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. | [optional]
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request. | [optional]

### Return type

[**GetTasksForProject200Response**](GetTasksForProject200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

