# MembershipResponseAnyOf

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. With the introduction of “comment-only” projects in Asana, a user’s membership in a project comes with associated permissions. These permissions (whether a user has full access to the project or comment-only access) are accessible through the project memberships endpoints described here.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | Type of the membership. | [optional] 
**user** | [**CustomFieldResponsePeopleValueInner**](CustomFieldResponsePeopleValueInner.md) |  | [optional] 
**project** | [**JobBaseNewProject**](JobBaseNewProject.md) |  | [optional] 
**member** | [**ProjectMembershipResponseMember**](ProjectMembershipResponseMember.md) |  | [optional] 
**write_access** | **str** | Whether the member has full access, edit access, or comment-only access to the project. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


