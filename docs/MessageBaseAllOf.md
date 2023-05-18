# MessageBaseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**modified_at** | **bool, date, datetime, dict, float, int, list, str, none_type** | The time at which this message was last modified. | [optional] 
**title** | **str** | The title of the message. | [optional] 
**text** | **str** | The text content of the message. | [optional] 
**num_likes** | **int** | The number of users who have liked this message. | [optional] [readonly] 
**likes** | [**[GoalResponseLikesInner]**](GoalResponseLikesInner.md) | Array of likes for users who have liked this message. | [optional] [readonly] 
**followers** | [**[CustomFieldResponsePeopleValueInner]**](CustomFieldResponsePeopleValueInner.md) | Array of users this message was sent to. | [optional] [readonly] 
**parents** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | The parents of this message. This is an array of the containers the message was sent to. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


