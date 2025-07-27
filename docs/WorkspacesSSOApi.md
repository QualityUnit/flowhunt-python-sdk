# flowhunt.WorkspacesSSOApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_sso_settings**](WorkspacesSSOApi.md#create_workspace_sso_settings) | **POST** /v2/workspaces/{workspace_id}/sso | Create Workspace Sso Settings
[**delete_workspace_sso_settings**](WorkspacesSSOApi.md#delete_workspace_sso_settings) | **DELETE** /v2/workspaces/{workspace_id}/sso/{provider} | Delete Workspace Sso Settings
[**get_workspace_sso_settings**](WorkspacesSSOApi.md#get_workspace_sso_settings) | **GET** /v2/workspaces/{workspace_id}/sso/{provider} | Get Workspace Sso Settings
[**list_workspace_sso_settings**](WorkspacesSSOApi.md#list_workspace_sso_settings) | **GET** /v2/workspaces/{workspace_id}/sso | List Workspace Sso Settings
[**update_workspace_sso_settings**](WorkspacesSSOApi.md#update_workspace_sso_settings) | **PUT** /v2/workspaces/{workspace_id}/sso/{provider} | Update Workspace Sso Settings


# **create_workspace_sso_settings**
> WorkspaceSSOResponse create_workspace_sso_settings(workspace_id, workspace_sso_create_request)

Create Workspace Sso Settings

Create SSO settings for a workspace.
Admin endpoint - requires workspace admin permissions.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_create_request import WorkspaceSSOCreateRequest
from flowhunt.models.workspace_sso_response import WorkspaceSSOResponse
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
    api_instance = flowhunt.WorkspacesSSOApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_sso_create_request = flowhunt.WorkspaceSSOCreateRequest() # WorkspaceSSOCreateRequest | 

    try:
        # Create Workspace Sso Settings
        api_response = api_instance.create_workspace_sso_settings(workspace_id, workspace_sso_create_request)
        print("The response of WorkspacesSSOApi->create_workspace_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSOApi->create_workspace_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_sso_create_request** | [**WorkspaceSSOCreateRequest**](WorkspaceSSOCreateRequest.md)|  | 

### Return type

[**WorkspaceSSOResponse**](WorkspaceSSOResponse.md)

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

# **delete_workspace_sso_settings**
> Completed delete_workspace_sso_settings(workspace_id, provider)

Delete Workspace Sso Settings

Delete SSO settings for a workspace and provider.
Admin endpoint - requires workspace admin permissions.

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
    api_instance = flowhunt.WorkspacesSSOApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    provider = 'provider_example' # str | 

    try:
        # Delete Workspace Sso Settings
        api_response = api_instance.delete_workspace_sso_settings(workspace_id, provider)
        print("The response of WorkspacesSSOApi->delete_workspace_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSOApi->delete_workspace_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **provider** | **str**|  | 

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

# **get_workspace_sso_settings**
> WorkspaceSSOResponse get_workspace_sso_settings(workspace_id, provider)

Get Workspace Sso Settings

Get SSO settings for a specific workspace and provider.
Admin endpoint - requires workspace admin permissions.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_response import WorkspaceSSOResponse
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
    api_instance = flowhunt.WorkspacesSSOApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    provider = 'provider_example' # str | 

    try:
        # Get Workspace Sso Settings
        api_response = api_instance.get_workspace_sso_settings(workspace_id, provider)
        print("The response of WorkspacesSSOApi->get_workspace_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSOApi->get_workspace_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **provider** | **str**|  | 

### Return type

[**WorkspaceSSOResponse**](WorkspaceSSOResponse.md)

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

# **list_workspace_sso_settings**
> WorkspaceSSOListResponse list_workspace_sso_settings(workspace_id)

List Workspace Sso Settings

List all SSO settings for a workspace.
Admin endpoint - requires workspace admin permissions.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_list_response import WorkspaceSSOListResponse
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
    api_instance = flowhunt.WorkspacesSSOApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Workspace Sso Settings
        api_response = api_instance.list_workspace_sso_settings(workspace_id)
        print("The response of WorkspacesSSOApi->list_workspace_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSOApi->list_workspace_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceSSOListResponse**](WorkspaceSSOListResponse.md)

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

# **update_workspace_sso_settings**
> WorkspaceSSOResponse update_workspace_sso_settings(workspace_id, provider, workspace_sso_update_request)

Update Workspace Sso Settings

Update SSO settings for a workspace and provider.
Admin endpoint - requires workspace admin permissions.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_response import WorkspaceSSOResponse
from flowhunt.models.workspace_sso_update_request import WorkspaceSSOUpdateRequest
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
    api_instance = flowhunt.WorkspacesSSOApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    provider = 'provider_example' # str | 
    workspace_sso_update_request = flowhunt.WorkspaceSSOUpdateRequest() # WorkspaceSSOUpdateRequest | 

    try:
        # Update Workspace Sso Settings
        api_response = api_instance.update_workspace_sso_settings(workspace_id, provider, workspace_sso_update_request)
        print("The response of WorkspacesSSOApi->update_workspace_sso_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSOApi->update_workspace_sso_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **provider** | **str**|  | 
 **workspace_sso_update_request** | [**WorkspaceSSOUpdateRequest**](WorkspaceSSOUpdateRequest.md)|  | 

### Return type

[**WorkspaceSSOResponse**](WorkspaceSSOResponse.md)

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

