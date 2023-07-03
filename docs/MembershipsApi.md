# asana_preview.MembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](MembershipsApi.md#create_membership) | **POST** /memberships | Create a membership
[**delete_membership**](MembershipsApi.md#delete_membership) | **DELETE** /memberships/{membership_gid} | Delete a membership
[**get_memberships**](MembershipsApi.md#get_memberships) | **GET** /memberships | Get multiple memberships
[**update_membership**](MembershipsApi.md#update_membership) | **PUT** /memberships/{membership_gid} | Update a membership

# **create_membership**
> MembershipResponseData create_membership(body=body)

Create a membership

Creates a new membership in a `goal`. `Teams` or `users` can be a member of `goals`.  Returns the full record of the newly created membership.

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
api_instance = asana_preview.MembershipsApi(asana_preview.ApiClient(configuration))
body = asana_preview.MembershipsBody() # MembershipsBody | The updated fields for the membership. (optional)

try:
    # Create a membership
    api_response = api_instance.create_membership(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MembershipsBody**](MembershipsBody.md)| The updated fields for the membership. | [optional] 

### Return type

[**MembershipResponseData**](MembershipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> EmptyResponseData delete_membership(membership_gid)

Delete a membership

A specific, existing membership can be deleted by making a `DELETE` request on the URL for that membership.  Returns an empty data record.

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
api_instance = asana_preview.MembershipsApi(asana_preview.ApiClient(configuration))
membership_gid = '12345' # str | Globally unique identifier for the membership.

try:
    # Delete a membership
    api_response = api_instance.delete_membership(membership_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_gid** | **str**| Globally unique identifier for the membership. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memberships**
> MembershipResponseArray get_memberships(parent=parent, member=member, limit=limit, offset=offset)

Get multiple memberships

Returns compact `goal_membership` records. The possible types for `parent` in this request are `goal`. An additional member (user GID or team GID) can be passed in to filter to a specific membership.

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
api_instance = asana_preview.MembershipsApi(asana_preview.ApiClient(configuration))
parent = '159874' # str | Globally unique identifier for `goal`. (optional)
member = '1061493' # str | Globally unique identifier for `team` or `user`. (optional)
limit = 50 # int | Pagination limit for the request. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)

try:
    # Get multiple memberships
    api_response = api_instance.get_memberships(parent=parent, member=member, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->get_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for &#x60;goal&#x60;. | [optional] 
 **member** | **str**| Globally unique identifier for &#x60;team&#x60; or &#x60;user&#x60;. | [optional] 
 **limit** | **int**| Pagination limit for the request. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 

### Return type

[**MembershipResponseArray**](MembershipResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_membership**
> MembershipResponseData update_membership(membership_gid, body=body)

Update a membership

An existing membership can be updated by making a `PUT` request on the URL for that goal. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged. Memberships on `project`, `portfolio`, `team`, and `goals` can be updated.

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
api_instance = asana_preview.MembershipsApi(asana_preview.ApiClient(configuration))
membership_gid = '12345' # str | Globally unique identifier for the membership.
body = asana_preview.MembershipsMembershipGidBody() # MembershipsMembershipGidBody | The updated fields for the membership. (optional)

try:
    # Update a membership
    api_response = api_instance.update_membership(membership_gid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_gid** | **str**| Globally unique identifier for the membership. | 
 **body** | [**MembershipsMembershipGidBody**](MembershipsMembershipGidBody.md)| The updated fields for the membership. | [optional] 

### Return type

[**MembershipResponseData**](MembershipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

