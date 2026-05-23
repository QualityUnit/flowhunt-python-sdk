# flowhunt.MCPConnectorsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcp_connector**](MCPConnectorsApi.md#create_mcp_connector) | **POST** /v2/mcp_connectors/create | Create Mcp Connector
[**delete_mcp_connector**](MCPConnectorsApi.md#delete_mcp_connector) | **DELETE** /v2/mcp_connectors/{connector_id} | Delete Mcp Connector
[**get_mcp_connector**](MCPConnectorsApi.md#get_mcp_connector) | **GET** /v2/mcp_connectors/{connector_id} | Get Mcp Connector
[**search_mcp_connectors**](MCPConnectorsApi.md#search_mcp_connectors) | **POST** /v2/mcp_connectors/search | Search Mcp Connectors
[**test_mcp_connector**](MCPConnectorsApi.md#test_mcp_connector) | **POST** /v2/mcp_connectors/{connector_id}/test | Test Mcp Connector
[**update_mcp_connector**](MCPConnectorsApi.md#update_mcp_connector) | **PUT** /v2/mcp_connectors/{connector_id} | Update Mcp Connector


# **create_mcp_connector**
> MCPConnectorResponse create_mcp_connector(workspace_id, mcp_connector_create_request)

Create Mcp Connector

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_connector_create_request import MCPConnectorCreateRequest
from flowhunt.models.mcp_connector_response import MCPConnectorResponse
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
    api_instance = flowhunt.MCPConnectorsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    mcp_connector_create_request = flowhunt.MCPConnectorCreateRequest() # MCPConnectorCreateRequest | 

    try:
        # Create Mcp Connector
        api_response = api_instance.create_mcp_connector(workspace_id, mcp_connector_create_request)
        print("The response of MCPConnectorsApi->create_mcp_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPConnectorsApi->create_mcp_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **mcp_connector_create_request** | [**MCPConnectorCreateRequest**](MCPConnectorCreateRequest.md)|  | 

### Return type

[**MCPConnectorResponse**](MCPConnectorResponse.md)

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

# **delete_mcp_connector**
> Completed delete_mcp_connector(connector_id, workspace_id)

Delete Mcp Connector

### Example

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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.MCPConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Mcp Connector
        api_response = api_instance.delete_mcp_connector(connector_id, workspace_id)
        print("The response of MCPConnectorsApi->delete_mcp_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPConnectorsApi->delete_mcp_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
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

# **get_mcp_connector**
> MCPConnectorResponse get_mcp_connector(connector_id, workspace_id)

Get Mcp Connector

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_connector_response import MCPConnectorResponse
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
    api_instance = flowhunt.MCPConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Mcp Connector
        api_response = api_instance.get_mcp_connector(connector_id, workspace_id)
        print("The response of MCPConnectorsApi->get_mcp_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPConnectorsApi->get_mcp_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**MCPConnectorResponse**](MCPConnectorResponse.md)

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

# **search_mcp_connectors**
> List[MCPConnectorResponse] search_mcp_connectors(workspace_id, mcp_connector_search_request)

Search Mcp Connectors

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_connector_response import MCPConnectorResponse
from flowhunt.models.mcp_connector_search_request import MCPConnectorSearchRequest
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
    api_instance = flowhunt.MCPConnectorsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    mcp_connector_search_request = flowhunt.MCPConnectorSearchRequest() # MCPConnectorSearchRequest | 

    try:
        # Search Mcp Connectors
        api_response = api_instance.search_mcp_connectors(workspace_id, mcp_connector_search_request)
        print("The response of MCPConnectorsApi->search_mcp_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPConnectorsApi->search_mcp_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **mcp_connector_search_request** | [**MCPConnectorSearchRequest**](MCPConnectorSearchRequest.md)|  | 

### Return type

[**List[MCPConnectorResponse]**](MCPConnectorResponse.md)

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

# **test_mcp_connector**
> MCPConnectorTestResponse test_mcp_connector(connector_id, workspace_id)

Test Mcp Connector

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_connector_test_response import MCPConnectorTestResponse
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
    api_instance = flowhunt.MCPConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Test Mcp Connector
        api_response = api_instance.test_mcp_connector(connector_id, workspace_id)
        print("The response of MCPConnectorsApi->test_mcp_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPConnectorsApi->test_mcp_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**MCPConnectorTestResponse**](MCPConnectorTestResponse.md)

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

# **update_mcp_connector**
> MCPConnectorResponse update_mcp_connector(connector_id, workspace_id, mcp_connector_update_request)

Update Mcp Connector

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_connector_response import MCPConnectorResponse
from flowhunt.models.mcp_connector_update_request import MCPConnectorUpdateRequest
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
    api_instance = flowhunt.MCPConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    mcp_connector_update_request = flowhunt.MCPConnectorUpdateRequest() # MCPConnectorUpdateRequest | 

    try:
        # Update Mcp Connector
        api_response = api_instance.update_mcp_connector(connector_id, workspace_id, mcp_connector_update_request)
        print("The response of MCPConnectorsApi->update_mcp_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPConnectorsApi->update_mcp_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **mcp_connector_update_request** | [**MCPConnectorUpdateRequest**](MCPConnectorUpdateRequest.md)|  | 

### Return type

[**MCPConnectorResponse**](MCPConnectorResponse.md)

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

