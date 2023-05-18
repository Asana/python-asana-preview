# CreateProjectFromAsanaTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**team** | **str** | *Create-only*. The team that this project is shared with. This field only exists for projects in organizations. | [optional] 
**workspace** | [**CreateProjectFromAsanaTemplateRequestAllOf1Workspace**](CreateProjectFromAsanaTemplateRequestAllOf1Workspace.md) |  | [optional] 
**project_template** | **str** | The string ID of the Asana-created template to create the project from. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


