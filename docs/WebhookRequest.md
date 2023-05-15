# WebhookRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | A resource ID to subscribe to. Many Asana resources are valid to create webhooks on, but higher-level resources require filters. | 
**target** | **str** | The URL to receive the HTTP POST. The full URL will be used to deliver events from this webhook (including parameters) which allows encoding of application-specific state when the webhook is created. | 
**filters** | [**[WebhookRequestFiltersInner]**](WebhookRequestFiltersInner.md) | An array of WebhookFilter objects to specify a whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


