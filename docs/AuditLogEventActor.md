# AuditLogEventActor

The entity that triggered the event. Will typically be a user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_type** | **str** | The type of actor. Can be one of &#x60;user&#x60;, &#x60;asana&#x60;, &#x60;asana_support&#x60;, &#x60;anonymous&#x60;, or &#x60;external_administrator&#x60;. | [optional] 
**gid** | **str** | Globally unique identifier of the actor, if it is a user. | [optional] 
**name** | **str** | The name of the actor, if it is a user. | [optional] 
**email** | **str** | The email of the actor, if it is a user. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


