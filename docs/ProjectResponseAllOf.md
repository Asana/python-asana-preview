# ProjectResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**[CustomFieldCompact]**](CustomFieldCompact.md) | Array of Custom Fields. | [optional] [readonly] 
**completed** | **bool** | True if the project is currently marked complete, false if not. | [optional] [readonly] 
**completed_at** | **datetime, none_type** | The time at which this project was completed, or null if the project is not completed. | [optional] [readonly] 
**completed_by** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user that marked this project complete, or null if the project is not completed. | [optional] [readonly] 
**followers** | [**[UserCompact]**](UserCompact.md) | Array of users following this project. Followers are a subset of members who have opted in to receive \&quot;tasks added\&quot; notifications for a project. | [optional] [readonly] 
**owner** | **bool, date, datetime, dict, float, int, list, str, none_type** | The current owner of the project, may be null. | [optional] 
**team** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**icon** | **str, none_type** | The icon for a project. | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] [readonly] 
**project_brief** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**created_from_template** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


