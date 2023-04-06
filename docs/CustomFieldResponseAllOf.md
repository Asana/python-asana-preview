# CustomFieldResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**people_value** | [**[UserCompact]**](UserCompact.md) | *Conditional*. Only relevant for custom fields of type &#x60;people&#x60;. This array of [compact user](/reference/users) objects reflects the values of a &#x60;people&#x60; custom field. | [optional] [readonly] 
**is_global_to_workspace** | **bool** | This flag describes whether this custom field is available to every container in the workspace. Before project-specific custom fields, this field was always true. | [optional] [readonly] 
**asana_created_field** | **str, none_type** | *Conditional*. A unique identifier to associate this field with the template source of truth. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


