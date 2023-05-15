# WorkspaceMembershipResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**workspace** | [**WorkspaceCompact**](WorkspaceCompact.md) |  | [optional] 
**user_task_list** | [**UserTaskListCompact**](UserTaskListCompact.md) |  | [optional] 
**is_active** | **bool** | Reflects if this user still a member of the workspace. | [optional] [readonly] 
**is_admin** | **bool** | Reflects if this user is an admin of the workspace. | [optional] [readonly] 
**is_guest** | **bool** | Reflects if this user is a guest of the workspace. | [optional] [readonly] 
**vacation_dates** | [**WorkspaceMembershipResponseAllOfVacationDates**](WorkspaceMembershipResponseAllOfVacationDates.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


