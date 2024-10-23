# flowhunt.SecretsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret**](SecretsApi.md#create_secret) | **POST** /v2/secrets/create | Create Secret
[**delete_secret**](SecretsApi.md#delete_secret) | **DELETE** /v2/secrets/{secret_id} | Delete Secret
[**get_secret**](SecretsApi.md#get_secret) | **GET** /v2/secrets/{secret_id} | Get Secret
[**search_secret**](SecretsApi.md#search_secret) | **POST** /v2/secrets/search | Search Secret
[**update_secret**](SecretsApi.md#update_secret) | **PUT** /v2/secrets/{secret_id} | Update Secret


# **create_secret**
> SecretResponse create_secret(workspace_id, secret_create_request)

Create Secret

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.secret_create_request import SecretCreateRequest
from flowhunt.models.secret_response import SecretResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.SecretsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    secret_create_request = flowhunt.SecretCreateRequest() # SecretCreateRequest | 

    try:
        # Create Secret
        api_response = api_instance.create_secret(workspace_id, secret_create_request)
        print("The response of SecretsApi->create_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->create_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **secret_create_request** | [**SecretCreateRequest**](SecretCreateRequest.md)|  | 

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **delete_secret**
> Completed delete_secret(secret_id, workspace_id)

Delete Secret

### Example

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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.SecretsApi(api_client)
    secret_id = 'secret_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Secret
        api_response = api_instance.delete_secret(secret_id, workspace_id)
        print("The response of SecretsApi->delete_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->delete_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **str**|  | 
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

# **get_secret**
> SecretResponse get_secret(secret_id, workspace_id)

Get Secret

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.secret_response import SecretResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.SecretsApi(api_client)
    secret_id = 'secret_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Secret
        api_response = api_instance.get_secret(secret_id, workspace_id)
        print("The response of SecretsApi->get_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->get_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **search_secret**
> List[SecretResponse] search_secret(workspace_id, secret_search_request)

Search Secret

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.secret_response import SecretResponse
from flowhunt.models.secret_search_request import SecretSearchRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.SecretsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    secret_search_request = flowhunt.SecretSearchRequest() # SecretSearchRequest | 

    try:
        # Search Secret
        api_response = api_instance.search_secret(workspace_id, secret_search_request)
        print("The response of SecretsApi->search_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->search_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **secret_search_request** | [**SecretSearchRequest**](SecretSearchRequest.md)|  | 

### Return type

[**List[SecretResponse]**](SecretResponse.md)

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

# **update_secret**
> SecretResponse update_secret(secret_id, workspace_id, secret_update_request)

Update Secret

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.secret_response import SecretResponse
from flowhunt.models.secret_update_request import SecretUpdateRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.SecretsApi(api_client)
    secret_id = 'secret_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    secret_update_request = flowhunt.SecretUpdateRequest() # SecretUpdateRequest | 

    try:
        # Update Secret
        api_response = api_instance.update_secret(secret_id, workspace_id, secret_update_request)
        print("The response of SecretsApi->update_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->update_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **secret_update_request** | [**SecretUpdateRequest**](SecretUpdateRequest.md)|  | 

### Return type

[**SecretResponse**](SecretResponse.md)

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

