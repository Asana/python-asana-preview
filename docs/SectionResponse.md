# SectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the section (i.e. the text displayed as the section header). | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**projects** | [**[ProjectCompact]**](ProjectCompact.md) | *Deprecated - please use project instead* | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


