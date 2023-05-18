# GoalRelationshipRequest

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. A *goal relationship* is an object representing the relationship between a goal and another goal, a project, or a portfolio.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**supporting_resource** | [**GoalRelationshipBaseSupportingResource**](GoalRelationshipBaseSupportingResource.md) |  | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#39;s progress contributes to the supported goal&#39;s progress. This can only be 0 or 1. | [optional] 
**supported_goal** | [**GoalRelationshipBaseSupportedGoal**](GoalRelationshipBaseSupportedGoal.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


