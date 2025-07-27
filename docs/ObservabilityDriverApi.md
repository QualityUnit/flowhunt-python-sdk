# flowhunt.ObservabilityDriverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_langfuse_observability_driver**](ObservabilityDriverApi.md#activate_langfuse_observability_driver) | **POST** /v2/observability_driver/langfuse | Activate Langfuse Observability Driver
[**delete_observability_driver**](ObservabilityDriverApi.md#delete_observability_driver) | **DELETE** /v2/observability_driver/{driver_type} | Delete Observability Driver
[**get_observability_driver**](ObservabilityDriverApi.md#get_observability_driver) | **GET** /v2/observability_driver/{driver_type} | Get Observability Driver
[**get_observability_driver_workspace**](ObservabilityDriverApi.md#get_observability_driver_workspace) | **POST** /v2/observability_driver/ | Get Observability Driver Workspace
[**update_langfuse_observability_driver**](ObservabilityDriverApi.md#update_langfuse_observability_driver) | **PUT** /v2/observability_driver/langfuse | Update Langfuse Observability Driver


# **activate_langfuse_observability_driver**
> ObservabilityDriverResponse activate_langfuse_observability_driver(workspace_id, langfuse_request)

Activate Langfuse Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.langfuse_request import LangfuseRequest
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    langfuse_request = flowhunt.LangfuseRequest() # LangfuseRequest | 

    try:
        # Activate Langfuse Observability Driver
        api_response = api_instance.activate_langfuse_observability_driver(workspace_id, langfuse_request)
        print("The response of ObservabilityDriverApi->activate_langfuse_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->activate_langfuse_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **langfuse_request** | [**LangfuseRequest**](LangfuseRequest.md)|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

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

# **delete_observability_driver**
> DriverSuccessResponse delete_observability_driver(driver_type, workspace_id)

Delete Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.driver_success_response import DriverSuccessResponse
from flowhunt.models.driver_type import DriverType
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
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    driver_type = flowhunt.DriverType() # DriverType | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Observability Driver
        api_response = api_instance.delete_observability_driver(driver_type, workspace_id)
        print("The response of ObservabilityDriverApi->delete_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->delete_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_type** | [**DriverType**](.md)|  | 
 **workspace_id** | **str**|  | 

### Return type

[**DriverSuccessResponse**](DriverSuccessResponse.md)

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

# **get_observability_driver**
> ObservabilityDriverResponse get_observability_driver(driver_type, workspace_id)

Get Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.driver_type import DriverType
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    driver_type = flowhunt.DriverType() # DriverType | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Observability Driver
        api_response = api_instance.get_observability_driver(driver_type, workspace_id)
        print("The response of ObservabilityDriverApi->get_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->get_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_type** | [**DriverType**](.md)|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

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

# **get_observability_driver_workspace**
> List[ObservabilityDriverResponse] get_observability_driver_workspace(workspace_id)

Get Observability Driver Workspace

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Observability Driver Workspace
        api_response = api_instance.get_observability_driver_workspace(workspace_id)
        print("The response of ObservabilityDriverApi->get_observability_driver_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->get_observability_driver_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[ObservabilityDriverResponse]**](ObservabilityDriverResponse.md)

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

# **update_langfuse_observability_driver**
> ObservabilityDriverResponse update_langfuse_observability_driver(workspace_id, langfuse_request)

Update Langfuse Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.langfuse_request import LangfuseRequest
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    langfuse_request = flowhunt.LangfuseRequest() # LangfuseRequest | 

    try:
        # Update Langfuse Observability Driver
        api_response = api_instance.update_langfuse_observability_driver(workspace_id, langfuse_request)
        print("The response of ObservabilityDriverApi->update_langfuse_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->update_langfuse_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **langfuse_request** | [**LangfuseRequest**](LangfuseRequest.md)|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

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

