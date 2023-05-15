# BatchResponse

A response object returned from a batch request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The HTTP status code that the invoked endpoint returned. | [optional] 
**headers** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A map of HTTP headers specific to this result. This is primarily used for returning a &#x60;Location&#x60; header to accompany a &#x60;201 Created&#x60; result.  The parent HTTP response will contain all common headers. | [optional] 
**body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The JSON body that the invoked endpoint returned. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


