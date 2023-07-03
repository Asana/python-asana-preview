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
> GoalRelationshipResponseData add_supporting_relationship(body, goal_gid, opt_fields=opt_fields)

Add a supporting goal relationship

Creates a goal relationship by adding a supporting resource to a given goal.  Returns the newly created goal relationship record.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.GoalRelationshipsApi(asana_preview.ApiClient(configuration))
body = asana_preview.GoalGidAddSupportingRelationshipBody() # GoalGidAddSupportingRelationshipBody | The supporting resource to be added to the goal
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ['[\"contribution_weight\",\"resource_subtype\",\"supported_goal\",\"supported_goal.name\",\"supported_goal.owner\",\"supported_goal.owner.name\",\"supporting_resource\",\"supporting_resource.name\"]'] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Add a supporting goal relationship
    api_response = api_instance.add_supporting_relationship(body, goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->add_supporting_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalGidAddSupportingRelationshipBody**](GoalGidAddSupportingRelationshipBody.md)| The supporting resource to be added to the goal | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalRelationshipResponseData**](GoalRelationshipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_relationship**
> GoalRelationshipResponseData get_goal_relationship(goal_relationship_gid, opt_fields=opt_fields)

Get a goal relationship

Returns the complete updated goal relationship record for a single goal relationship.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.GoalRelationshipsApi(asana_preview.ApiClient(configuration))
goal_relationship_gid = '12345' # str | Globally unique identifier for the goal relationship.
opt_fields = ['[\"contribution_weight\",\"resource_subtype\",\"supported_goal\",\"supported_goal.name\",\"supported_goal.owner\",\"supported_goal.owner.name\",\"supporting_resource\",\"supporting_resource.name\"]'] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a goal relationship
    api_response = api_instance.get_goal_relationship(goal_relationship_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->get_goal_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_relationship_gid** | **str**| Globally unique identifier for the goal relationship. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalRelationshipResponseData**](GoalRelationshipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_relationships**
> GoalRelationshipResponseArray get_goal_relationships(supported_goal, resource_subtype=resource_subtype, opt_fields=opt_fields)

Get goal relationships

Returns compact goal relationship records.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.GoalRelationshipsApi(asana_preview.ApiClient(configuration))
supported_goal = '12345' # str | Globally unique identifier for the supported goal in the goal relationship.
resource_subtype = 'subgoal' # str | If provided, filter to goal relationships with a given resource_subtype. (optional)
opt_fields = ['[\"contribution_weight\",\"resource_subtype\",\"supported_goal\",\"supported_goal.name\",\"supported_goal.owner\",\"supported_goal.owner.name\",\"supporting_resource\",\"supporting_resource.name\"]'] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get goal relationships
    api_response = api_instance.get_goal_relationships(supported_goal, resource_subtype=resource_subtype, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->get_goal_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supported_goal** | **str**| Globally unique identifier for the supported goal in the goal relationship. | 
 **resource_subtype** | **str**| If provided, filter to goal relationships with a given resource_subtype. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalRelationshipResponseArray**](GoalRelationshipResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supporting_relationship**
> EmptyResponseData remove_supporting_relationship(body, goal_gid)

Removes a supporting goal relationship

Removes a goal relationship for a given parent goal.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.GoalRelationshipsApi(asana_preview.ApiClient(configuration))
body = asana_preview.GoalGidRemoveSupportingRelationshipBody() # GoalGidRemoveSupportingRelationshipBody | The supporting resource to be removed from the goal
goal_gid = '12345' # str | Globally unique identifier for the goal.

try:
    # Removes a supporting goal relationship
    api_response = api_instance.remove_supporting_relationship(body, goal_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->remove_supporting_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalGidRemoveSupportingRelationshipBody**](GoalGidRemoveSupportingRelationshipBody.md)| The supporting resource to be removed from the goal | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_relationship**
> GoalRelationshipResponseData update_goal_relationship(body, goal_relationship_gid, opt_fields=opt_fields)

Update a goal relationship

An existing goal relationship can be updated by making a PUT request on the URL for that goal relationship. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal relationship record.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.GoalRelationshipsApi(asana_preview.ApiClient(configuration))
body = asana_preview.GoalRelationshipsGoalRelationshipGidBody() # GoalRelationshipsGoalRelationshipGidBody | The updated fields for the goal relationship.
goal_relationship_gid = '12345' # str | Globally unique identifier for the goal relationship.
opt_fields = ['[\"contribution_weight\",\"resource_subtype\",\"supported_goal\",\"supported_goal.name\",\"supported_goal.owner\",\"supported_goal.owner.name\",\"supporting_resource\",\"supporting_resource.name\"]'] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a goal relationship
    api_response = api_instance.update_goal_relationship(body, goal_relationship_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->update_goal_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalRelationshipsGoalRelationshipGidBody**](GoalRelationshipsGoalRelationshipGidBody.md)| The updated fields for the goal relationship. | 
 **goal_relationship_gid** | **str**| Globally unique identifier for the goal relationship. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalRelationshipResponseData**](GoalRelationshipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

