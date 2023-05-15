# asana_preview.TypeaheadApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**typeahead_for_workspace**](TypeaheadApi.md#typeahead_for_workspace) | **GET** /workspaces/{workspace_gid}/typeahead | Get objects via typeahead


# **typeahead_for_workspace**
> TypeaheadForWorkspace200Response typeahead_for_workspace(workspace_gid, )

Get objects via typeahead

Retrieves objects in the workspace based via an auto-completion/typeahead search algorithm. This feature is meant to provide results quickly, so do not rely on this API to provide extremely accurate search results. The result set is limited to a single page of results with a maximum size, so you won’t be able to fetch large numbers of results.  The typeahead search API provides search for objects from a single workspace. This endpoint should be used to query for objects when creating an auto-completion/typeahead search feature. This API is meant to provide results quickly and should not be relied upon for accurate or exhaustive search results. The results sets are limited in size and cannot be paginated.  Queries return a compact representation of each object which is typically the gid and name fields. Interested in a specific set of fields or all of the fields?! Of course you are. Use field selectors to manipulate what data is included in a response.  Resources with type `user` are returned in order of most contacted to least contacted. This is determined by task assignments, adding the user to projects, and adding the user as a follower to tasks, messages, etc.  Resources with type `project` are returned in order of recency. This is determined when the user visits the project, is added to the project, and completes tasks in the project.  Resources with type `task` are returned with priority placed on tasks the user is following, but no guarantee on the order of those tasks.  Resources with type `project_template` are returned with priority placed on favorited project templates.  Leaving the `query` string empty or omitted will give you results, still following the resource ordering above. This could be used to list users or projects that are relevant for the requesting user's api token.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import typeahead_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = typeahead_api.TypeaheadApi(api_client)
    workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
    type = "user" # str | *Deprecated: new integrations should prefer the resource_type field.* (optional) if omitted the server will use the default value of "user"
    query = "Greg" # str | The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results. (optional)
    count = 20 # int | The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["name"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get objects via typeahead
        api_response = api_instance.typeahead_for_workspace(workspace_gid, )
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TypeaheadApi->typeahead_for_workspace: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get objects via typeahead
        api_response = api_instance.typeahead_for_workspace(workspace_gid, type=type, query=query, count=count, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling TypeaheadApi->typeahead_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. |
 **resource_type** | **str**| The type of values the typeahead should return. You can choose from one of the following: &#x60;custom_field&#x60;, &#x60;project&#x60;, &#x60;project_template&#x60;, &#x60;portfolio&#x60;, &#x60;tag&#x60;, &#x60;task&#x60;, and &#x60;user&#x60;. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. &#x60;task&#x60;). Using multiple types is not yet supported. | defaults to "user"
 **type** | **str**| *Deprecated: new integrations should prefer the resource_type field.* | [optional] if omitted the server will use the default value of "user"
 **query** | **str**| The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results. | [optional]
 **count** | **int**| The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**TypeaheadForWorkspace200Response**](TypeaheadForWorkspace200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved objects via a typeahead search algorithm. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

