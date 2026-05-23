# flowhunt.ProjectIssueTagsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_issue_tag**](ProjectIssueTagsApi.md#create_project_issue_tag) | **POST** /v2/projects/{project_id}/tags/create | Create Project Issue Tag
[**delete_project_issue_tag**](ProjectIssueTagsApi.md#delete_project_issue_tag) | **DELETE** /v2/projects/{project_id}/tags/{tag_id} | Delete Project Issue Tag
[**get_project_issue_tag**](ProjectIssueTagsApi.md#get_project_issue_tag) | **GET** /v2/projects/{project_id}/tags/{tag_id} | Get Project Issue Tag
[**search_project_issue_tags**](ProjectIssueTagsApi.md#search_project_issue_tags) | **POST** /v2/projects/{project_id}/tags/ | Search Project Issue Tags
[**update_project_issue_tag**](ProjectIssueTagsApi.md#update_project_issue_tag) | **PUT** /v2/projects/{project_id}/tags/{tag_id} | Update Project Issue Tag


# **create_project_issue_tag**
> ProjectIssueTagResponse create_project_issue_tag(project_id, workspace_id, project_issue_tag_create)

Create Project Issue Tag

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_tag_create import ProjectIssueTagCreate
from flowhunt.models.project_issue_tag_response import ProjectIssueTagResponse
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
    api_instance = flowhunt.ProjectIssueTagsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_tag_create = flowhunt.ProjectIssueTagCreate() # ProjectIssueTagCreate | 

    try:
        # Create Project Issue Tag
        api_response = api_instance.create_project_issue_tag(project_id, workspace_id, project_issue_tag_create)
        print("The response of ProjectIssueTagsApi->create_project_issue_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueTagsApi->create_project_issue_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_tag_create** | [**ProjectIssueTagCreate**](ProjectIssueTagCreate.md)|  | 

### Return type

[**ProjectIssueTagResponse**](ProjectIssueTagResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_issue_tag**
> Completed delete_project_issue_tag(project_id, tag_id, workspace_id)

Delete Project Issue Tag

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
    api_instance = flowhunt.ProjectIssueTagsApi(api_client)
    project_id = 'project_id_example' # str | 
    tag_id = 'tag_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Project Issue Tag
        api_response = api_instance.delete_project_issue_tag(project_id, tag_id, workspace_id)
        print("The response of ProjectIssueTagsApi->delete_project_issue_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueTagsApi->delete_project_issue_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tag_id** | **str**|  | 
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

# **get_project_issue_tag**
> ProjectIssueTagResponse get_project_issue_tag(project_id, tag_id, workspace_id)

Get Project Issue Tag

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_tag_response import ProjectIssueTagResponse
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
    api_instance = flowhunt.ProjectIssueTagsApi(api_client)
    project_id = 'project_id_example' # str | 
    tag_id = 'tag_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Project Issue Tag
        api_response = api_instance.get_project_issue_tag(project_id, tag_id, workspace_id)
        print("The response of ProjectIssueTagsApi->get_project_issue_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueTagsApi->get_project_issue_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tag_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectIssueTagResponse**](ProjectIssueTagResponse.md)

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

# **search_project_issue_tags**
> List[ProjectIssueTagResponse] search_project_issue_tags(project_id, workspace_id, project_issue_tag_search_request)

Search Project Issue Tags

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_tag_response import ProjectIssueTagResponse
from flowhunt.models.project_issue_tag_search_request import ProjectIssueTagSearchRequest
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
    api_instance = flowhunt.ProjectIssueTagsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_tag_search_request = flowhunt.ProjectIssueTagSearchRequest() # ProjectIssueTagSearchRequest | 

    try:
        # Search Project Issue Tags
        api_response = api_instance.search_project_issue_tags(project_id, workspace_id, project_issue_tag_search_request)
        print("The response of ProjectIssueTagsApi->search_project_issue_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueTagsApi->search_project_issue_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_tag_search_request** | [**ProjectIssueTagSearchRequest**](ProjectIssueTagSearchRequest.md)|  | 

### Return type

[**List[ProjectIssueTagResponse]**](ProjectIssueTagResponse.md)

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

# **update_project_issue_tag**
> ProjectIssueTagResponse update_project_issue_tag(project_id, tag_id, workspace_id, project_issue_tag_update)

Update Project Issue Tag

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_tag_response import ProjectIssueTagResponse
from flowhunt.models.project_issue_tag_update import ProjectIssueTagUpdate
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
    api_instance = flowhunt.ProjectIssueTagsApi(api_client)
    project_id = 'project_id_example' # str | 
    tag_id = 'tag_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_tag_update = flowhunt.ProjectIssueTagUpdate() # ProjectIssueTagUpdate | 

    try:
        # Update Project Issue Tag
        api_response = api_instance.update_project_issue_tag(project_id, tag_id, workspace_id, project_issue_tag_update)
        print("The response of ProjectIssueTagsApi->update_project_issue_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueTagsApi->update_project_issue_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tag_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_tag_update** | [**ProjectIssueTagUpdate**](ProjectIssueTagUpdate.md)|  | 

### Return type

[**ProjectIssueTagResponse**](ProjectIssueTagResponse.md)

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

