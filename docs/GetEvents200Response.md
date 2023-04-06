# GetEvents200Response

The full record for all events that have occurred since the sync token was created.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[EventResponse]**](EventResponse.md) |  | [optional] 
**sync** | **str** | A sync token to be used with the next call to the /events endpoint. | [optional] 
**has_more** | **bool** | Indicates whether there are more events to pull. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


