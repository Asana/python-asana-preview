# asana_preview.MembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](MembershipsApi.md#create_membership) | **POST** /memberships | Create a membership
[**delete_membership**](MembershipsApi.md#delete_membership) | **DELETE** /memberships/{membership_gid} | Delete a membership
[**get_memberships**](MembershipsApi.md#get_memberships) | **GET** /memberships | Get multiple memberships
[**update_membership**](MembershipsApi.md#update_membership) | **PUT** /memberships/{membership_gid} | Update a membership


# **create_membership**
> CreateMembership200Response create_membership()

Create a membership

Creates a new membership in a `team`, `project`, `goal`, or `portfolio`. `Teams` or `users` can be a member of `goals`. `Project`, `team`, and `portfolios` have users as members.  Returns the full record of the newly created membership.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import memberships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memberships_api.MembershipsApi(api_client)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    create_membership_request = CreateMembershipRequest(
        data=CreateMembershipRequest(
            is_active=True,
            is_guest=True,
            is_admin=False,
            member="12345",
            parent="true",
        ),
    ) # CreateMembershipRequest | The updated fields for the membership. (optional)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a membership
        api_response = api_instance.create_membership(opt_pretty=opt_pretty, create_membership_request=create_membership_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling MembershipsApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **create_membership_request** | [**CreateMembershipRequest**](CreateMembershipRequest.md)| The updated fields for the membership. | [optional]

### Return type

[**CreateMembership200Response**](CreateMembership200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created the requested membership. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> DeleteAttachment200Response delete_membership(membership_gid)

Delete a membership

A specific, existing membership can be deleted by making a `DELETE` request on the URL for that membership.  Returns an empty data record.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import memberships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memberships_api.MembershipsApi(api_client)
    membership_gid = "12345" # str | Globally unique identifier for the membership.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Delete a membership
        api_response = api_instance.delete_membership(membership_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling MembershipsApi->delete_membership: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a membership
        api_response = api_instance.delete_membership(membership_gid, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling MembershipsApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_gid** | **str**| Globally unique identifier for the membership. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted the requested membership. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memberships**
> GetMemberships200Response get_memberships()

Get multiple memberships

Returns compact `goal_membership`, `team_membership`, `project_membership`, `portfolio_membership`, or `workspace_membership` records. The possible types for `parent` in this request are `project`, `portfolio`, `team`, `goal`, and `workspace`. An additional member (user GID or team GID) can be passed in to filter to a specific membership. If a `parent` param is not provided, a `member`, `resource_subtype`, and `workspace` param must be provided.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import memberships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memberships_api.MembershipsApi(api_client)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    parent = "159874" # str | Globally unique identifier for `project`, `portfolio`,   `team`, `goal`, and `workspace`. (optional)
    member = "1061493" # str | Globally unique identifier for `team` or `user`. (optional)
    resource_subtype = "team_membership" # str | The resource_subtype to filter on. Must be provided with `member` and `workspace` if `parent` is not provided. Valid values include `team_membership`, `workspace_membership`, `portfolio_membership` (optional)
    workspace = "75642" # str | The workspace to filter on. Must be provided with `member` and `resource_subtype` if `parent` is not provided. (optional)
    limit = 50 # int | Pagination limit for the request. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get multiple memberships
        api_response = api_instance.get_memberships(opt_pretty=opt_pretty, parent=parent, member=member, resource_subtype=resource_subtype, workspace=workspace, limit=limit, offset=offset)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling MembershipsApi->get_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **parent** | **str**| Globally unique identifier for &#x60;project&#x60;, &#x60;portfolio&#x60;,   &#x60;team&#x60;, &#x60;goal&#x60;, and &#x60;workspace&#x60;. | [optional]
 **member** | **str**| Globally unique identifier for &#x60;team&#x60; or &#x60;user&#x60;. | [optional]
 **resource_subtype** | **str**| The resource_subtype to filter on. Must be provided with &#x60;member&#x60; and &#x60;workspace&#x60; if &#x60;parent&#x60; is not provided. Valid values include &#x60;team_membership&#x60;, &#x60;workspace_membership&#x60;, &#x60;portfolio_membership&#x60; | [optional]
 **workspace** | **str**| The workspace to filter on. Must be provided with &#x60;member&#x60; and &#x60;resource_subtype&#x60; if &#x60;parent&#x60; is not provided. | [optional]
 **limit** | **int**| Pagination limit for the request. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]

### Return type

[**GetMemberships200Response**](GetMemberships200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested membership. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_membership**
> CreateMembership200Response update_membership(membership_gid)

Update a membership

An existing membership can be updated by making a `PUT` request on the URL for that goal. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged. Memberships on `project`, `portfolio`, `team`, and `goals` can be updated.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import memberships_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memberships_api.MembershipsApi(api_client)
    membership_gid = "12345" # str | Globally unique identifier for the membership.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    update_membership_request = UpdateMembershipRequest(
        data=MembershipRequest(
            is_active=True,
            is_guest=True,
            is_admin=False,
        ),
    ) # UpdateMembershipRequest | The updated fields for the membership. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Update a membership
        api_response = api_instance.update_membership(membership_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling MembershipsApi->update_membership: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a membership
        api_response = api_instance.update_membership(membership_gid, opt_pretty=opt_pretty, update_membership_request=update_membership_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling MembershipsApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_gid** | **str**| Globally unique identifier for the membership. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **update_membership_request** | [**UpdateMembershipRequest**](UpdateMembershipRequest.md)| The updated fields for the membership. | [optional]

### Return type

[**CreateMembership200Response**](CreateMembership200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the requested membership. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

