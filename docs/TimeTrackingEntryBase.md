# TimeTrackingEntryBase

A generic Asana Resource, containing a globally unique identifier.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**duration_minutes** | **int** | Time in minutes tracked by the entry. | [optional] 
**entered_on** | **date** | The day that this entry is logged on. | [optional] 
**created_by** | [**StoryResponseAssignee**](StoryResponseAssignee.md) |  | [optional] 
**task** | [**StoryResponseTask**](StoryResponseTask.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


