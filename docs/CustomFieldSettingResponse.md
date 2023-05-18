# CustomFieldSettingResponse

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. Custom Fields Settings objects represent the many-to-many join of the Custom Field and Project as well as stores information that is relevant to that particular pairing.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**project** | [**CustomFieldSettingResponseProject**](CustomFieldSettingResponseProject.md) |  | [optional] 
**is_important** | **bool** | &#x60;is_important&#x60; is used in the Asana web application to determine if this custom field is displayed in the list/grid view of a project or portfolio. | [optional] [readonly] 
**parent** | [**CustomFieldSettingResponseParent**](CustomFieldSettingResponseParent.md) |  | [optional] 
**custom_field** | [**CustomFieldSettingResponseCustomField**](CustomFieldSettingResponseCustomField.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


