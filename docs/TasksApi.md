# asana_preview.TasksApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dependencies_for_task**](TasksApi.md#add_dependencies_for_task) | **POST** /tasks/{task_gid}/addDependencies | Set dependencies for a task
[**add_dependents_for_task**](TasksApi.md#add_dependents_for_task) | **POST** /tasks/{task_gid}/addDependents | Set dependents for a task
[**add_project_for_task**](TasksApi.md#add_project_for_task) | **POST** /tasks/{task_gid}/addProject | Add a project to a task
[**add_tag_for_task**](TasksApi.md#add_tag_for_task) | **POST** /tasks/{task_gid}/addTag | Add a tag to a task
[**create_subtask_for_task**](TasksApi.md#create_subtask_for_task) | **POST** /tasks/{task_gid}/subtasks | Create a subtask
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Create a task
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{task_gid} | Delete a task
[**duplicate_task**](TasksApi.md#duplicate_task) | **POST** /tasks/{task_gid}/duplicate | Duplicate a task
[**get_dependencies_for_task**](TasksApi.md#get_dependencies_for_task) | **GET** /tasks/{task_gid}/dependencies | Get dependencies from a task
[**get_dependents_for_task**](TasksApi.md#get_dependents_for_task) | **GET** /tasks/{task_gid}/dependents | Get dependents from a task
[**get_subtasks_for_task**](TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
[**get_tasks_for_project**](TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
[**get_tasks_for_section**](TasksApi.md#get_tasks_for_section) | **GET** /sections/{section_gid}/tasks | Get tasks from a section
[**get_tasks_for_tag**](TasksApi.md#get_tasks_for_tag) | **GET** /tags/{tag_gid}/tasks | Get tasks from a tag
[**get_tasks_for_user_task_list**](TasksApi.md#get_tasks_for_user_task_list) | **GET** /user_task_lists/{user_task_list_gid}/tasks | Get tasks from a user task list
[**remove_dependencies_for_task**](TasksApi.md#remove_dependencies_for_task) | **POST** /tasks/{task_gid}/removeDependencies | Unlink dependencies from a task
[**remove_dependents_for_task**](TasksApi.md#remove_dependents_for_task) | **POST** /tasks/{task_gid}/removeDependents | Unlink dependents from a task
[**remove_follower_for_task**](TasksApi.md#remove_follower_for_task) | **POST** /tasks/{task_gid}/removeFollowers | Remove followers from a task
[**remove_project_for_task**](TasksApi.md#remove_project_for_task) | **POST** /tasks/{task_gid}/removeProject | Remove a project from a task
[**remove_tag_for_task**](TasksApi.md#remove_tag_for_task) | **POST** /tasks/{task_gid}/removeTag | Remove a tag from a task
[**search_tasks_for_workspace**](TasksApi.md#search_tasks_for_workspace) | **GET** /workspaces/{workspace_gid}/tasks/search | Search tasks in a workspace
[**set_parent_for_task**](TasksApi.md#set_parent_for_task) | **POST** /tasks/{task_gid}/setParent | Set the parent of a task
[**update_task**](TasksApi.md#update_task) | **PUT** /tasks/{task_gid} | Update a task


# **add_dependencies_for_task**
> DeleteAttachment200Response add_dependencies_for_task(task_gid, add_dependencies_for_task_request)

Set dependencies for a task

Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    add_dependencies_for_task_request = AddDependenciesForTaskRequest(
        data=ModifyDependenciesRequest(
            dependencies=[
                "dependencies_example",
            ],
        ),
    ) # AddDependenciesForTaskRequest | The list of tasks to set as dependencies.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Set dependencies for a task
        api_response = api_instance.add_dependencies_for_task(task_gid, add_dependencies_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_dependencies_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set dependencies for a task
        api_response = api_instance.add_dependencies_for_task(task_gid, add_dependencies_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_dependencies_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **add_dependencies_for_task_request** | [**AddDependenciesForTaskRequest**](AddDependenciesForTaskRequest.md)| The list of tasks to set as dependencies. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set the specified dependencies on the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dependents_for_task**
> DeleteAttachment200Response add_dependents_for_task(task_gid, add_dependents_for_task_request)

Set dependents for a task

Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    add_dependents_for_task_request = AddDependentsForTaskRequest(
        data=ModifyDependentsRequest(
            dependents=[
                "dependents_example",
            ],
        ),
    ) # AddDependentsForTaskRequest | The list of tasks to add as dependents.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Set dependents for a task
        api_response = api_instance.add_dependents_for_task(task_gid, add_dependents_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_dependents_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set dependents for a task
        api_response = api_instance.add_dependents_for_task(task_gid, add_dependents_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_dependents_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **add_dependents_for_task_request** | [**AddDependentsForTaskRequest**](AddDependentsForTaskRequest.md)| The list of tasks to add as dependents. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set the specified dependents on the given task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_for_task**
> DeleteAttachment200Response add_project_for_task(task_gid, add_project_for_task_request)

Add a project to a task

Adds the task to the specified project, in the optional location specified. If no location arguments are given, the task will be added to the end of the project.  `addProject` can also be used to reorder a task within a project or section that already contains it.  At most one of `insert_before`, `insert_after`, or `section` should be specified. Inserting into a section in an non-order-dependent way can be done by specifying section, otherwise, to insert within a section in a particular place, specify `insert_before` or `insert_after` and a task within the section to anchor the position of this task.  Returns an empty data block.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    add_project_for_task_request = AddProjectForTaskRequest(
        data=TaskAddProjectRequest(
            project="13579",
            insert_after="124816",
            insert_before="432134",
            section="987654",
        ),
    ) # AddProjectForTaskRequest | The project to add the task to.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Add a project to a task
        api_response = api_instance.add_project_for_task(task_gid, add_project_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_project_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a project to a task
        api_response = api_instance.add_project_for_task(task_gid, add_project_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_project_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **add_project_for_task_request** | [**AddProjectForTaskRequest**](AddProjectForTaskRequest.md)| The project to add the task to. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the specified project to the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_for_task**
> DeleteAttachment200Response add_tag_for_task(task_gid, add_tag_for_task_request)

Add a tag to a task

Adds a tag to a task. Returns an empty data block.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    add_tag_for_task_request = AddTagForTaskRequest(
        data=TaskAddTagRequest(
            tag="13579",
        ),
    ) # AddTagForTaskRequest | The tag to add to the task.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Add a tag to a task
        api_response = api_instance.add_tag_for_task(task_gid, add_tag_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_tag_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a tag to a task
        api_response = api_instance.add_tag_for_task(task_gid, add_tag_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->add_tag_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **add_tag_for_task_request** | [**AddTagForTaskRequest**](AddTagForTaskRequest.md)| The tag to add to the task. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the specified tag to the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subtask_for_task**
> CreateTask201Response create_subtask_for_task(task_gid, create_task_request)

Create a subtask

Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    create_task_request = CreateTaskRequest(
        data=TaskRequest(None),
    ) # CreateTaskRequest | The new subtask to create.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","due_on","name","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Create a subtask
        api_response = api_instance.create_subtask_for_task(task_gid, create_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->create_subtask_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a subtask
        api_response = api_instance.create_subtask_for_task(task_gid, create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->create_subtask_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| The new subtask to create. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the specified subtask. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> CreateTask201Response create_task(create_task_request)

Create a task

Creating a new task is as easy as POSTing to the `/tasks` endpoint with a data block containing the fields you’d like to set on the task. Any unspecified fields will take on default values.  Every task is required to be created in a specific workspace, and this workspace cannot be changed once set. The workspace need not be set explicitly if you specify `projects` or a `parent` task instead.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    create_task_request = CreateTaskRequest(
        data=TaskRequest(None),
    ) # CreateTaskRequest | The task to create.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","due_on","name","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Create a task
        api_response = api_instance.create_task(create_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a task
        api_response = api_instance.create_task(create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| The task to create. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> DeleteAttachment200Response delete_task(task_gid)

Delete a task

A specific, existing task can be deleted by making a DELETE request on the URL for that task. Deleted tasks go into the “trash” of the user making the delete request. Tasks can be recovered from the trash within a period of 30 days; afterward they are completely removed from the system.  Returns an empty data record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Delete a task
        api_response = api_instance.delete_task(task_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->delete_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a task
        api_response = api_instance.delete_task(task_gid, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_task**
> GetJob200Response duplicate_task(task_gid, duplicate_task_request)

Duplicate a task

Creates and returns a job that will asynchronously handle the duplication.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    duplicate_task_request = DuplicateTaskRequest(
        data=TaskDuplicateRequest(
            name="New Task Name",
            include="["notes","assignee"]",
        ),
    ) # DuplicateTaskRequest | Describes the duplicate's name and the fields that will be duplicated.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["status","resource_subtype","new_project_template","new_task","new_task_template","new_project"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Duplicate a task
        api_response = api_instance.duplicate_task(task_gid, duplicate_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->duplicate_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Duplicate a task
        api_response = api_instance.duplicate_task(task_gid, duplicate_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->duplicate_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **duplicate_task_request** | [**DuplicateTaskRequest**](DuplicateTaskRequest.md)| Describes the duplicate&#39;s name and the fields that will be duplicated. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetJob200Response**](GetJob200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the job to handle duplication. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependencies_for_task**
> GetTasks200Response get_dependencies_for_task(task_gid)

Get dependencies from a task

Returns the compact representations of all of the dependencies of a task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get dependencies from a task
        api_response = api_instance.get_dependencies_for_task(task_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_dependencies_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get dependencies from a task
        api_response = api_instance.get_dependencies_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_dependencies_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task&#39;s dependencies. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependents_for_task**
> GetTasks200Response get_dependents_for_task(task_gid)

Get dependents from a task

Returns the compact representations of all of the dependents of a task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get dependents from a task
        api_response = api_instance.get_dependents_for_task(task_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_dependents_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get dependents from a task
        api_response = api_instance.get_dependents_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_dependents_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified dependents of the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtasks_for_task**
> GetTasks200Response get_subtasks_for_task(task_gid)

Get subtasks from a task

Returns a compact representation of all of the subtasks of a task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

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
        api_response = api_instance.get_subtasks_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_subtasks_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

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
> CreateTask201Response get_task(task_gid)

Get a task

Returns the complete task record for a single task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","due_on","name","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

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
        api_response = api_instance.get_task(task_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

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
> GetTasks200Response get_tasks()

Get multiple tasks

Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/reference/searchtasksforworkspace).

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    assignee = "14641" # str | The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified. *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.* (optional)
    project = "321654" # str | The project to filter tasks on. (optional)
    section = "321654" # str | The section to filter tasks on. (optional)
    workspace = "321654" # str | The workspace to filter tasks on. *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.* (optional)
    completed_since = dateutil_parser('2012-02-22T02:06:58.158Z') # datetime | Only return tasks that are either incomplete or that have been completed since this time. (optional)
    modified_since = dateutil_parser('2012-02-22T02:06:58.158Z') # datetime | Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get multiple tasks
        api_response = api_instance.get_tasks(opt_pretty=opt_pretty, limit=limit, offset=offset, assignee=assignee, project=project, section=section, workspace=workspace, completed_since=completed_since, modified_since=modified_since, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **assignee** | **str**| The assignee to filter tasks on. If searching for unassigned tasks, assignee.any &#x3D; null can be specified. *Note: If you specify &#x60;assignee&#x60;, you must also specify the &#x60;workspace&#x60; to filter on.* | [optional]
 **project** | **str**| The project to filter tasks on. | [optional]
 **section** | **str**| The section to filter tasks on. | [optional]
 **workspace** | **str**| The workspace to filter tasks on. *Note: If you specify &#x60;workspace&#x60;, you must also specify the &#x60;assignee&#x60; to filter on.* | [optional]
 **completed_since** | **datetime**| Only return tasks that are either incomplete or that have been completed since this time. | [optional]
 **modified_since** | **datetime**| Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

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
> GetTasks200Response get_tasks_for_project(project_gid)

Get tasks from a project

Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    project_gid = "1331" # str | Globally unique identifier for the project.
    completed_since = "2012-02-22T02:06:58.158Z" # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

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
        api_response = api_instance.get_tasks_for_project(project_gid, completed_since=completed_since, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. |
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

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

# **get_tasks_for_section**
> GetTasks200Response get_tasks_for_section(section_gid)

Get tasks from a section

*Board view only*: Returns the compact section records for all tasks within the given section.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    section_gid = "321654" # str | The globally unique identifier for the section.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get tasks from a section
        api_response = api_instance.get_tasks_for_section(section_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_section: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tasks from a section
        api_response = api_instance.get_tasks_for_section(section_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the section&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_tag**
> GetTasks200Response get_tasks_for_tag(tag_gid)

Get tasks from a tag

Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    tag_gid = "11235" # str | Globally unique identifier for the tag.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get tasks from a tag
        api_response = api_instance.get_tasks_for_tag(tag_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_tag: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tasks from a tag
        api_response = api_instance.get_tasks_for_tag(tag_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_gid** | **str**| Globally unique identifier for the tag. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the tasks associated with the specified tag. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_user_task_list**
> GetTasks200Response get_tasks_for_user_task_list(user_task_list_gid)

Get tasks from a user task list

Returns the compact list of tasks in a user’s My Tasks list. *Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.* *Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    user_task_list_gid = "12345" # str | Globally unique identifier for the user task list.
    completed_since = "2012-02-22T02:06:58.158Z" # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get tasks from a user task list
        api_response = api_instance.get_tasks_for_user_task_list(user_task_list_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_user_task_list: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tasks from a user task list
        api_response = api_instance.get_tasks_for_user_task_list(user_task_list_gid, completed_since=completed_since, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->get_tasks_for_user_task_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_task_list_gid** | **str**| Globally unique identifier for the user task list. |
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the user task list&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dependencies_for_task**
> DeleteAttachment200Response remove_dependencies_for_task(task_gid, add_dependencies_for_task_request)

Unlink dependencies from a task

Unlinks a set of dependencies from this task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    add_dependencies_for_task_request = AddDependenciesForTaskRequest(
        data=ModifyDependenciesRequest(
            dependencies=[
                "dependencies_example",
            ],
        ),
    ) # AddDependenciesForTaskRequest | The list of tasks to unlink as dependencies.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Unlink dependencies from a task
        api_response = api_instance.remove_dependencies_for_task(task_gid, add_dependencies_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_dependencies_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unlink dependencies from a task
        api_response = api_instance.remove_dependencies_for_task(task_gid, add_dependencies_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_dependencies_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **add_dependencies_for_task_request** | [**AddDependenciesForTaskRequest**](AddDependenciesForTaskRequest.md)| The list of tasks to unlink as dependencies. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully unlinked the dependencies from the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dependents_for_task**
> DeleteAttachment200Response remove_dependents_for_task(task_gid, add_dependents_for_task_request)

Unlink dependents from a task

Unlinks a set of dependents from this task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    add_dependents_for_task_request = AddDependentsForTaskRequest(
        data=ModifyDependentsRequest(
            dependents=[
                "dependents_example",
            ],
        ),
    ) # AddDependentsForTaskRequest | The list of tasks to remove as dependents.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Unlink dependents from a task
        api_response = api_instance.remove_dependents_for_task(task_gid, add_dependents_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_dependents_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unlink dependents from a task
        api_response = api_instance.remove_dependents_for_task(task_gid, add_dependents_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_dependents_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **add_dependents_for_task_request** | [**AddDependentsForTaskRequest**](AddDependentsForTaskRequest.md)| The list of tasks to remove as dependents. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully unlinked the specified tasks as dependents. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_follower_for_task**
> CreateTask201Response remove_follower_for_task(task_gid, remove_follower_for_task_request)

Remove followers from a task

Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    remove_follower_for_task_request = RemoveFollowerForTaskRequest(
        data=TaskRemoveFollowersRequest(
            followers=["13579","321654"],
        ),
    ) # RemoveFollowerForTaskRequest | The followers to remove from the task.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","due_on","name","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Remove followers from a task
        api_response = api_instance.remove_follower_for_task(task_gid, remove_follower_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_follower_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove followers from a task
        api_response = api_instance.remove_follower_for_task(task_gid, remove_follower_for_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_follower_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **remove_follower_for_task_request** | [**RemoveFollowerForTaskRequest**](RemoveFollowerForTaskRequest.md)| The followers to remove from the task. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the specified followers from the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_for_task**
> DeleteAttachment200Response remove_project_for_task(task_gid, remove_project_for_task_request)

Remove a project from a task

Removes the task from the specified project. The task will still exist in the system, but it will not be in the project anymore.  Returns an empty data block.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    remove_project_for_task_request = RemoveProjectForTaskRequest(
        data=TaskRemoveProjectRequest(
            project="13579",
        ),
    ) # RemoveProjectForTaskRequest | The project to remove the task from.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Remove a project from a task
        api_response = api_instance.remove_project_for_task(task_gid, remove_project_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_project_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a project from a task
        api_response = api_instance.remove_project_for_task(task_gid, remove_project_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_project_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **remove_project_for_task_request** | [**RemoveProjectForTaskRequest**](RemoveProjectForTaskRequest.md)| The project to remove the task from. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the specified project from the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag_for_task**
> DeleteAttachment200Response remove_tag_for_task(task_gid, remove_tag_for_task_request)

Remove a tag from a task

Removes a tag from a task. Returns an empty data block.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    remove_tag_for_task_request = RemoveTagForTaskRequest(
        data=TaskRemoveTagRequest(
            tag="13579",
        ),
    ) # RemoveTagForTaskRequest | The tag to remove from the task.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Remove a tag from a task
        api_response = api_instance.remove_tag_for_task(task_gid, remove_tag_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_tag_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a tag from a task
        api_response = api_instance.remove_tag_for_task(task_gid, remove_tag_for_task_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->remove_tag_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **remove_tag_for_task_request** | [**RemoveTagForTaskRequest**](RemoveTagForTaskRequest.md)| The tag to remove from the task. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the specified tag from the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tasks_for_workspace**
> GetTasks200Response search_tasks_for_workspace(workspace_gid)

Search tasks in a workspace

To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need. #### Premium access Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:  - The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace  Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter. #### Eventual consistency Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product. #### Rate limits You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits). #### Custom field parameters | Parameter name | Custom field type | Accepted type | |---|---|---| | custom_fields.{gid}.is_set | All | Boolean | | custom_fields.{gid}.value | Text | String | | custom_fields.{gid}.value | Number | Number | | custom_fields.{gid}.value | Enum | Enum option ID | | custom_fields.{gid}.starts_with | Text only | String | | custom_fields.{gid}.ends_with | Text only | String | | custom_fields.{gid}.contains | Text only | String | | custom_fields.{gid}.less_than | Number only | Number | | custom_fields.{gid}.greater_than | Number only | Number |   For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.  **Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field  *Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    text = "Bug" # str | Performs full-text search on both task name and description (optional)
    resource_subtype = "milestone" # str | Filters results by the task's resource_subtype (optional) if omitted the server will use the default value of "milestone"
    assignee_any = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    assignee_not = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    portfolios_any = "12345,23456,34567" # str | Comma-separated list of portfolio IDs (optional)
    projects_any = "12345,23456,34567" # str | Comma-separated list of project IDs (optional)
    projects_not = "12345,23456,34567" # str | Comma-separated list of project IDs (optional)
    projects_all = "12345,23456,34567" # str | Comma-separated list of project IDs (optional)
    sections_any = "12345,23456,34567" # str | Comma-separated list of section or column IDs (optional)
    sections_not = "12345,23456,34567" # str | Comma-separated list of section or column IDs (optional)
    sections_all = "12345,23456,34567" # str | Comma-separated list of section or column IDs (optional)
    tags_any = "12345,23456,34567" # str | Comma-separated list of tag IDs (optional)
    tags_not = "12345,23456,34567" # str | Comma-separated list of tag IDs (optional)
    tags_all = "12345,23456,34567" # str | Comma-separated list of tag IDs (optional)
    teams_any = "12345,23456,34567" # str | Comma-separated list of team IDs (optional)
    followers_not = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    created_by_any = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    created_by_not = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    assigned_by_any = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    assigned_by_not = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    liked_by_not = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    commented_on_by_not = "12345,23456,34567" # str | Comma-separated list of user identifiers (optional)
    due_on_before = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    due_on_after = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    due_on = dateutil_parser('2019-09-15').date() # date, none_type | ISO 8601 date string or `null` (optional)
    due_at_before = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    due_at_after = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    start_on_before = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    start_on_after = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    start_on = dateutil_parser('2019-09-15').date() # date, none_type | ISO 8601 date string or `null` (optional)
    created_on_before = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    created_on_after = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    created_on = dateutil_parser('2019-09-15').date() # date, none_type | ISO 8601 date string or `null` (optional)
    created_at_before = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    created_at_after = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    completed_on_before = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    completed_on_after = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    completed_on = dateutil_parser('2019-09-15').date() # date, none_type | ISO 8601 date string or `null` (optional)
    completed_at_before = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    completed_at_after = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    modified_on_before = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    modified_on_after = dateutil_parser('2019-09-15').date() # date | ISO 8601 date string (optional)
    modified_on = dateutil_parser('2019-09-15').date() # date, none_type | ISO 8601 date string or `null` (optional)
    modified_at_before = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    modified_at_after = dateutil_parser('2019-04-15T01:01:46.055Z') # datetime | ISO 8601 datetime string (optional)
    is_blocking = False # bool | Filter to incomplete tasks with dependents (optional)
    is_blocked = False # bool | Filter to tasks with incomplete dependencies (optional)
    has_attachment = False # bool | Filter to tasks with attachments (optional)
    completed = False # bool | Filter to completed tasks (optional)
    is_subtask = False # bool | Filter to subtasks (optional)
    sort_by = "likes" # str | One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at` (optional) if omitted the server will use the default value of "modified_at"
    sort_ascending = True # bool | Default `false` (optional) if omitted the server will use the default value of False
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","name","due_on","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Search tasks in a workspace
        api_response = api_instance.search_tasks_for_workspace(workspace_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->search_tasks_for_workspace: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search tasks in a workspace
        api_response = api_instance.search_tasks_for_workspace(workspace_gid, opt_pretty=opt_pretty, text=text, resource_subtype=resource_subtype, assignee_any=assignee_any, assignee_not=assignee_not, portfolios_any=portfolios_any, projects_any=projects_any, projects_not=projects_not, projects_all=projects_all, sections_any=sections_any, sections_not=sections_not, sections_all=sections_all, tags_any=tags_any, tags_not=tags_not, tags_all=tags_all, teams_any=teams_any, followers_not=followers_not, created_by_any=created_by_any, created_by_not=created_by_not, assigned_by_any=assigned_by_any, assigned_by_not=assigned_by_not, liked_by_not=liked_by_not, commented_on_by_not=commented_on_by_not, due_on_before=due_on_before, due_on_after=due_on_after, due_on=due_on, due_at_before=due_at_before, due_at_after=due_at_after, start_on_before=start_on_before, start_on_after=start_on_after, start_on=start_on, created_on_before=created_on_before, created_on_after=created_on_after, created_on=created_on, created_at_before=created_at_before, created_at_after=created_at_after, completed_on_before=completed_on_before, completed_on_after=completed_on_after, completed_on=completed_on, completed_at_before=completed_at_before, completed_at_after=completed_at_after, modified_on_before=modified_on_before, modified_on_after=modified_on_after, modified_on=modified_on, modified_at_before=modified_at_before, modified_at_after=modified_at_after, is_blocking=is_blocking, is_blocked=is_blocked, has_attachment=has_attachment, completed=completed, is_subtask=is_subtask, sort_by=sort_by, sort_ascending=sort_ascending, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->search_tasks_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **text** | **str**| Performs full-text search on both task name and description | [optional]
 **resource_subtype** | **str**| Filters results by the task&#39;s resource_subtype | [optional] if omitted the server will use the default value of "milestone"
 **assignee_any** | **str**| Comma-separated list of user identifiers | [optional]
 **assignee_not** | **str**| Comma-separated list of user identifiers | [optional]
 **portfolios_any** | **str**| Comma-separated list of portfolio IDs | [optional]
 **projects_any** | **str**| Comma-separated list of project IDs | [optional]
 **projects_not** | **str**| Comma-separated list of project IDs | [optional]
 **projects_all** | **str**| Comma-separated list of project IDs | [optional]
 **sections_any** | **str**| Comma-separated list of section or column IDs | [optional]
 **sections_not** | **str**| Comma-separated list of section or column IDs | [optional]
 **sections_all** | **str**| Comma-separated list of section or column IDs | [optional]
 **tags_any** | **str**| Comma-separated list of tag IDs | [optional]
 **tags_not** | **str**| Comma-separated list of tag IDs | [optional]
 **tags_all** | **str**| Comma-separated list of tag IDs | [optional]
 **teams_any** | **str**| Comma-separated list of team IDs | [optional]
 **followers_not** | **str**| Comma-separated list of user identifiers | [optional]
 **created_by_any** | **str**| Comma-separated list of user identifiers | [optional]
 **created_by_not** | **str**| Comma-separated list of user identifiers | [optional]
 **assigned_by_any** | **str**| Comma-separated list of user identifiers | [optional]
 **assigned_by_not** | **str**| Comma-separated list of user identifiers | [optional]
 **liked_by_not** | **str**| Comma-separated list of user identifiers | [optional]
 **commented_on_by_not** | **str**| Comma-separated list of user identifiers | [optional]
 **due_on_before** | **date**| ISO 8601 date string | [optional]
 **due_on_after** | **date**| ISO 8601 date string | [optional]
 **due_on** | **date, none_type**| ISO 8601 date string or &#x60;null&#x60; | [optional]
 **due_at_before** | **datetime**| ISO 8601 datetime string | [optional]
 **due_at_after** | **datetime**| ISO 8601 datetime string | [optional]
 **start_on_before** | **date**| ISO 8601 date string | [optional]
 **start_on_after** | **date**| ISO 8601 date string | [optional]
 **start_on** | **date, none_type**| ISO 8601 date string or &#x60;null&#x60; | [optional]
 **created_on_before** | **date**| ISO 8601 date string | [optional]
 **created_on_after** | **date**| ISO 8601 date string | [optional]
 **created_on** | **date, none_type**| ISO 8601 date string or &#x60;null&#x60; | [optional]
 **created_at_before** | **datetime**| ISO 8601 datetime string | [optional]
 **created_at_after** | **datetime**| ISO 8601 datetime string | [optional]
 **completed_on_before** | **date**| ISO 8601 date string | [optional]
 **completed_on_after** | **date**| ISO 8601 date string | [optional]
 **completed_on** | **date, none_type**| ISO 8601 date string or &#x60;null&#x60; | [optional]
 **completed_at_before** | **datetime**| ISO 8601 datetime string | [optional]
 **completed_at_after** | **datetime**| ISO 8601 datetime string | [optional]
 **modified_on_before** | **date**| ISO 8601 date string | [optional]
 **modified_on_after** | **date**| ISO 8601 date string | [optional]
 **modified_on** | **date, none_type**| ISO 8601 date string or &#x60;null&#x60; | [optional]
 **modified_at_before** | **datetime**| ISO 8601 datetime string | [optional]
 **modified_at_after** | **datetime**| ISO 8601 datetime string | [optional]
 **is_blocking** | **bool**| Filter to incomplete tasks with dependents | [optional]
 **is_blocked** | **bool**| Filter to tasks with incomplete dependencies | [optional]
 **has_attachment** | **bool**| Filter to tasks with attachments | [optional]
 **completed** | **bool**| Filter to completed tasks | [optional]
 **is_subtask** | **bool**| Filter to subtasks | [optional]
 **sort_by** | **str**| One of &#x60;due_date&#x60;, &#x60;created_at&#x60;, &#x60;completed_at&#x60;, &#x60;likes&#x60;, or &#x60;modified_at&#x60;, defaults to &#x60;modified_at&#x60; | [optional] if omitted the server will use the default value of "modified_at"
 **sort_ascending** | **bool**| Default &#x60;false&#x60; | [optional] if omitted the server will use the default value of False
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the section&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parent_for_task**
> CreateTask201Response set_parent_for_task(task_gid, set_parent_for_task_request)

Set the parent of a task

parent, or no parent task at all. Returns an empty data block. When using `insert_before` and `insert_after`, at most one of those two options can be specified, and they must already be subtasks of the parent.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    set_parent_for_task_request = SetParentForTaskRequest(
        data=TaskSetParentRequest(
            parent="987654",
            insert_after="null",
            insert_before="124816",
        ),
    ) # SetParentForTaskRequest | The new parent of the subtask.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","due_on","name","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Set the parent of a task
        api_response = api_instance.set_parent_for_task(task_gid, set_parent_for_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->set_parent_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set the parent of a task
        api_response = api_instance.set_parent_for_task(task_gid, set_parent_for_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->set_parent_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **set_parent_for_task_request** | [**SetParentForTaskRequest**](SetParentForTaskRequest.md)| The new parent of the subtask. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully changed the parent of the specified subtask. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> CreateTask201Response update_task(task_gid, create_task_request)

Update a task

A specific, existing task can be updated by making a PUT request on the URL for that task. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated task record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import tasks_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tasks_api.TasksApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    create_task_request = CreateTaskRequest(
        data=TaskRequest(None),
    ) # CreateTaskRequest | The task to update.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","memberships","parent","assignee_status","actual_time_minutes","custom_fields","html_notes","start_at","assignee_section","due_on","name","permalink_url","external","modified_at","num_hearts","num_likes","resource_subtype","projects","num_subtasks","completed_at","completed_by","dependencies","approval_status","dependents","hearts","likes","liked","workspace","tags","hearted","due_at","completed","is_rendered_as_separator","notes","assignee","followers","start_on"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Update a task
        api_response = api_instance.update_task(task_gid, create_task_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a task
        api_response = api_instance.update_task(task_gid, create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| The task to update. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

