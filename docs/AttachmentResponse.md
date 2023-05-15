# AttachmentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the file. | [optional] [readonly] 
**resource_subtype** | **str** | The service hosting the attachment. Valid values are &#x60;asana&#x60;, &#x60;dropbox&#x60;, &#x60;gdrive&#x60;, &#x60;onedrive&#x60;, &#x60;box&#x60;, &#x60;vimeo&#x60;, and &#x60;external&#x60;. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**download_url** | **str, none_type** | The URL containing the content of the attachment. *Note:* May be null if the attachment is hosted by [Box](https://www.box.com/) and will be null if the attachment is a Video Message hosted by [Vimeo](https://vimeo.com/). If present, this URL may only be valid for two minutes from the time of retrieval. You should avoid persisting this URL somewhere and just refresh it on demand to ensure you do not keep stale URLs. | [optional] [readonly] 
**permanent_url** | **str, none_type** |  | [optional] [readonly] 
**host** | **str** | The service hosting the attachment. Valid values are &#x60;asana&#x60;, &#x60;dropbox&#x60;, &#x60;gdrive&#x60;, &#x60;box&#x60;, and &#x60;vimeo&#x60;. | [optional] [readonly] 
**parent** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**size** | **int** | The size of the attachment in bytes. Only present when the &#x60;resource_subtype&#x60; is &#x60;asana&#x60;. | [optional] [readonly] 
**view_url** | **str, none_type** | The URL where the attachment can be viewed, which may be friendlier to users in a browser than just directing them to a raw file. May be null if no view URL exists for the service. | [optional] [readonly] 
**connected_to_app** | **bool** | Whether the attachment is connected to the app making the request for the purposes of showing an app components widget. Only present when the &#x60;resource_subtype&#x60; is &#x60;external&#x60; or &#x60;gdrive&#x60;. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


