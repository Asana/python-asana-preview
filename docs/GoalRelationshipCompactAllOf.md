# GoalRelationshipCompactAllOf

A *goal relationship* is an object representing the relationship between a goal and another goal, a project, or a portfolio.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**supporting_resource** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#39;s progress contributes to the supported goal&#39;s progress. This can only be 0 or 1. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

