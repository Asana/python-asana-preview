# asana_preview.StoriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_story_for_task**](StoriesApi.md#create_story_for_task) | **POST** /tasks/{task_gid}/stories | Create a story on a task
[**delete_story**](StoriesApi.md#delete_story) | **DELETE** /stories/{story_gid} | Delete a story
[**get_stories_for_task**](StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
[**get_story**](StoriesApi.md#get_story) | **GET** /stories/{story_gid} | Get a story
[**update_story**](StoriesApi.md#update_story) | **PUT** /stories/{story_gid} | Update a story


# **create_story_for_task**
> GetStory200Response create_story_for_task(task_gid, update_story_request)

Create a story on a task

Adds a story to a task. This endpoint currently only allows for comment stories to be created. The comment will be authored by the currently authenticated user, and timestamped when the server receives the request.  Returns the full record for the new story added to the task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import stories_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stories_api.StoriesApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    update_story_request = UpdateStoryRequest(
        data=StoryBase(None),
    ) # UpdateStoryRequest | The story to create.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","new_enum_value","created_by","new_number_value","is_edited","previews","old_multi_enum_values","new_name","new_people_value","project","follower","new_resource_subtype","tag","old_resource_subtype","task","is_editable","sticker_name","story","new_section","num_likes","num_hearts","old_name","resource_subtype","html_text","duplicate_of","hearts","source","target","likes","liked","old_date_value","old_enum_value","hearted","old_section","new_date_value","type","new_approval_status","text","old_people_value","assignee","new_dates","new_text_value","duplicated_from","custom_field","dependency","old_text_value","is_pinned","old_dates","old_approval_status","old_number_value","new_multi_enum_values"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Create a story on a task
        api_response = api_instance.create_story_for_task(task_gid, update_story_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->create_story_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a story on a task
        api_response = api_instance.create_story_for_task(task_gid, update_story_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->create_story_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. |
 **update_story_request** | [**UpdateStoryRequest**](UpdateStoryRequest.md)| The story to create. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetStory200Response**](GetStory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story**
> DeleteAttachment200Response delete_story(story_gid)

Delete a story

Deletes a story. A user can only delete stories they have created.  Returns an empty data record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import stories_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stories_api.StoriesApi(api_client)
    story_gid = "35678" # str | Globally unique identifier for the story.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Delete a story
        api_response = api_instance.delete_story(story_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->delete_story: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a story
        api_response = api_instance.delete_story(story_gid, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->delete_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. |
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
**200** | Successfully deleted the specified story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stories_for_task**
> GetStoriesForTask200Response get_stories_for_task(task_gid)

Get stories from a task

Returns the compact records for all stories on the task.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import stories_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stories_api.StoriesApi(api_client)
    task_gid = "321654" # str | The task to operate on.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","new_enum_value","created_by","new_number_value","is_edited","previews","old_multi_enum_values","new_name","new_people_value","project","follower","new_resource_subtype","tag","old_resource_subtype","task","is_editable","sticker_name","story","new_section","num_likes","num_hearts","old_name","resource_subtype","html_text","duplicate_of","hearts","source","target","likes","liked","old_date_value","old_enum_value","hearted","old_section","new_date_value","type","new_approval_status","text","old_people_value","assignee","new_dates","new_text_value","duplicated_from","custom_field","dependency","old_text_value","is_pinned","old_dates","old_approval_status","old_number_value","new_multi_enum_values"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get stories from a task
        api_response = api_instance.get_stories_for_task(task_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->get_stories_for_task: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get stories from a task
        api_response = api_instance.get_stories_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->get_stories_for_task: %s\n" % e)
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

[**GetStoriesForTask200Response**](GetStoriesForTask200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task&#39;s stories. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story**
> GetStory200Response get_story(story_gid)

Get a story

Returns the full record for a single story.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import stories_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stories_api.StoriesApi(api_client)
    story_gid = "35678" # str | Globally unique identifier for the story.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["created_at","new_enum_value","created_by","new_number_value","is_edited","previews","old_multi_enum_values","new_name","new_people_value","project","follower","new_resource_subtype","tag","old_resource_subtype","task","is_editable","sticker_name","story","new_section","num_likes","num_hearts","old_name","resource_subtype","html_text","duplicate_of","hearts","source","target","likes","liked","old_date_value","old_enum_value","hearted","old_section","new_date_value","type","new_approval_status","text","old_people_value","assignee","new_dates","new_text_value","duplicated_from","custom_field","dependency","old_text_value","is_pinned","old_dates","old_approval_status","old_number_value","new_multi_enum_values"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get a story
        api_response = api_instance.get_story(story_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->get_story: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a story
        api_response = api_instance.get_story(story_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->get_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetStory200Response**](GetStory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story**
> GetStory200Response update_story(story_gid, update_story_request)

Update a story

Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import stories_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stories_api.StoriesApi(api_client)
    story_gid = "35678" # str | Globally unique identifier for the story.
    update_story_request = UpdateStoryRequest(
        data=StoryBase(None),
    ) # UpdateStoryRequest | The comment story to update.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["created_at","new_enum_value","created_by","new_number_value","is_edited","previews","old_multi_enum_values","new_name","new_people_value","project","follower","new_resource_subtype","tag","old_resource_subtype","task","is_editable","sticker_name","story","new_section","num_likes","num_hearts","old_name","resource_subtype","html_text","duplicate_of","hearts","source","target","likes","liked","old_date_value","old_enum_value","hearted","old_section","new_date_value","type","new_approval_status","text","old_people_value","assignee","new_dates","new_text_value","duplicated_from","custom_field","dependency","old_text_value","is_pinned","old_dates","old_approval_status","old_number_value","new_multi_enum_values"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Update a story
        api_response = api_instance.update_story(story_gid, update_story_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->update_story: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a story
        api_response = api_instance.update_story(story_gid, update_story_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling StoriesApi->update_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. |
 **update_story_request** | [**UpdateStoryRequest**](UpdateStoryRequest.md)| The comment story to update. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetStory200Response**](GetStory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

