# ProjectDuplicateRequestScheduleDates

A dictionary of options to auto-shift dates. `task_dates` must be included to use this option. Requires either `start_on` or `due_on`, but not both.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_skip_weekends** | **bool** | Determines if the auto-shifted dates should skip weekends. | 
**due_on** | **str** | Sets the last due date in the duplicated project to the given date. The rest of the due dates will be offset by the same amount as the due dates in the original project. | [optional] 
**start_on** | **str** | Sets the first start date in the duplicated project to the given date. The rest of the start dates will be offset by the same amount as the start dates in the original project. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


