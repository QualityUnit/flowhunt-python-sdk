# flowhunt-python-sdk.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_integration**](IntegrationsApi.md#create_api_integration) | **POST** /v2/integrations/api_integrations/create | Create Api Integration
[**create_api_integration_endpoint**](IntegrationsApi.md#create_api_integration_endpoint) | **POST** /v2/integrations/api_integrations/{integration_id}/endpoints/create | Create Api Integration Endpoint
[**get_all_integrations**](IntegrationsApi.md#get_all_integrations) | **GET** /v2/integrations/all | Get All Integrations
[**get_api_integration**](IntegrationsApi.md#get_api_integration) | **GET** /v2/integrations/api_integrations/ | Get Api Integration
[**get_api_integration_auth_methods**](IntegrationsApi.md#get_api_integration_auth_methods) | **GET** /v2/integrations/api_integrations/auth_methods | Get Api Integration Auth Methods
[**get_api_integration_endpoints**](IntegrationsApi.md#get_api_integration_endpoints) | **POST** /v2/integrations/api_integrations/{integration_id}/endpoints | Get Api Integration Endpoints
[**get_api_integrations**](IntegrationsApi.md#get_api_integrations) | **POST** /v2/integrations/api_integrations/ | Get Api Integrations
[**get_my_integrations**](IntegrationsApi.md#get_my_integrations) | **POST** /v2/integrations/ | Get My Integrations
[**import_openapi_spec**](IntegrationsApi.md#import_openapi_spec) | **POST** /v2/integrations/api_integrations/{integration_id}/import/openapi-file | Import Openapi Spec
[**import_openapi_spec_from_url**](IntegrationsApi.md#import_openapi_spec_from_url) | **POST** /v2/integrations/api_integrations/{integration_id}/import/openapi-url | Import Openapi Spec From Url
[**remove_api_integration**](IntegrationsApi.md#remove_api_integration) | **DELETE** /v2/integrations/api_integrations/{integration_id} | Remove Api Integration
[**remove_api_integration_endpoint**](IntegrationsApi.md#remove_api_integration_endpoint) | **DELETE** /v2/integrations/api_integrations/{integration_id}/endpoints/{endpoint_id} | Remove Api Integration Endpoint
[**update_api_integration**](IntegrationsApi.md#update_api_integration) | **PUT** /v2/integrations/api_integrations/{integration_id} | Update Api Integration
[**update_api_integration_endpoint**](IntegrationsApi.md#update_api_integration_endpoint) | **PUT** /v2/integrations/api_integrations/{integration_id}/endpoints/{endpoint_id} | Update Api Integration Endpoint


# **create_api_integration**
> ApiIntegrationResponse create_api_integration(workspace_id, api_integration_create_request)

Create Api Integration

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_create_request import ApiIntegrationCreateRequest
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    api_integration_create_request = flowhunt-python-sdk.ApiIntegrationCreateRequest() # ApiIntegrationCreateRequest | 

    try:
        # Create Api Integration
        api_response = api_instance.create_api_integration(workspace_id, api_integration_create_request)
        print("The response of IntegrationsApi->create_api_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_api_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **api_integration_create_request** | [**ApiIntegrationCreateRequest**](ApiIntegrationCreateRequest.md)|  | 

### Return type

[**ApiIntegrationResponse**](ApiIntegrationResponse.md)

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

# **create_api_integration_endpoint**
> ApiEndpointResponse create_api_integration_endpoint(integration_id, workspace_id, api_endpoint_create_request)

Create Api Integration Endpoint

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_endpoint_create_request import ApiEndpointCreateRequest
from flowhunt-python-sdk.models.api_endpoint_response import ApiEndpointResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    api_endpoint_create_request = flowhunt-python-sdk.ApiEndpointCreateRequest() # ApiEndpointCreateRequest | 

    try:
        # Create Api Integration Endpoint
        api_response = api_instance.create_api_integration_endpoint(integration_id, workspace_id, api_endpoint_create_request)
        print("The response of IntegrationsApi->create_api_integration_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_api_integration_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **api_endpoint_create_request** | [**ApiEndpointCreateRequest**](ApiEndpointCreateRequest.md)|  | 

### Return type

[**ApiEndpointResponse**](ApiEndpointResponse.md)

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

# **get_all_integrations**
> List[IntegrationResponse] get_all_integrations(workspace_id)

Get All Integrations

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.integration_response import IntegrationResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get All Integrations
        api_response = api_instance.get_all_integrations(workspace_id)
        print("The response of IntegrationsApi->get_all_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_all_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[IntegrationResponse]**](IntegrationResponse.md)

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

# **get_api_integration**
> ApiIntegrationResponse get_api_integration(workspace_id, integration_id)

Get Api Integration

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    integration_id = 'integration_id_example' # str | 

    try:
        # Get Api Integration
        api_response = api_instance.get_api_integration(workspace_id, integration_id)
        print("The response of IntegrationsApi->get_api_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_api_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **integration_id** | **str**|  | 

### Return type

[**ApiIntegrationResponse**](ApiIntegrationResponse.md)

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

# **get_api_integration_auth_methods**
> List[ApiIntegrationAuthenticationMethod] get_api_integration_auth_methods()

Get Api Integration Auth Methods

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_authentication_method import ApiIntegrationAuthenticationMethod
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)

    try:
        # Get Api Integration Auth Methods
        api_response = api_instance.get_api_integration_auth_methods()
        print("The response of IntegrationsApi->get_api_integration_auth_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_api_integration_auth_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiIntegrationAuthenticationMethod]**](ApiIntegrationAuthenticationMethod.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_integration_endpoints**
> List[ApiEndpointResponse] get_api_integration_endpoints(integration_id, workspace_id, api_endpoint_search_request)

Get Api Integration Endpoints

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_endpoint_response import ApiEndpointResponse
from flowhunt-python-sdk.models.api_endpoint_search_request import ApiEndpointSearchRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    api_endpoint_search_request = flowhunt-python-sdk.ApiEndpointSearchRequest() # ApiEndpointSearchRequest | 

    try:
        # Get Api Integration Endpoints
        api_response = api_instance.get_api_integration_endpoints(integration_id, workspace_id, api_endpoint_search_request)
        print("The response of IntegrationsApi->get_api_integration_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_api_integration_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **api_endpoint_search_request** | [**ApiEndpointSearchRequest**](ApiEndpointSearchRequest.md)|  | 

### Return type

[**List[ApiEndpointResponse]**](ApiEndpointResponse.md)

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

# **get_api_integrations**
> List[ApiIntegrationResponse] get_api_integrations(workspace_id, api_integration_search_request)

Get Api Integrations

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse
from flowhunt-python-sdk.models.api_integration_search_request import ApiIntegrationSearchRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    api_integration_search_request = flowhunt-python-sdk.ApiIntegrationSearchRequest() # ApiIntegrationSearchRequest | 

    try:
        # Get Api Integrations
        api_response = api_instance.get_api_integrations(workspace_id, api_integration_search_request)
        print("The response of IntegrationsApi->get_api_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_api_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **api_integration_search_request** | [**ApiIntegrationSearchRequest**](ApiIntegrationSearchRequest.md)|  | 

### Return type

[**List[ApiIntegrationResponse]**](ApiIntegrationResponse.md)

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

# **get_my_integrations**
> List[IntegrationDetailResponse] get_my_integrations(workspace_id, integration_search_request)

Get My Integrations

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.integration_detail_response import IntegrationDetailResponse
from flowhunt-python-sdk.models.integration_search_request import IntegrationSearchRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    integration_search_request = flowhunt-python-sdk.IntegrationSearchRequest() # IntegrationSearchRequest | 

    try:
        # Get My Integrations
        api_response = api_instance.get_my_integrations(workspace_id, integration_search_request)
        print("The response of IntegrationsApi->get_my_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_my_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **integration_search_request** | [**IntegrationSearchRequest**](IntegrationSearchRequest.md)|  | 

### Return type

[**List[IntegrationDetailResponse]**](IntegrationDetailResponse.md)

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

# **import_openapi_spec**
> ApiIntegrationResponse import_openapi_spec(integration_id, workspace_id, file)

Import Openapi Spec

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file = None # bytearray | 

    try:
        # Import Openapi Spec
        api_response = api_instance.import_openapi_spec(integration_id, workspace_id, file)
        print("The response of IntegrationsApi->import_openapi_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->import_openapi_spec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**ApiIntegrationResponse**](ApiIntegrationResponse.md)

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

# **import_openapi_spec_from_url**
> ApiIntegrationResponse import_openapi_spec_from_url(integration_id, workspace_id, api_integration_open_api_import_request)

Import Openapi Spec From Url

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_open_api_import_request import ApiIntegrationOpenApiImportRequest
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    api_integration_open_api_import_request = flowhunt-python-sdk.ApiIntegrationOpenApiImportRequest() # ApiIntegrationOpenApiImportRequest | 

    try:
        # Import Openapi Spec From Url
        api_response = api_instance.import_openapi_spec_from_url(integration_id, workspace_id, api_integration_open_api_import_request)
        print("The response of IntegrationsApi->import_openapi_spec_from_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->import_openapi_spec_from_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **api_integration_open_api_import_request** | [**ApiIntegrationOpenApiImportRequest**](ApiIntegrationOpenApiImportRequest.md)|  | 

### Return type

[**ApiIntegrationResponse**](ApiIntegrationResponse.md)

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

# **remove_api_integration**
> Completed remove_api_integration(integration_id, workspace_id)

Remove Api Integration

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Remove Api Integration
        api_response = api_instance.remove_api_integration(integration_id, workspace_id)
        print("The response of IntegrationsApi->remove_api_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->remove_api_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
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

# **remove_api_integration_endpoint**
> Completed remove_api_integration_endpoint(integration_id, endpoint_id, workspace_id)

Remove Api Integration Endpoint

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    endpoint_id = 'endpoint_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Remove Api Integration Endpoint
        api_response = api_instance.remove_api_integration_endpoint(integration_id, endpoint_id, workspace_id)
        print("The response of IntegrationsApi->remove_api_integration_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->remove_api_integration_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **endpoint_id** | **str**|  | 
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

# **update_api_integration**
> ApiIntegrationResponse update_api_integration(integration_id, workspace_id, api_integration_update_request)

Update Api Integration

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse
from flowhunt-python-sdk.models.api_integration_update_request import ApiIntegrationUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    api_integration_update_request = flowhunt-python-sdk.ApiIntegrationUpdateRequest() # ApiIntegrationUpdateRequest | 

    try:
        # Update Api Integration
        api_response = api_instance.update_api_integration(integration_id, workspace_id, api_integration_update_request)
        print("The response of IntegrationsApi->update_api_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->update_api_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **api_integration_update_request** | [**ApiIntegrationUpdateRequest**](ApiIntegrationUpdateRequest.md)|  | 

### Return type

[**ApiIntegrationResponse**](ApiIntegrationResponse.md)

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

# **update_api_integration_endpoint**
> ApiEndpointResponse update_api_integration_endpoint(integration_id, endpoint_id, workspace_id, api_endpoint_update_request)

Update Api Integration Endpoint

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.api_endpoint_response import ApiEndpointResponse
from flowhunt-python-sdk.models.api_endpoint_update_request import ApiEndpointUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    endpoint_id = 'endpoint_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    api_endpoint_update_request = flowhunt-python-sdk.ApiEndpointUpdateRequest() # ApiEndpointUpdateRequest | 

    try:
        # Update Api Integration Endpoint
        api_response = api_instance.update_api_integration_endpoint(integration_id, endpoint_id, workspace_id, api_endpoint_update_request)
        print("The response of IntegrationsApi->update_api_integration_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->update_api_integration_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **endpoint_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **api_endpoint_update_request** | [**ApiEndpointUpdateRequest**](ApiEndpointUpdateRequest.md)|  | 

### Return type

[**ApiEndpointResponse**](ApiEndpointResponse.md)

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

