# flowhunt.FineTuningsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_ft**](FineTuningsApi.md#create_image_ft) | **POST** /v2/fine_tunings/images/ | Create Image Ft
[**delete_file_ft**](FineTuningsApi.md#delete_file_ft) | **DELETE** /v2/fine_tunings/files/{file_key} | Delete File Ft
[**delete_image_ft**](FineTuningsApi.md#delete_image_ft) | **DELETE** /v2/fine_tunings/images/{ft_id} | Delete Image Ft
[**generate_images**](FineTuningsApi.md#generate_images) | **POST** /v2/fine_tunings/inference/images | Generate Images
[**get_file_ft**](FineTuningsApi.md#get_file_ft) | **GET** /v2/fine_tunings/files/{file_key} | Get File Ft
[**get_inference_results**](FineTuningsApi.md#get_inference_results) | **GET** /v2/fine_tunings/inference/results/{inference_id} | Get Inference Results
[**handle_replicate_webhook**](FineTuningsApi.md#handle_replicate_webhook) | **POST** /v2/fine_tunings/webhooks/replicate | Handle Replicate Webhook
[**search_image_fts**](FineTuningsApi.md#search_image_fts) | **POST** /v2/fine_tunings/images/search | Search Image Fts
[**search_inference_history**](FineTuningsApi.md#search_inference_history) | **POST** /v2/fine_tunings/inference/history | Search Inference History
[**update_image_ft**](FineTuningsApi.md#update_image_ft) | **PUT** /v2/fine_tunings/images/{ft_id} | Update Image Ft
[**upload_image_ft**](FineTuningsApi.md#upload_image_ft) | **POST** /v2/fine_tunings/files/{ft_type}/upload | Upload Image Ft


# **create_image_ft**
> ImageFTResponse create_image_ft(workspace_id, image_ft_create_request)

Create Image Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_ft_create_request import ImageFTCreateRequest
from flowhunt.models.image_ft_response import ImageFTResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    image_ft_create_request = flowhunt.ImageFTCreateRequest() # ImageFTCreateRequest | 

    try:
        # Create Image Ft
        api_response = api_instance.create_image_ft(workspace_id, image_ft_create_request)
        print("The response of FineTuningsApi->create_image_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->create_image_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **image_ft_create_request** | [**ImageFTCreateRequest**](ImageFTCreateRequest.md)|  | 

### Return type

[**ImageFTResponse**](ImageFTResponse.md)

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

# **delete_file_ft**
> object delete_file_ft(file_key, workspace_id, file_type)

Delete File Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.inference_file_type import InferenceFileType
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    file_key = 'file_key_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file_type = flowhunt.InferenceFileType() # InferenceFileType | 

    try:
        # Delete File Ft
        api_response = api_instance.delete_file_ft(file_key, workspace_id, file_type)
        print("The response of FineTuningsApi->delete_file_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->delete_file_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_key** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file_type** | [**InferenceFileType**](.md)|  | 

### Return type

**object**

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

# **delete_image_ft**
> Completed delete_image_ft(ft_id, workspace_id)

Delete Image Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    ft_id = 'ft_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Image Ft
        api_response = api_instance.delete_image_ft(ft_id, workspace_id)
        print("The response of FineTuningsApi->delete_image_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->delete_image_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ft_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **generate_images**
> ImageInferenceScheduleResponse generate_images(workspace_id, image_inference_request)

Generate Images

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_inference_request import ImageInferenceRequest
from flowhunt.models.image_inference_schedule_response import ImageInferenceScheduleResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    image_inference_request = flowhunt.ImageInferenceRequest() # ImageInferenceRequest | 

    try:
        # Generate Images
        api_response = api_instance.generate_images(workspace_id, image_inference_request)
        print("The response of FineTuningsApi->generate_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->generate_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **image_inference_request** | [**ImageInferenceRequest**](ImageInferenceRequest.md)|  | 

### Return type

[**ImageInferenceScheduleResponse**](ImageInferenceScheduleResponse.md)

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

# **get_file_ft**
> object get_file_ft(file_key, workspace_id, file_type)

Get File Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.inference_file_type import InferenceFileType
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    file_key = 'file_key_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file_type = flowhunt.InferenceFileType() # InferenceFileType | 

    try:
        # Get File Ft
        api_response = api_instance.get_file_ft(file_key, workspace_id, file_type)
        print("The response of FineTuningsApi->get_file_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->get_file_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_key** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file_type** | [**InferenceFileType**](.md)|  | 

### Return type

**object**

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

# **get_inference_results**
> ImageInferenceResultResponse get_inference_results(inference_id, workspace_id)

Get Inference Results

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_inference_result_response import ImageInferenceResultResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    inference_id = 'inference_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Inference Results
        api_response = api_instance.get_inference_results(inference_id, workspace_id)
        print("The response of FineTuningsApi->get_inference_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->get_inference_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inference_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ImageInferenceResultResponse**](ImageInferenceResultResponse.md)

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

# **handle_replicate_webhook**
> Completed handle_replicate_webhook(workspace_id, ft_id)

Handle Replicate Webhook

### Example


```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.FineTuningsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    ft_id = 'ft_id_example' # str | 

    try:
        # Handle Replicate Webhook
        api_response = api_instance.handle_replicate_webhook(workspace_id, ft_id)
        print("The response of FineTuningsApi->handle_replicate_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->handle_replicate_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **ft_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **search_image_fts**
> List[ImageFTResponse] search_image_fts(workspace_id, image_ft_search_request)

Search Image Fts

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_ft_response import ImageFTResponse
from flowhunt.models.image_ft_search_request import ImageFTSearchRequest
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    image_ft_search_request = flowhunt.ImageFTSearchRequest() # ImageFTSearchRequest | 

    try:
        # Search Image Fts
        api_response = api_instance.search_image_fts(workspace_id, image_ft_search_request)
        print("The response of FineTuningsApi->search_image_fts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->search_image_fts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **image_ft_search_request** | [**ImageFTSearchRequest**](ImageFTSearchRequest.md)|  | 

### Return type

[**List[ImageFTResponse]**](ImageFTResponse.md)

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

# **search_inference_history**
> List[ImageInferenceResponse] search_inference_history(workspace_id, inference_history_search_request)

Search Inference History

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_inference_response import ImageInferenceResponse
from flowhunt.models.inference_history_search_request import InferenceHistorySearchRequest
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    inference_history_search_request = flowhunt.InferenceHistorySearchRequest() # InferenceHistorySearchRequest | 

    try:
        # Search Inference History
        api_response = api_instance.search_inference_history(workspace_id, inference_history_search_request)
        print("The response of FineTuningsApi->search_inference_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->search_inference_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **inference_history_search_request** | [**InferenceHistorySearchRequest**](InferenceHistorySearchRequest.md)|  | 

### Return type

[**List[ImageInferenceResponse]**](ImageInferenceResponse.md)

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

# **update_image_ft**
> ImageFTResponse update_image_ft(ft_id, workspace_id, image_ft_update_request)

Update Image Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_ft_response import ImageFTResponse
from flowhunt.models.image_ft_update_request import ImageFTUpdateRequest
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    ft_id = 'ft_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    image_ft_update_request = flowhunt.ImageFTUpdateRequest() # ImageFTUpdateRequest | 

    try:
        # Update Image Ft
        api_response = api_instance.update_image_ft(ft_id, workspace_id, image_ft_update_request)
        print("The response of FineTuningsApi->update_image_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->update_image_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ft_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **image_ft_update_request** | [**ImageFTUpdateRequest**](ImageFTUpdateRequest.md)|  | 

### Return type

[**ImageFTResponse**](ImageFTResponse.md)

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

# **upload_image_ft**
> FileUploadResponse upload_image_ft(ft_type, workspace_id, file)

Upload Image Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.ft_type import FTType
from flowhunt.models.file_upload_response import FileUploadResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FineTuningsApi(api_client)
    ft_type = flowhunt.FTType() # FTType | 
    workspace_id = 'workspace_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload Image Ft
        api_response = api_instance.upload_image_ft(ft_type, workspace_id, file)
        print("The response of FineTuningsApi->upload_image_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->upload_image_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ft_type** | [**FTType**](.md)|  | 
 **workspace_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

