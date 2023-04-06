# asana_preview.SectionsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sections_for_project**](SectionsApi.md#get_sections_for_project) | **GET** /projects/{project_gid}/sections | Get sections in a project


# **get_sections_for_project**
> GetSectionsForProject200Response get_sections_for_project(project_gid)

Get sections in a project

Returns the compact records for all sections in the specified project.

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import sections_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sections_api.SectionsApi(api_client)
    project_gid = "1331" # str | Globally unique identifier for the project.
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  'Note: You can only pass in an offset that was returned to you via a previously paginated request. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get sections in a project
        api_response = api_instance.get_sections_for_project(project_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling SectionsApi->get_sections_for_project: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get sections in a project
        api_response = api_instance.get_sections_for_project(project_gid, opt_fields=opt_fields, opt_pretty=opt_pretty, limit=limit, offset=offset)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling SectionsApi->get_sections_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. |
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token.  An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.  &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request. | [optional]

### Return type

[**GetSectionsForProject200Response**](GetSectionsForProject200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved sections in project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

