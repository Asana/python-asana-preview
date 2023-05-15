# AuditLogEvent

An object representing a single event within an Asana domain.  Every audit log event is comprised of an `event_type`, `actor`, `resource`, and `context`. Some events will include additional metadata about the event under `details`. See our [currently supported list of events](/docs/audit-log-events#supported-audit-log-events) for more details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the &#x60;AuditLogEvent&#x60;, as a string. | [optional] 
**created_at** | **datetime** | The time the event was created. | [optional] 
**event_type** | **str** | The type of the event. | [optional] 
**event_category** | **str** | The category that this &#x60;event_type&#x60; belongs to. | [optional] 
**actor** | [**AuditLogEventActor**](AuditLogEventActor.md) |  | [optional] 
**resource** | [**AuditLogEventResource**](AuditLogEventResource.md) |  | [optional] 
**details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Event specific details. The schema will vary depending on the &#x60;event_type&#x60;. | [optional] 
**context** | [**AuditLogEventContext**](AuditLogEventContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


