# BatchRequestAction

An action object for use in a batch request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relative_path** | **str** | The path of the desired endpoint relative to the API’s base URL. Query parameters are not accepted here; put them in &#x60;data&#x60; instead. | 
**method** | **str** | The HTTP method you wish to emulate for the action. | 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | For &#x60;GET&#x60; requests, this should be a map of query parameters you would have normally passed in the URL. Options and pagination are not accepted here; put them in &#x60;options&#x60; instead. For &#x60;POST&#x60;, &#x60;PATCH&#x60;, and &#x60;PUT&#x60; methods, this should be the content you would have normally put in the data field of the body. | [optional] 
**options** | [**BatchRequestActionOptions**](BatchRequestActionOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


