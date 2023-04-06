# CustomFieldCompactAllOfDateValue

*Conditional*. Only relevant for custom fields of type `date`. This object reflects the chosen date (and optionally, time) value of a `date` custom field. If no date is selected, the value of `date_value` will be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | A string representing the date in YYYY-MM-DD format. | [optional] 
**date_time** | **str** | A string representing the date in ISO 8601 format. If no time value is selected, the value of &#x60;date-time&#x60; will be &#x60;null&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


