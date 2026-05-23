# flowhunt.AsanaApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asana_project_tasks**](AsanaApi.md#get_asana_project_tasks) | **GET** /v2/integrations/asana/{integration_id}/projects/{project_gid}/tasks | Get Asana Project Tasks
[**get_asana_projects**](AsanaApi.md#get_asana_projects) | **GET** /v2/integrations/asana/{integration_id}/projects | Get Asana Projects
[**get_asana_users**](AsanaApi.md#get_asana_users) | **GET** /v2/integrations/asana/{integration_id}/users | Get Asana Users
[**get_asana_workspaces**](AsanaApi.md#get_asana_workspaces) | **GET** /v2/integrations/asana/ | Get Asana Workspaces


# **get_asana_project_tasks**
> List[AsanaTaskResponse] get_asana_project_tasks(integration_id, project_gid, workspace_id)

Get Asana Project Tasks

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.asana_task_response import AsanaTaskResponse
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
    api_instance = flowhunt.AsanaApi(api_client)
    integration_id = 'integration_id_example' # str | 
    project_gid = 'project_gid_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Asana Project Tasks
        api_response = api_instance.get_asana_project_tasks(integration_id, project_gid, workspace_id)
        print("The response of AsanaApi->get_asana_project_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsanaApi->get_asana_project_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **project_gid** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[AsanaTaskResponse]**](AsanaTaskResponse.md)

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

# **get_asana_projects**
> List[AsanaProjectResponse] get_asana_projects(integration_id, workspace_id)

Get Asana Projects

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.asana_project_response import AsanaProjectResponse
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
    api_instance = flowhunt.AsanaApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Asana Projects
        api_response = api_instance.get_asana_projects(integration_id, workspace_id)
        print("The response of AsanaApi->get_asana_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsanaApi->get_asana_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[AsanaProjectResponse]**](AsanaProjectResponse.md)

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

# **get_asana_users**
> List[AsanaUserResponse] get_asana_users(integration_id, workspace_id)

Get Asana Users

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.asana_user_response import AsanaUserResponse
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
    api_instance = flowhunt.AsanaApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Asana Users
        api_response = api_instance.get_asana_users(integration_id, workspace_id)
        print("The response of AsanaApi->get_asana_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsanaApi->get_asana_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[AsanaUserResponse]**](AsanaUserResponse.md)

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

# **get_asana_workspaces**
> List[AsanaWorkspaceResponse] get_asana_workspaces(workspace_id)

Get Asana Workspaces

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.asana_workspace_response import AsanaWorkspaceResponse
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
    api_instance = flowhunt.AsanaApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Asana Workspaces
        api_response = api_instance.get_asana_workspaces(workspace_id)
        print("The response of AsanaApi->get_asana_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsanaApi->get_asana_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[AsanaWorkspaceResponse]**](AsanaWorkspaceResponse.md)

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

