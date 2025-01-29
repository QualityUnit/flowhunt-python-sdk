# flowhunt.FineTuningsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_ft**](FineTuningsApi.md#create_image_ft) | **POST** /v2/fine_tunings/images/ | Create Image Ft
[**delete_image_ft**](FineTuningsApi.md#delete_image_ft) | **DELETE** /v2/fine_tunings/images/{ft_id} | Delete Image Ft
[**handle_replicate_webhook**](FineTuningsApi.md#handle_replicate_webhook) | **POST** /v2/fine_tunings/webhooks/replicate | Handle Replicate Webhook
[**search_image_fts**](FineTuningsApi.md#search_image_fts) | **POST** /v2/fine_tunings/images/search | Search Image Fts
[**train_image_ft**](FineTuningsApi.md#train_image_ft) | **POST** /v2/fine_tunings/images/{ft_id}/train | Train Image Ft
[**update_image_ft**](FineTuningsApi.md#update_image_ft) | **PUT** /v2/fine_tunings/images/{ft_id} | Update Image Ft
[**upload_image_ft**](FineTuningsApi.md#upload_image_ft) | **POST** /v2/fine_tunings/images/{ft_id}/upload | Upload Image Ft


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

# **train_image_ft**
> ImageFTResponse train_image_ft(ft_id, workspace_id, image_ft_train_request)

Train Image Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.image_ft_response import ImageFTResponse
from flowhunt.models.image_ft_train_request import ImageFTTrainRequest
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
    image_ft_train_request = flowhunt.ImageFTTrainRequest() # ImageFTTrainRequest | 

    try:
        # Train Image Ft
        api_response = api_instance.train_image_ft(ft_id, workspace_id, image_ft_train_request)
        print("The response of FineTuningsApi->train_image_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->train_image_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ft_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **image_ft_train_request** | [**ImageFTTrainRequest**](ImageFTTrainRequest.md)|  | 

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
> ImageFTResponse upload_image_ft(ft_id, workspace_id, file)

Upload Image Ft

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
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
    ft_id = 'ft_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload Image Ft
        api_response = api_instance.upload_image_ft(ft_id, workspace_id, file)
        print("The response of FineTuningsApi->upload_image_ft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningsApi->upload_image_ft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ft_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**ImageFTResponse**](ImageFTResponse.md)

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

