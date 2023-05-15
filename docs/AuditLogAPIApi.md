# asana_preview.AuditLogAPIApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_events**](AuditLogAPIApi.md#get_audit_log_events) | **GET** /workspaces/{workspace_gid}/audit_log_events | Get audit log events


# **get_audit_log_events**
> GetAuditLogEvents200Response get_audit_log_events(workspace_gid)

Get audit log events

Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/reference/audit-log-api) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/reference/audit-log-api) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  *Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/reference/audit-log-api) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

### Example

* Bearer Authentication (personalAccessToken):

```python
import asana_preview
from asana_preview.api import audit_log_api_api
from pprint import pprint

# Configure Bearer authorization: personalAccessToken
configuration = asana_preview.Configuration(
    access_token = 'PERSONAL_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with asana_preview.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log_api_api.AuditLogAPIApi(api_client)
    workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
    start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter to events created after this time (inclusive). (optional)
    end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter to events created before this time (exclusive). (optional)
    event_type = "event_type_example" # str | Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values. (optional)
    actor_type = "user" # str | Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded. (optional)
    actor_gid = "actor_gid_example" # str | Filter to events triggered by the actor with this ID. (optional)
    resource_gid = "resource_gid_example" # str | Filter to events with this resource ID. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ["event_category","created_at","resource","event_type","details","actor","context"] # [str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    # Example passing only required values which don't have defaults set
    try:
        # Get audit log events
        api_response = api_instance.get_audit_log_events(workspace_gid)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling AuditLogAPIApi->get_audit_log_events: %s\n" % e)

    # Example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get audit log events
        api_response = api_instance.get_audit_log_events(workspace_gid, start_at=start_at, end_at=end_at, event_type=event_type, actor_type=actor_type, actor_gid=actor_gid, resource_gid=resource_gid, limit=limit, offset=offset, opt_fields=opt_fields)
        pprint(api_response)
    except asana_preview.ApiException as e:
        print("Exception when calling AuditLogAPIApi->get_audit_log_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. |
 **start_at** | **datetime**| Filter to events created after this time (inclusive). | [optional]
 **end_at** | **datetime**| Filter to events created before this time (exclusive). | [optional]
 **event_type** | **str**| Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values. | [optional]
 **actor_type** | **str**| Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If &#x60;actor_gid&#x60; is included, this should be excluded. | [optional]
 **actor_gid** | **str**| Filter to events triggered by the actor with this ID. | [optional]
 **resource_gid** | **str**| Filter to events with this resource ID. | [optional]
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional]
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional]
 **opt_fields** | **[str]**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional]

### Return type

[**GetAuditLogEvents200Response**](GetAuditLogEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AuditLogEvents were successfully retrieved. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

