# asana_preview.GoalRelationshipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_supporting_relationship**](GoalRelationshipsApi.md#add_supporting_relationship) | **POST** /goals/{goal_gid}/addSupportingRelationship | Add a supporting goal relationship
[**get_goal_relationship**](GoalRelationshipsApi.md#get_goal_relationship) | **GET** /goal_relationships/{goal_relationship_gid} | Get a goal relationship
[**get_goal_relationships**](GoalRelationshipsApi.md#get_goal_relationships) | **GET** /goal_relationships | Get goal relationships
[**remove_supporting_relationship**](GoalRelationshipsApi.md#remove_supporting_relationship) | **POST** /goals/{goal_gid}/removeSupportingRelationship | Removes a supporting goal relationship
[**update_goal_relationship**](GoalRelationshipsApi.md#update_goal_relationship) | **PUT** /goal_relationships/{goal_relationship_gid} | Update a goal relationship


# **add_supporting_relationship**
> GetGoalRelationship200Response add_supporting_relationship(goal_gid, add_supporting_relationship_request)

Add a supporting goal relationship

Creates a goal relationship by adding a supporting resource to a given goal.  Returns the newly created goal relationship record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goal_relationships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goal_relationships_api.GoalRelationshipsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    add_supporting_relationship_request = AddSupportingRelationshipRequest(
        data=GoalAddSupportingRelationshipRequest(
            supporting_resource="12345",
            insert_before="1331",
            insert_after="1331",
            contribution_weight=1,
        ),
    ) # AddSupportingRelationshipRequest | The supporting resource to be added to the goal
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["supporting_resource","supported_goal","contribution_weight","resource_subtype"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Add a supporting goal relationship
        api_response = api_instance.add_supporting_relationship(goal_gid, add_supporting_relationship_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->add_supporting_relationship: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a supporting goal relationship
        api_response = api_instance.add_supporting_relationship(goal_gid, add_supporting_relationship_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->add_supporting_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **add_supporting_relationship_request** | [**AddSupportingRelationshipRequest**](AddSupportingRelationshipRequest.md)| The supporting resource to be added to the goal |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoalRelationship200Response**](GetGoalRelationship200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created the goal relationship. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_relationship**
> GetGoalRelationship200Response get_goal_relationship(goal_relationship_gid)

Get a goal relationship

Returns the complete updated goal relationship record for a single goal relationship.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goal_relationships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goal_relationships_api.GoalRelationshipsApi(api_client)
    goal_relationship_gid = "12345" # str | Globally unique identifier for the goal relationship.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["supporting_resource","supported_goal","contribution_weight","resource_subtype"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get a goal relationship
        api_response = api_instance.get_goal_relationship(goal_relationship_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->get_goal_relationship: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a goal relationship
        api_response = api_instance.get_goal_relationship(goal_relationship_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->get_goal_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_relationship_gid** | **str**| Globally unique identifier for the goal relationship. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoalRelationship200Response**](GetGoalRelationship200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the record for the goal relationship. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_relationships**
> GetGoalRelationships200Response get_goal_relationships(supported_goal)

Get goal relationships

Returns compact goal relationship records.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goal_relationships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goal_relationships_api.GoalRelationshipsApi(api_client)
    supported_goal = "12345" # str | Globally unique identifier for the supported goal in the goal relationship.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    resource_subtype = "subgoal" # str | If provided, filter to goal relationships with a given resource_subtype. (optional)
    opt_fields = ["supporting_resource","supported_goal","contribution_weight","resource_subtype"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get goal relationships
        api_response = api_instance.get_goal_relationships(supported_goal)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->get_goal_relationships: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get goal relationships
        api_response = api_instance.get_goal_relationships(supported_goal, opt_pretty=opt_pretty, resource_subtype=resource_subtype, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->get_goal_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supported_goal** | **str**| Globally unique identifier for the supported goal in the goal relationship. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **resource_subtype** | **str**| If provided, filter to goal relationships with a given resource_subtype. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoalRelationships200Response**](GetGoalRelationships200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested goal relationships. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supporting_relationship**
> DeleteAttachment200Response remove_supporting_relationship(goal_gid, remove_supporting_relationship_request)

Removes a supporting goal relationship

Removes a goal relationship for a given parent goal.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goal_relationships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goal_relationships_api.GoalRelationshipsApi(api_client)
    goal_gid = "12345" # str | Globally unique identifier for the goal.
    remove_supporting_relationship_request = RemoveSupportingRelationshipRequest(
        data=GoalRemoveSupportingRelationshipRequest(
            supporting_resource="12345",
        ),
    ) # RemoveSupportingRelationshipRequest | The supporting resource to be removed from the goal
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Removes a supporting goal relationship
        api_response = api_instance.remove_supporting_relationship(goal_gid, remove_supporting_relationship_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->remove_supporting_relationship: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes a supporting goal relationship
        api_response = api_instance.remove_supporting_relationship(goal_gid, remove_supporting_relationship_request, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->remove_supporting_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. |
 **remove_supporting_relationship_request** | [**RemoveSupportingRelationshipRequest**](RemoveSupportingRelationshipRequest.md)| The supporting resource to be removed from the goal |
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
**200** | Successfully removed the goal relationship. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_relationship**
> GetGoalRelationship200Response update_goal_relationship(goal_relationship_gid, update_goal_relationship_request)

Update a goal relationship

An existing goal relationship can be updated by making a PUT request on the URL for that goal relationship. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal relationship record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import goal_relationships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goal_relationships_api.GoalRelationshipsApi(api_client)
    goal_relationship_gid = "12345" # str | Globally unique identifier for the goal relationship.
    update_goal_relationship_request = UpdateGoalRelationshipRequest(
        data=GoalRelationshipRequest(None),
    ) # UpdateGoalRelationshipRequest | The updated fields for the goal relationship.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["supporting_resource","supported_goal","contribution_weight","resource_subtype"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Update a goal relationship
        api_response = api_instance.update_goal_relationship(goal_relationship_gid, update_goal_relationship_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->update_goal_relationship: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a goal relationship
        api_response = api_instance.update_goal_relationship(goal_relationship_gid, update_goal_relationship_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling GoalRelationshipsApi->update_goal_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_relationship_gid** | **str**| Globally unique identifier for the goal relationship. |
 **update_goal_relationship_request** | [**UpdateGoalRelationshipRequest**](UpdateGoalRelationshipRequest.md)| The updated fields for the goal relationship. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetGoalRelationship200Response**](GetGoalRelationship200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the goal relationship. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

