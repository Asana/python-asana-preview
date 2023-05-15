# asana_preview.GoalsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_goal**](GoalsApi.md#create_goal) | **POST** /goals | Create a goal
[**create_goal_metric**](GoalsApi.md#create_goal_metric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
[**delete_goal**](GoalsApi.md#delete_goal) | **DELETE** /goals/{goal_gid} | Delete a goal
[**get_goal**](GoalsApi.md#get_goal) | **GET** /goals/{goal_gid} | Get a goal
[**get_goals**](GoalsApi.md#get_goals) | **GET** /goals | Get goals
[**get_parent_goals_for_goal**](GoalsApi.md#get_parent_goals_for_goal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
[**update_goal**](GoalsApi.md#update_goal) | **PUT** /goals/{goal_gid} | Update a goal
[**update_goal_metric**](GoalsApi.md#update_goal_metric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric


# **create_goal**
> GetGoal200Response create_goal(update_goal_request)

Create a goal

Creates a new goal in a workspace or team.  Returns the full record of the newly created goal.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    update_goal_request = UpdateGoalRequest(
        data=GoalRequest(None),
    ) # UpdateGoalRequest | The goal to create.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","due_on","current_status_update","name","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Create a goal
        api_response = api_instance.create_goal(update_goal_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->create_goal: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a goal
        api_response = api_instance.create_goal(update_goal_request, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->create_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_goal_request** | [**UpdateGoalRequest**](UpdateGoalRequest.md)| The goal to create. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal_metric**
> GetGoal200Response create_goal_metric(goal_gid, create_goal_metric_request)

Create a goal metric

Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    create_goal_metric_request = CreateGoalMetricRequest(
        data=GoalMetricBase(None),
    ) # CreateGoalMetricRequest | The goal metric to create.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","due_on","current_status_update","name","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Create a goal metric
        api_response = api_instance.create_goal_metric(goal_gid, create_goal_metric_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->create_goal_metric: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a goal metric
        api_response = api_instance.create_goal_metric(goal_gid, create_goal_metric_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->create_goal_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **create_goal_metric_request** | [**CreateGoalMetricRequest**](CreateGoalMetricRequest.md)| The goal metric to create. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new goal metric. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_goal**
> DeleteAttachment200Response delete_goal(goal_gid)

Delete a goal

A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.  Returns an empty data record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Delete a goal
        api_response = api_instance.delete_goal(goal_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->delete_goal: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a goal
        api_response = api_instance.delete_goal(goal_gid, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->delete_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
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
**200** | Successfully deleted the specified goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal**
> GetGoal200Response get_goal(goal_gid)

Get a goal

Returns the complete goal record for a single goal.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","due_on","current_status_update","name","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get a goal
        api_response = api_instance.get_goal(goal_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->get_goal: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a goal
        api_response = api_instance.get_goal(goal_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->get_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the record for a single goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals**
> GetGoals200Response get_goals()

Get goals

Returns compact goal records.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    portfolio = "159874" # str | Globally unique identifier for supporting portfolio. (optional)
    project = "512241" # str | Globally unique identifier for supporting project. (optional)
    is_workspace_level = False # bool | Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. (optional)
    team = "31326" # str | Globally unique identifier for the team. (optional)
    workspace = "31326" # str | Globally unique identifier for the workspace. (optional)
    time_periods = [
        "221693,506165",
    ] # [str] | Globally unique identifiers for the time periods. (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","name","current_status_update","due_on","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get goals
        api_response = api_instance.get_goals(opt_pretty=opt_pretty, limit=limit, offset=offset, portfolio=portfolio, project=project, is_workspace_level=is_workspace_level, team=team, workspace=workspace, time_periods=time_periods, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->get_goals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **portfolio** | **str**| Globally unique identifier for supporting portfolio. | [optional]
 **project** | **str**| Globally unique identifier for supporting project. | [optional]
 **is_workspace_level** | **bool**| Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. | [optional]
 **team** | **str**| Globally unique identifier for the team. | [optional]
 **workspace** | **str**| Globally unique identifier for the workspace. | [optional]
 **time_periods** | **[str]**| Globally unique identifiers for the time periods. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoals200Response**](GetGoals200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested goals. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_goals_for_goal**
> GetGoals200Response get_parent_goals_for_goal(goal_gid)

Get parent goals from a goal

Returns a compact representation of all of the parent goals of a goal.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","name","current_status_update","due_on","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get parent goals from a goal
        api_response = api_instance.get_parent_goals_for_goal(goal_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->get_parent_goals_for_goal: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get parent goals from a goal
        api_response = api_instance.get_parent_goals_for_goal(goal_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->get_parent_goals_for_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoals200Response**](GetGoals200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified goal&#39;s parent goals. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal**
> GetGoal200Response update_goal(goal_gid, update_goal_request)

Update a goal

An existing goal can be updated by making a PUT request on the URL for that goal. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    update_goal_request = UpdateGoalRequest(
        data=GoalRequest(None),
    ) # UpdateGoalRequest | The updated fields for the goal.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","due_on","current_status_update","name","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Update a goal
        api_response = api_instance.update_goal(goal_gid, update_goal_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->update_goal: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a goal
        api_response = api_instance.update_goal(goal_gid, update_goal_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->update_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **update_goal_request** | [**UpdateGoalRequest**](UpdateGoalRequest.md)| The updated fields for the goal. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_metric**
> GetGoal200Response update_goal_metric(goal_gid, update_goal_metric_request)

Update a goal metric

Updates a goal's existing metric's `current_number_value` if one exists, otherwise responds with a 400 status code.  Returns the complete updated goal metric record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goals_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goals_api.GoalsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    update_goal_metric_request = UpdateGoalMetricRequest(
        data=GoalMetricCurrentValueRequest(None),
    ) # UpdateGoalMetricRequest | The updated fields for the goal metric.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["status","is_workspace_level","num_likes","html_notes","notes","workspace","followers","time_period","start_on","due_on","current_status_update","name","likes","liked","metric","team","owner"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Update a goal metric
        api_response = api_instance.update_goal_metric(goal_gid, update_goal_metric_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->update_goal_metric: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a goal metric
        api_response = api_instance.update_goal_metric(goal_gid, update_goal_metric_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalsApi->update_goal_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **update_goal_metric_request** | [**UpdateGoalMetricRequest**](UpdateGoalMetricRequest.md)| The updated fields for the goal metric. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the goal metric. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

