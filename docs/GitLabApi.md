# flowhunt.GitLabApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_branches**](GitLabApi.md#get_branches) | **GET** /v2/integrations/gitlab/branches | Get Branches
[**get_projects**](GitLabApi.md#get_projects) | **GET** /v2/integrations/gitlab/projects | Get Projects


# **get_branches**
> GitLabBranchesResponse get_branches(workspace_id, project_id)

Get Branches

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.git_lab_branches_response import GitLabBranchesResponse
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
    api_instance = flowhunt.GitLabApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Get Branches
        api_response = api_instance.get_branches(workspace_id, project_id)
        print("The response of GitLabApi->get_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitLabApi->get_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**GitLabBranchesResponse**](GitLabBranchesResponse.md)

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

# **get_projects**
> GitLabProjectsResponse get_projects(workspace_id)

Get Projects

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.git_lab_projects_response import GitLabProjectsResponse
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
    api_instance = flowhunt.GitLabApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Projects
        api_response = api_instance.get_projects(workspace_id)
        print("The response of GitLabApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitLabApi->get_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GitLabProjectsResponse**](GitLabProjectsResponse.md)

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

