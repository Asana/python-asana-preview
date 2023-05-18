# TeamMembershipCompact

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. This object represents a user's connection to a team.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**user** | [**CustomFieldResponsePeopleValueInner**](CustomFieldResponsePeopleValueInner.md) |  | [optional] 
**team** | [**GoalResponseTeamAllOf**](GoalResponseTeamAllOf.md) |  | [optional] 
**is_guest** | **bool** | Describes if the user is a guest in the team. | [optional] 
**is_limited_access** | **bool** | Describes if the user has limited access to the team. | [optional] 
**is_admin** | **bool** | Describes if the user is a team admin. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


