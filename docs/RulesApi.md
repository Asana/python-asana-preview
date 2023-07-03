# asana_preview.RulesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_rule**](RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule

# **trigger_rule**
> RuleTriggerResponseData trigger_rule(body, rule_trigger_gid)

Trigger a rule

Trigger a rule which uses an [\"incoming web request\"](/docs/incoming-web-requests) trigger.

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
api_instance = asana_preview.RulesApi(asana_preview.ApiClient(configuration))
body = asana_preview.RuleTriggerGidRunBody() # RuleTriggerGidRunBody | A dictionary of variables accessible from within the rule.
rule_trigger_gid = '12345' # str | The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint.

try:
    # Trigger a rule
    api_response = api_instance.trigger_rule(body, rule_trigger_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->trigger_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RuleTriggerGidRunBody**](RuleTriggerGidRunBody.md)| A dictionary of variables accessible from within the rule. | 
 **rule_trigger_gid** | **str**| The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint. | 

### Return type

[**RuleTriggerResponseData**](RuleTriggerResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

