# UserBaseResponse

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. A *user* object represents an account in Asana that can be given access to various workspaces, projects, and tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] [readonly] 
**photo** | [**UserBaseResponsePhoto**](UserBaseResponsePhoto.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


