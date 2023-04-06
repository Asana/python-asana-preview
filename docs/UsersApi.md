# asana_preview.UsersApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UsersApi.md#get_user) | **GET** /users/{user_gid} | Get a user


# **get_user**
> GetUser200Response get_user(user_gid)

Get a user

Returns the full user record for the single user with the provided ID.

### Example

* Bearer Authentication (personal_access_token):

```python
import asana_preview
from asana_preview.api import users_api
from pprint import pprint

# Configure Bearer authorization: personal_access_token
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
    opt_fields = ["gid","resource_type"] # [str] | Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. (optional)
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get a user
        api_response = api_instance.get_user(user_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a user
        api_response = api_instance.get_user(user_gid, opt_fields=opt_fields, opt_pretty=opt_pretty)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. |
 **opt_fields** | **[str]**| Defines fields to return.  Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.  The gid of included objects will always be returned, regardless of the field options. | [optional]
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[personal_access_token](../README.md#personal_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the user specified. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

