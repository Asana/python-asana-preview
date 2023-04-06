# asana_preview.ProjectsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects


# **get_project**
> GetProject200Response get_project(project_gid)

Get a project

Returns the complete project record for a single project.

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import projects_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_gid = "1331" # str | Globally unique identifier for the project.
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get a project
        api_response = api_instance.get_project(project_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a project
        api_response = api_instance.get_project(project_gid, opt_fields=opt_fields, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. |
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**GetProject200Response**](GetProject200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> GetProjects200Response get_projects()

Get multiple projects

Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned.  *Note: This endpoint may timeout for large domains. Try filtering by team!*

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import projects_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request. (optional)
    archived = False # bool | Only return projects whose `archived` field takes on the value of this parameter. (optional)
    team = "14916" # str | The team to filter projects on. (optional)
    workspace = "1331" # str | The workspace or organization to filter projects on. (optional)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get multiple projects
        api_response = api_instance.get_projects(opt_fields=opt_fields, opt_pretty=opt_pretty, limit=limit, offset=offset, archived=archived, team=team, workspace=workspace)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request. | [optional]
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional]
 **team** | **str**| The team to filter projects on. | [optional]
 **workspace** | **str**| The workspace or organization to filter projects on. | [optional]

### Return type

[**GetProjects200Response**](GetProjects200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved projects. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

