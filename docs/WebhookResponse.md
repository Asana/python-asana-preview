# WebhookResponse

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. Webhook objects represent the state of an active subscription for a server to be updated with information from Asana. This schema represents the subscription itself, not the objects that are sent to the server. For information on those please refer to the [event](/reference/events) schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**active** | **bool** | If true, the webhook will send events - if false it is considered inactive and will not generate events. | [optional] [readonly] 
**resource** | [**MessageParentAllOf**](MessageParentAllOf.md) |  | [optional] 
**target** | **str** | The URL to receive the HTTP POST. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**last_failure_at** | **datetime** | The timestamp when the webhook last received an error when sending an event to the target. | [optional] [readonly] 
**last_failure_content** | **str** | The contents of the last error response sent to the webhook when attempting to deliver events to the target. | [optional] [readonly] 
**last_success_at** | **datetime** | The timestamp when the webhook last successfully sent an event to the target. | [optional] [readonly] 
**filters** | [**[WebhookRequestFiltersInner]**](WebhookRequestFiltersInner.md) | Whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


