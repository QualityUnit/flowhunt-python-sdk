# flowhunt.MCPServersApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcp_server**](MCPServersApi.md#create_mcp_server) | **POST** /v2/mcp_servers/create | Create Mcp Server
[**delete_mcp_server**](MCPServersApi.md#delete_mcp_server) | **DELETE** /v2/mcp_servers/{mcp_server_id} | Delete Mcp Server
[**get_all_mcp_subservers**](MCPServersApi.md#get_all_mcp_subservers) | **GET** /v2/mcp_servers/all | Get All Mcp Subservers
[**get_mcp_server**](MCPServersApi.md#get_mcp_server) | **GET** /v2/mcp_servers/{mcp_server_id} | Get Mcp Server
[**search_mcp_servers**](MCPServersApi.md#search_mcp_servers) | **POST** /v2/mcp_servers/ | Search Mcp Servers
[**update_mcp_server**](MCPServersApi.md#update_mcp_server) | **PUT** /v2/mcp_servers/{mcp_server_id} | Update Mcp Server


# **create_mcp_server**
> MCPServerResponse create_mcp_server(workspace_id, mcp_server_create_request)

Create Mcp Server

Create a new MCP server.

Args:
    main_request: The main request object for rate limiting.
    workspace_id: The workspace ID.
    request: The MCP server creation request.
    user: The authenticated user.
    controller: The MCP server controller.

Returns:
    MCPServerCreateResponse: The created MCP server with the raw API key.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_server_create_request import MCPServerCreateRequest
from flowhunt.models.mcp_server_response import MCPServerResponse
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
    api_instance = flowhunt.MCPServersApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    mcp_server_create_request = flowhunt.MCPServerCreateRequest() # MCPServerCreateRequest | 

    try:
        # Create Mcp Server
        api_response = api_instance.create_mcp_server(workspace_id, mcp_server_create_request)
        print("The response of MCPServersApi->create_mcp_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPServersApi->create_mcp_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **mcp_server_create_request** | [**MCPServerCreateRequest**](MCPServerCreateRequest.md)|  | 

### Return type

[**MCPServerResponse**](MCPServerResponse.md)

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

# **delete_mcp_server**
> Completed delete_mcp_server(mcp_server_id, workspace_id)

Delete Mcp Server

Delete an MCP server.

Args:
    main_request: The main request object for rate limiting.
    workspace_id: The workspace ID.
    mcp_server_id: The MCP server ID.
    user: The authenticated user.
    controller: The MCP server controller.

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
    api_instance = flowhunt.MCPServersApi(api_client)
    mcp_server_id = 'mcp_server_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Mcp Server
        api_response = api_instance.delete_mcp_server(mcp_server_id, workspace_id)
        print("The response of MCPServersApi->delete_mcp_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPServersApi->delete_mcp_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_server_id** | **str**|  | 
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

# **get_all_mcp_subservers**
> List[GeneralMCPSubserverResponse] get_all_mcp_subservers()

Get All Mcp Subservers

Get all MCP subservers available in the system.

Args:
    user: The authenticated user.
    controller: The MCP server controller.

Returns:
    List[MCPSubServerBinding]: List of all MCP subservers.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.general_mcp_subserver_response import GeneralMCPSubserverResponse
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
    api_instance = flowhunt.MCPServersApi(api_client)

    try:
        # Get All Mcp Subservers
        api_response = api_instance.get_all_mcp_subservers()
        print("The response of MCPServersApi->get_all_mcp_subservers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPServersApi->get_all_mcp_subservers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GeneralMCPSubserverResponse]**](GeneralMCPSubserverResponse.md)

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

# **get_mcp_server**
> MCPServerResponse get_mcp_server(mcp_server_id, workspace_id)

Get Mcp Server

Get an MCP server by ID.

Args:
    workspace_id: The workspace ID.
    mcp_server_id: The MCP server ID.
    user: The authenticated user.
    controller: The MCP server controller.

Returns:
    MCPServerResponse: The MCP server.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_server_response import MCPServerResponse
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
    api_instance = flowhunt.MCPServersApi(api_client)
    mcp_server_id = 'mcp_server_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Mcp Server
        api_response = api_instance.get_mcp_server(mcp_server_id, workspace_id)
        print("The response of MCPServersApi->get_mcp_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPServersApi->get_mcp_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_server_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**MCPServerResponse**](MCPServerResponse.md)

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

# **search_mcp_servers**
> List[MCPServerResponse] search_mcp_servers(workspace_id, mcp_server_search_request)

Search Mcp Servers

List MCP servers in a workspace.

Args:
    workspace_id: The workspace ID.
    user: The authenticated user.
    controller: The MCP server controller.

Returns:
    List[MCPServerResponse]: List of MCP servers.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_server_response import MCPServerResponse
from flowhunt.models.mcp_server_search_request import MCPServerSearchRequest
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
    api_instance = flowhunt.MCPServersApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    mcp_server_search_request = flowhunt.MCPServerSearchRequest() # MCPServerSearchRequest | 

    try:
        # Search Mcp Servers
        api_response = api_instance.search_mcp_servers(workspace_id, mcp_server_search_request)
        print("The response of MCPServersApi->search_mcp_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPServersApi->search_mcp_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **mcp_server_search_request** | [**MCPServerSearchRequest**](MCPServerSearchRequest.md)|  | 

### Return type

[**List[MCPServerResponse]**](MCPServerResponse.md)

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

# **update_mcp_server**
> MCPServerResponse update_mcp_server(mcp_server_id, workspace_id, mcp_server_create_request)

Update Mcp Server

Update an MCP server.

Args:
    main_request: The main request object for rate limiting.
    workspace_id: The workspace ID.
    mcp_server_id: The MCP server ID.
    request: The update request.
    user: The authenticated user.
    controller: The MCP server controller.

Returns:
    MCPServerResponse: The updated MCP server.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.mcp_server_create_request import MCPServerCreateRequest
from flowhunt.models.mcp_server_response import MCPServerResponse
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
    api_instance = flowhunt.MCPServersApi(api_client)
    mcp_server_id = 'mcp_server_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    mcp_server_create_request = flowhunt.MCPServerCreateRequest() # MCPServerCreateRequest | 

    try:
        # Update Mcp Server
        api_response = api_instance.update_mcp_server(mcp_server_id, workspace_id, mcp_server_create_request)
        print("The response of MCPServersApi->update_mcp_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPServersApi->update_mcp_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_server_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **mcp_server_create_request** | [**MCPServerCreateRequest**](MCPServerCreateRequest.md)|  | 

### Return type

[**MCPServerResponse**](MCPServerResponse.md)

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

