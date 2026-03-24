# flowhunt.DefaultApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_branding**](DefaultApi.md#get_branding) | **GET** /v2/settings/branding | Get Branding
[**get_public_branding**](DefaultApi.md#get_public_branding) | **GET** /v2/settings/branding/public | Get Public Branding
[**update_branding**](DefaultApi.md#update_branding) | **PUT** /v2/settings/branding | Update Branding


# **get_branding**
> BrandingResponse get_branding(workspace_id)

Get Branding

Get dashboard branding settings for the workspace.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.branding_response import BrandingResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.DefaultApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Branding
        api_response = api_instance.get_branding(workspace_id)
        print("The response of DefaultApi->get_branding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_branding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**BrandingResponse**](BrandingResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_branding**
> BrandingResponse get_public_branding(slug)

Get Public Branding

Get branding by slug (public, no auth required).

### Example


```python
import flowhunt
from flowhunt.models.branding_response import BrandingResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.DefaultApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Get Public Branding
        api_response = api_instance.get_public_branding(slug)
        print("The response of DefaultApi->get_public_branding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_public_branding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**BrandingResponse**](BrandingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_branding**
> BrandingResponse update_branding(workspace_id, branding_update_request)

Update Branding

Update dashboard branding settings. Requires white-label addon.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.branding_response import BrandingResponse
from flowhunt.models.branding_update_request import BrandingUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.DefaultApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    branding_update_request = flowhunt.BrandingUpdateRequest() # BrandingUpdateRequest | 

    try:
        # Update Branding
        api_response = api_instance.update_branding(workspace_id, branding_update_request)
        print("The response of DefaultApi->update_branding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_branding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **branding_update_request** | [**BrandingUpdateRequest**](BrandingUpdateRequest.md)|  | 

### Return type

[**BrandingResponse**](BrandingResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

