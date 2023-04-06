# EventResponseChange

Information about the type of change that has occurred. This field is only present when the value of the property `action`, describing the action taken on the **resource**, is `changed`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The name of the field that has changed in the resource. | [optional] [readonly] 
**action** | **str** | The type of action taken on the **field** which has been changed.  This can be one of &#x60;changed&#x60;, &#x60;added&#x60;, or &#x60;removed&#x60; depending on the nature of the change. | [optional] [readonly] 
**new_value** | **bool, date, datetime, dict, float, int, list, str, none_type** | *Conditional.* This property is only present when the **field&#39;s** &#x60;action&#x60; is &#x60;changed&#x60; _and_ the &#x60;new_value&#x60; is an Asana resource. This will be only the &#x60;gid&#x60; and &#x60;resource_type&#x60; of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](/docs/inputoutput-options)) when using the [get events](/reference/getevents) endpoint. | [optional] 
**added_value** | **bool, date, datetime, dict, float, int, list, str, none_type** | *Conditional.* This property is only present when the **field&#39;s** &#x60;action&#x60; is &#x60;added&#x60; _and_ the &#x60;added_value&#x60; is an Asana resource. This will be only the &#x60;gid&#x60; and &#x60;resource_type&#x60; of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](/docs/inputoutput-options)) when using the [get events](/reference/getevents) endpoint. | [optional] 
**removed_value** | **bool, date, datetime, dict, float, int, list, str, none_type** | *Conditional.* This property is only present when the **field&#39;s** &#x60;action&#x60; is &#x60;removed&#x60; _and_ the &#x60;removed_value&#x60; is an Asana resource. This will be only the &#x60;gid&#x60; and &#x60;resource_type&#x60; of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](/docs/inputoutput-options)) when using the [get events](/reference/getevents) endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


