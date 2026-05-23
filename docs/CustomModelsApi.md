# flowhunt.CustomModelsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_custom_models**](CustomModelsApi.md#bulk_delete_custom_models) | **POST** /v2/custom-models/delete | Bulk Delete Custom Models
[**create_custom_model**](CustomModelsApi.md#create_custom_model) | **POST** /v2/custom-models/create | Create Custom Model
[**delete_custom_model**](CustomModelsApi.md#delete_custom_model) | **DELETE** /v2/custom-models/{custom_model_id} | Delete Custom Model
[**get_available_models**](CustomModelsApi.md#get_available_models) | **GET** /v2/custom-models/available | Get Available Models
[**list_ollama_models**](CustomModelsApi.md#list_ollama_models) | **POST** /v2/custom-models/list-ollama-models | List Ollama Models
[**search_custom_models**](CustomModelsApi.md#search_custom_models) | **POST** /v2/custom-models/search | Search Custom Models
[**update_custom_model**](CustomModelsApi.md#update_custom_model) | **PUT** /v2/custom-models/{custom_model_id} | Update Custom Model


# **bulk_delete_custom_models**
> Completed bulk_delete_custom_models(workspace_id, custom_model_bulk_delete_request)

Bulk Delete Custom Models

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.custom_model_bulk_delete_request import CustomModelBulkDeleteRequest
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    custom_model_bulk_delete_request = flowhunt.CustomModelBulkDeleteRequest() # CustomModelBulkDeleteRequest | 

    try:
        # Bulk Delete Custom Models
        api_response = api_instance.bulk_delete_custom_models(workspace_id, custom_model_bulk_delete_request)
        print("The response of CustomModelsApi->bulk_delete_custom_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->bulk_delete_custom_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **custom_model_bulk_delete_request** | [**CustomModelBulkDeleteRequest**](CustomModelBulkDeleteRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **create_custom_model**
> CustomModelResponse create_custom_model(workspace_id, custom_model_create_request)

Create Custom Model

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.custom_model_create_request import CustomModelCreateRequest
from flowhunt.models.custom_model_response import CustomModelResponse
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    custom_model_create_request = flowhunt.CustomModelCreateRequest() # CustomModelCreateRequest | 

    try:
        # Create Custom Model
        api_response = api_instance.create_custom_model(workspace_id, custom_model_create_request)
        print("The response of CustomModelsApi->create_custom_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->create_custom_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **custom_model_create_request** | [**CustomModelCreateRequest**](CustomModelCreateRequest.md)|  | 

### Return type

[**CustomModelResponse**](CustomModelResponse.md)

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

# **delete_custom_model**
> Completed delete_custom_model(custom_model_id, workspace_id)

Delete Custom Model

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    custom_model_id = 'custom_model_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Custom Model
        api_response = api_instance.delete_custom_model(custom_model_id, workspace_id)
        print("The response of CustomModelsApi->delete_custom_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->delete_custom_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_model_id** | **str**|  | 
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

# **get_available_models**
> AvailableModelsResponse get_available_models(workspace_id)

Get Available Models

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.available_models_response import AvailableModelsResponse
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Available Models
        api_response = api_instance.get_available_models(workspace_id)
        print("The response of CustomModelsApi->get_available_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->get_available_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**AvailableModelsResponse**](AvailableModelsResponse.md)

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

# **list_ollama_models**
> OllamaListModelsResponse list_ollama_models(workspace_id, ollama_list_models_request)

List Ollama Models

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.ollama_list_models_request import OllamaListModelsRequest
from flowhunt.models.ollama_list_models_response import OllamaListModelsResponse
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    ollama_list_models_request = flowhunt.OllamaListModelsRequest() # OllamaListModelsRequest | 

    try:
        # List Ollama Models
        api_response = api_instance.list_ollama_models(workspace_id, ollama_list_models_request)
        print("The response of CustomModelsApi->list_ollama_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->list_ollama_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **ollama_list_models_request** | [**OllamaListModelsRequest**](OllamaListModelsRequest.md)|  | 

### Return type

[**OllamaListModelsResponse**](OllamaListModelsResponse.md)

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

# **search_custom_models**
> List[CustomModelResponse] search_custom_models(workspace_id, custom_model_search_request)

Search Custom Models

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.custom_model_response import CustomModelResponse
from flowhunt.models.custom_model_search_request import CustomModelSearchRequest
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    custom_model_search_request = flowhunt.CustomModelSearchRequest() # CustomModelSearchRequest | 

    try:
        # Search Custom Models
        api_response = api_instance.search_custom_models(workspace_id, custom_model_search_request)
        print("The response of CustomModelsApi->search_custom_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->search_custom_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **custom_model_search_request** | [**CustomModelSearchRequest**](CustomModelSearchRequest.md)|  | 

### Return type

[**List[CustomModelResponse]**](CustomModelResponse.md)

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

# **update_custom_model**
> CustomModelResponse update_custom_model(custom_model_id, workspace_id, custom_model_update_request)

Update Custom Model

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.custom_model_response import CustomModelResponse
from flowhunt.models.custom_model_update_request import CustomModelUpdateRequest
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
    api_instance = flowhunt.CustomModelsApi(api_client)
    custom_model_id = 'custom_model_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    custom_model_update_request = flowhunt.CustomModelUpdateRequest() # CustomModelUpdateRequest | 

    try:
        # Update Custom Model
        api_response = api_instance.update_custom_model(custom_model_id, workspace_id, custom_model_update_request)
        print("The response of CustomModelsApi->update_custom_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomModelsApi->update_custom_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_model_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **custom_model_update_request** | [**CustomModelUpdateRequest**](CustomModelUpdateRequest.md)|  | 

### Return type

[**CustomModelResponse**](CustomModelResponse.md)

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

