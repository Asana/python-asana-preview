# ProjectTemplateBase

A generic Asana Resource, containing a globally unique identifier.A generic Asana Resource, containing a globally unique identifier. A *project template* is an object that allows new projects to be created with a predefined setup, which may include tasks, sections, Rules, etc. It simplifies the process of running a workflow that involves a similar set of work every time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project template. | [optional] 
**description** | **str** | Free-form textual information associated with the project template | [optional] 
**html_description** | **str** | The description of the project template with formatting as HTML. | [optional] 
**public** | **bool** | True if the project template is public to its team. | [optional] 
**owner** | [**ProjectTemplateBaseOwner**](ProjectTemplateBaseOwner.md) |  | [optional] 
**team** | [**GoalResponseTeamAllOf**](GoalResponseTeamAllOf.md) |  | [optional] 
**requested_dates** | [**[ProjectTemplateBaseRequestedDatesInner]**](ProjectTemplateBaseRequestedDatesInner.md) | Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project. | [optional] [readonly] 
**color** | **str, none_type** | Color of the project template. | [optional] 
**requested_roles** | [**[ProjectTemplateBaseRequestedRolesInner]**](ProjectTemplateBaseRequestedRolesInner.md) | Array of template roles in this project template. User Ids can be provided for these variables when instantiating a project to assign template tasks to the user. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


