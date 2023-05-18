# asana_preview.BatchAPIApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_request**](BatchAPIApi.md#create_batch_request) | **POST** /batch | Submit parallel requests


# **create_batch_request**
> CreateBatchRequest200Response create_batch_request(create_batch_request_request)

Submit parallel requests

Make multiple requests in parallel to Asana's API.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import batch_api_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_api_api.BatchAPIApi(api_client)
    create_batch_request_request = CreateBatchRequestRequest(
        data=BatchRequest(
            actions=[
                BatchRequestActionsInner(
                    relative_path="/tasks/123",
                    method="get",
                    data={},
                    options=BatchRequestActionsInnerOptions(
                        limit=50,
                        offset=1,
                        fields=["name","gid","notes","completed"],
                    ),
                ),
            ],
        ),
    ) # CreateBatchRequestRequest | The requests to batch together via the Batch API.
    opt_pretty = True # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ["headers","status_code","body"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Submit parallel requests
        api_response = api_instance.create_batch_request(create_batch_request_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling BatchAPIApi->create_batch_request: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submit parallel requests
        api_response = api_instance.create_batch_request(create_batch_request_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling BatchAPIApi->create_batch_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_batch_request_request** | [**CreateBatchRequestRequest**](CreateBatchRequestRequest.md)| The requests to batch together via the Batch API. |
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**CreateBatchRequest200Response**](CreateBatchRequest200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully completed the requested batch API operations. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

