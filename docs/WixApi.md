# flowhunt.WixApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_members**](WixApi.md#get_members) | **GET** /v2/integrations/wix/members | Get Members


# **get_members**
> WixMembersResponse get_members(workspace_id)

Get Members

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.wix_members_response import WixMembersResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WixApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Members
        api_response = api_instance.get_members(workspace_id)
        print("The response of WixApi->get_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WixApi->get_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WixMembersResponse**](WixMembersResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

