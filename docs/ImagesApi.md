# flowhunt.ImagesApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_image**](ImagesApi.md#convert_image) | **POST** /v2/images/convert | Convert Image
[**get_screenshot**](ImagesApi.md#get_screenshot) | **POST** /v2/images/screenshot | Get Screenshot
[**optimize_image**](ImagesApi.md#optimize_image) | **POST** /v2/images/optimize | Optimize Image


# **convert_image**
> TaskResponse convert_image(workspace_id, image_convert_request)

Convert Image

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_convert_request import ImageConvertRequest
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.ImagesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    image_convert_request = flowhunt.ImageConvertRequest() # ImageConvertRequest | 

    try:
        # Convert Image
        api_response = api_instance.convert_image(workspace_id, image_convert_request)
        print("The response of ImagesApi->convert_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->convert_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **image_convert_request** | [**ImageConvertRequest**](ImageConvertRequest.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **get_screenshot**
> ScreenshotResponse get_screenshot(workspace_id, screenshot_request)

Get Screenshot

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.screenshot_request import ScreenshotRequest
from flowhunt.models.screenshot_response import ScreenshotResponse
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
    api_instance = flowhunt.ImagesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    screenshot_request = flowhunt.ScreenshotRequest() # ScreenshotRequest | 

    try:
        # Get Screenshot
        api_response = api_instance.get_screenshot(workspace_id, screenshot_request)
        print("The response of ImagesApi->get_screenshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_screenshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **screenshot_request** | [**ScreenshotRequest**](ScreenshotRequest.md)|  | 

### Return type

[**ScreenshotResponse**](ScreenshotResponse.md)

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

# **optimize_image**
> TaskResponse optimize_image(workspace_id, image_optimize_request)

Optimize Image

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_optimize_request import ImageOptimizeRequest
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.ImagesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    image_optimize_request = flowhunt.ImageOptimizeRequest() # ImageOptimizeRequest | 

    try:
        # Optimize Image
        api_response = api_instance.optimize_image(workspace_id, image_optimize_request)
        print("The response of ImagesApi->optimize_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->optimize_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **image_optimize_request** | [**ImageOptimizeRequest**](ImageOptimizeRequest.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

