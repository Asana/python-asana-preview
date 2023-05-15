# asana_preview.RulesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_rule**](RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule


# **trigger_rule**
> TriggerRule200Response trigger_rule(rule_trigger_gid, trigger_rule_request)

Trigger a rule

Trigger a rule which uses an [\"incoming web request\"](/docs/incoming-web-requests) trigger.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import rules_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rules_api.RulesApi(api_client)
    rule_trigger_gid = "12345" # str | The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint.
    trigger_rule_request = TriggerRuleRequest(
        data=RuleTriggerRequest(
            resource="12345",
            action_data={},
        ),
    ) # TriggerRuleRequest | A dictionary of variables accessible from within the rule.
    opt_fields = ["message"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Trigger a rule
        api_response = api_instance.trigger_rule(rule_trigger_gid, trigger_rule_request)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling RulesApi->trigger_rule: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Trigger a rule
        api_response = api_instance.trigger_rule(rule_trigger_gid, trigger_rule_request, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling RulesApi->trigger_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_trigger_gid** | **str**| The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint. |
 **trigger_rule_request** | [**TriggerRuleRequest**](TriggerRuleRequest.md)| A dictionary of variables accessible from within the rule. |
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**TriggerRule200Response**](TriggerRule200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully triggered a rule. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

