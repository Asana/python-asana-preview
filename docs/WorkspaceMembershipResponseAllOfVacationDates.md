# WorkspaceMembershipResponseAllOfVacationDates

Contains keys `start_on` and `end_on` for the vacation dates for the user in this workspace. If `start_on` is null, the entire `vacation_dates` object will be null. If `end_on` is before today, the entire `vacation_dates` object will be null.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **str** | The day on which the user&#39;s vacation in this workspace starts. This is a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**end_on** | **str, none_type** | The day on which the user&#39;s vacation in this workspace ends, or null if there is no end date. This is a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


