# WebhookResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**last_failure_at** | **datetime** | The timestamp when the webhook last received an error when sending an event to the target. | [optional] [readonly] 
**last_failure_content** | **str** | The contents of the last error response sent to the webhook when attempting to deliver events to the target. | [optional] [readonly] 
**last_success_at** | **datetime** | The timestamp when the webhook last successfully sent an event to the target. | [optional] [readonly] 
**filters** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


