# MembershipResponseAnyOf4UserTaskList

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. A user task list represents the tasks assigned to a particular user. It provides API access to a user’s [My Tasks](https://asana.com/guide/help/fundamentals/my-tasks) view in Asana.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the user task list. | [optional] 
**owner** | **bool, date, datetime, dict, float, int, list, str, none_type** | The owner of the user task list, i.e. the person whose My Tasks is represented by this resource. | [optional] [readonly] 
**workspace** | **bool, date, datetime, dict, float, int, list, str, none_type** | The workspace in which the user task list is located. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


