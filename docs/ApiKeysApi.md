# flowhunt-python-sdk.ApiKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeysApi.md#create_api_key) | **POST** /v2/api_keys/create | Create Api Key
[**delete_api_key**](ApiKeysApi.md#delete_api_key) | **DELETE** /v2/api_keys/{api_key_id} | Delete Api Key
[**search_api_key**](ApiKeysApi.md#search_api_key) | **POST** /v2/api_keys/search | Search Api Key
[**update_api_key**](ApiKeysApi.md#update_api_key) | **PUT** /v2/api_keys/{api_key_id} | Update Api Key


# **create_api_key**
> ApiKeyResponse create_api_key(workspace_id, api_key_create_request)

Create Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_key_create_request import ApiKeyCreateRequest
from flowhunt-python-sdk.models.api_key_response import ApiKeyResponse
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.ApiKeysApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    api_key_create_request = flowhunt-python-sdk.ApiKeyCreateRequest() # ApiKeyCreateRequest | 

    try:
        # Create Api Key
        api_response = api_instance.create_api_key(workspace_id, api_key_create_request)
        print("The response of ApiKeysApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **api_key_create_request** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> Completed delete_api_key(api_key_id, workspace_id)

Delete Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.completed import Completed
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.ApiKeysApi(api_client)
    api_key_id = 'api_key_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Api Key
        api_response = api_instance.delete_api_key(api_key_id, workspace_id)
        print("The response of ApiKeysApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **search_api_key**
> List[ApiKeyResponse] search_api_key(workspace_id, api_key_search_request)

Search Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_key_response import ApiKeyResponse
from flowhunt-python-sdk.models.api_key_search_request import ApiKeySearchRequest
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.ApiKeysApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    api_key_search_request = flowhunt-python-sdk.ApiKeySearchRequest() # ApiKeySearchRequest | 

    try:
        # Search Api Key
        api_response = api_instance.search_api_key(workspace_id, api_key_search_request)
        print("The response of ApiKeysApi->search_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->search_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **api_key_search_request** | [**ApiKeySearchRequest**](ApiKeySearchRequest.md)|  | 

### Return type

[**List[ApiKeyResponse]**](ApiKeyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKeyResponse update_api_key(api_key_id, workspace_id, api_key_update_request)

Update Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_key_response import ApiKeyResponse
from flowhunt-python-sdk.models.api_key_update_request import ApiKeyUpdateRequest
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.ApiKeysApi(api_client)
    api_key_id = 'api_key_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    api_key_update_request = flowhunt-python-sdk.ApiKeyUpdateRequest() # ApiKeyUpdateRequest | 

    try:
        # Update Api Key
        api_response = api_instance.update_api_key(api_key_id, workspace_id, api_key_update_request)
        print("The response of ApiKeysApi->update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **api_key_update_request** | [**ApiKeyUpdateRequest**](ApiKeyUpdateRequest.md)|  | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

