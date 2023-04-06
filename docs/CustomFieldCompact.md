# CustomFieldCompact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**name** | **str** | The name of the custom field. | [optional] 
**resource_subtype** | **str** | The type of the custom field. Must be one of the given values. | [optional] 
**type** | **str** | *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values. | [optional] [readonly] 
**enum_options** | [**[EnumOption]**](EnumOption.md) | *Conditional*. Only relevant for custom fields of type &#x60;enum&#x60;. This array specifies the possible values which an &#x60;enum&#x60; custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield). | [optional] 
**enabled** | **bool** | *Conditional*. Determines if the custom field is enabled or not. | [optional] 
**date_value** | [**CustomFieldCompactAllOfDateValue**](CustomFieldCompactAllOfDateValue.md) |  | [optional] 
**enum_value** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**multi_enum_values** | [**[EnumOption]**](EnumOption.md) | *Conditional*. Only relevant for custom fields of type &#x60;multi_enum&#x60;. This object is the chosen values of a &#x60;multi_enum&#x60; custom field. | [optional] 
**number_value** | **float** | *Conditional*. This number is the value of a &#x60;number&#x60; custom field. | [optional] 
**text_value** | **str** | *Conditional*. This string is the value of a &#x60;text&#x60; custom field. | [optional] 
**display_value** | **str, none_type** | A string representation for the value of the custom field. Integrations that don&#39;t require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


