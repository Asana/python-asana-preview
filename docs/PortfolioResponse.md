# PortfolioResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the portfolio. | [optional] 
**color** | **str** | Color of the portfolio. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 
**custom_field_settings** | [**[CustomFieldSettingResponse]**](CustomFieldSettingResponse.md) | Array of custom field settings applied to the portfolio. | [optional] 
**current_status_update** | **bool, date, datetime, dict, float, int, list, str, none_type** | The latest &#x60;status_update&#x60; posted to this portfolio. | [optional] 
**due_on** | **datetime, none_type** | The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD. | [optional] 
**custom_fields** | [**[CustomFieldCompact]**](CustomFieldCompact.md) | Array of Custom Fields. | [optional] 
**members** | [**[UserCompact]**](UserCompact.md) |  | [optional] [readonly] 
**owner** | [**UserCompact**](UserCompact.md) |  | [optional] 
**start_on** | **date, none_type** | The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**workspace** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] [readonly] 
**public** | **bool** | True if the portfolio is public to its workspace members. | [optional] 
**project_templates** | [**[ProjectTemplateCompact]**](ProjectTemplateCompact.md) | Array of project templates that are in the portfolio | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


