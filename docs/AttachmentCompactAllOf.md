# AttachmentCompactAllOf

An *attachment* object represents any file attached to a task in Asana, whether it’s an uploaded file or one associated via a third-party service such as Dropbox or Google Drive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file. | [optional] [readonly] 
**resource_subtype** | **str** | The service hosting the attachment. Valid values are &#x60;asana&#x60;, &#x60;dropbox&#x60;, &#x60;gdrive&#x60;, &#x60;onedrive&#x60;, &#x60;box&#x60;, &#x60;vimeo&#x60;, and &#x60;external&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


