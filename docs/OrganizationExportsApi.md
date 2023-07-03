# asana_preview.OrganizationExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_export**](OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
[**get_organization_export**](OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request

# **create_organization_export**
> OrganizationExportResponseData create_organization_export(body, limit=limit, offset=offset, opt_fields=opt_fields)

Create an organization export request

This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.OrganizationExportsApi(asana_preview.ApiClient(configuration))
body = asana_preview.OrganizationExportsBody() # OrganizationExportsBody | The organization to export.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ['[\"created_at\",\"download_url\",\"organization\",\"organization.name\",\"state\"]'] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create an organization export request
    api_response = api_instance.create_organization_export(body, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationExportsApi->create_organization_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationExportsBody**](OrganizationExportsBody.md)| The organization to export. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**OrganizationExportResponseData**](OrganizationExportResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_export**
> OrganizationExportResponseData get_organization_export(organization_export_gid, opt_fields=opt_fields)

Get details on an org export request

Returns details of a previously-requested Organization export.

### Example
```python
from __future__ import print_function
import time
import asana_preview
from asana_preview.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana_preview.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asana_preview.OrganizationExportsApi(asana_preview.ApiClient(configuration))
organization_export_gid = '12345' # str | Globally unique identifier for the organization export.
opt_fields = ['[\"created_at\",\"download_url\",\"organization\",\"organization.name\",\"state\"]'] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get details on an org export request
    api_response = api_instance.get_organization_export(organization_export_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationExportsApi->get_organization_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_export_gid** | **str**| Globally unique identifier for the organization export. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**OrganizationExportResponseData**](OrganizationExportResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

