# ProjectBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**archived** | **bool** | True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries. | [optional] 
**color** | **str, none_type** | Color of the project. | [optional] 
**created_at** | **datetime** | The time at which this project was created. | [optional] [readonly] 
**current_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | *Deprecated: new integrations should prefer the &#x60;current_status_update&#x60; resource.* | [optional] 
**current_status_update** | **bool, date, datetime, dict, float, int, list, str, none_type** | The latest &#x60;status_update&#x60; posted to this project. | [optional] 
**custom_field_settings** | [**[CustomFieldSettingResponse]**](CustomFieldSettingResponse.md) | Array of Custom Field Settings (in compact form). | [optional] [readonly] 
**default_view** | **str** | The default view (list, board, calendar, or timeline) of a project. | [optional] 
**due_date** | **date, none_type** | *Deprecated: new integrations should prefer the &#x60;due_on&#x60; field.* | [optional] 
**due_on** | **date, none_type** | The day on which this project is due. This takes a date with format YYYY-MM-DD. | [optional] 
**html_notes** | **str** | [Opt In](/docs/inputoutput-options). The notes of the project with formatting as HTML. | [optional] 
**members** | [**[UserCompact]**](UserCompact.md) | Array of users who are members of this project. | [optional] [readonly] 
**modified_at** | **datetime** | The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.* | [optional] [readonly] 
**notes** | **str** | Free-form textual information associated with the project (ie., its description). | [optional] 
**public** | **bool** | True if the project is public to its team. | [optional] 
**start_on** | **date, none_type** | The day on which work for this project begins, or null if the project has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**workspace** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


