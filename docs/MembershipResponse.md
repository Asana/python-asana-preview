# MembershipResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**user** | [**CustomFieldResponsePeopleValueInner**](CustomFieldResponsePeopleValueInner.md) |  | [optional] 
**project** | [**JobBaseNewProject**](JobBaseNewProject.md) |  | [optional] 
**member** | [**ProjectMembershipResponseMember**](ProjectMembershipResponseMember.md) |  | [optional] 
**write_access** | **str** | Whether the member has full access, edit access, or comment-only access to the project. | [optional] [readonly] 
**portfolio** | [**PortfolioMembershipBasePortfolio**](PortfolioMembershipBasePortfolio.md) |  | [optional] 
**team** | [**GoalResponseTeamAllOf**](GoalResponseTeamAllOf.md) |  | [optional] 
**is_guest** | **bool** | Reflects if this user is a guest of the workspace. | [optional] [readonly] 
**is_limited_access** | **bool** | Describes if the user has limited access to the team. | [optional] 
**is_admin** | **bool** | Reflects if this user is an admin of the workspace. | [optional] [readonly] 
**goal** | [**GoalMembershipBaseGoal**](GoalMembershipBaseGoal.md) |  | [optional] 
**is_commenter** | **bool** | Describes if the member is comment only in goal. | [optional] 
**is_editor** | **bool** | Describes if the member is editor in goal. | [optional] 
**workspace** | [**GoalResponseWorkspace**](GoalResponseWorkspace.md) |  | [optional] 
**user_task_list** | [**MembershipResponseAnyOf4UserTaskList**](MembershipResponseAnyOf4UserTaskList.md) |  | [optional] 
**is_active** | **bool** | Reflects if this user still a member of the workspace. | [optional] [readonly] 
**vacation_dates** | [**WorkspaceMembershipResponseVacationDates**](WorkspaceMembershipResponseVacationDates.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


