# flowhunt.ProjectIssuesApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_comment**](ProjectIssuesApi.md#add_user_comment) | **POST** /v2/projects/{project_id}/issues/{issue_id}/comments | Add User Comment
[**cancel_all_issues**](ProjectIssuesApi.md#cancel_all_issues) | **POST** /v2/projects/{project_id}/issues/cancel-all | Cancel All Issues
[**cancel_issue**](ProjectIssuesApi.md#cancel_issue) | **POST** /v2/projects/{project_id}/issues/{issue_id}/cancel | Cancel Issue
[**create_project_issue**](ProjectIssuesApi.md#create_project_issue) | **POST** /v2/projects/{project_id}/issues/create | Create Project Issue
[**delete_issue**](ProjectIssuesApi.md#delete_issue) | **DELETE** /v2/projects/{project_id}/issues/{issue_id} | Delete Issue
[**get_project_issue**](ProjectIssuesApi.md#get_project_issue) | **GET** /v2/projects/{project_id}/issues/{issue_id} | Get Project Issue
[**search_project_issues**](ProjectIssuesApi.md#search_project_issues) | **POST** /v2/projects/{project_id}/issues/ | Search Project Issues
[**update_project_issue**](ProjectIssuesApi.md#update_project_issue) | **PUT** /v2/projects/{project_id}/issues/{issue_id} | Update Project Issue


# **add_user_comment**
> ProjectIssueResponse add_user_comment(project_id, issue_id, workspace_id, project_issue_comment_create)

Add User Comment

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_comment_create import ProjectIssueCommentCreate
from flowhunt.models.project_issue_response import ProjectIssueResponse
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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    issue_id = 'issue_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_comment_create = flowhunt.ProjectIssueCommentCreate() # ProjectIssueCommentCreate | 

    try:
        # Add User Comment
        api_response = api_instance.add_user_comment(project_id, issue_id, workspace_id, project_issue_comment_create)
        print("The response of ProjectIssuesApi->add_user_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->add_user_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **issue_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_comment_create** | [**ProjectIssueCommentCreate**](ProjectIssueCommentCreate.md)|  | 

### Return type

[**ProjectIssueResponse**](ProjectIssueResponse.md)

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

# **cancel_all_issues**
> Completed cancel_all_issues(project_id, workspace_id)

Cancel All Issues

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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Cancel All Issues
        api_response = api_instance.cancel_all_issues(project_id, workspace_id)
        print("The response of ProjectIssuesApi->cancel_all_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->cancel_all_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **cancel_issue**
> ProjectIssueResponse cancel_issue(project_id, issue_id, workspace_id)

Cancel Issue

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_response import ProjectIssueResponse
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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    issue_id = 'issue_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Cancel Issue
        api_response = api_instance.cancel_issue(project_id, issue_id, workspace_id)
        print("The response of ProjectIssuesApi->cancel_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->cancel_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **issue_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectIssueResponse**](ProjectIssueResponse.md)

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

# **create_project_issue**
> ProjectIssueResponse create_project_issue(project_id, workspace_id, project_issue_create)

Create Project Issue

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_create import ProjectIssueCreate
from flowhunt.models.project_issue_response import ProjectIssueResponse
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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_create = flowhunt.ProjectIssueCreate() # ProjectIssueCreate | 

    try:
        # Create Project Issue
        api_response = api_instance.create_project_issue(project_id, workspace_id, project_issue_create)
        print("The response of ProjectIssuesApi->create_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->create_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_create** | [**ProjectIssueCreate**](ProjectIssueCreate.md)|  | 

### Return type

[**ProjectIssueResponse**](ProjectIssueResponse.md)

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

# **delete_issue**
> Completed delete_issue(project_id, issue_id, workspace_id)

Delete Issue

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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    issue_id = 'issue_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Issue
        api_response = api_instance.delete_issue(project_id, issue_id, workspace_id)
        print("The response of ProjectIssuesApi->delete_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->delete_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **issue_id** | **str**|  | 
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

# **get_project_issue**
> ProjectIssueResponse get_project_issue(project_id, issue_id, workspace_id)

Get Project Issue

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_response import ProjectIssueResponse
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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    issue_id = 'issue_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Project Issue
        api_response = api_instance.get_project_issue(project_id, issue_id, workspace_id)
        print("The response of ProjectIssuesApi->get_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->get_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **issue_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectIssueResponse**](ProjectIssueResponse.md)

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

# **search_project_issues**
> ProjectIssueSearchResponse search_project_issues(project_id, workspace_id, project_issue_search_request)

Search Project Issues

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_search_request import ProjectIssueSearchRequest
from flowhunt.models.project_issue_search_response import ProjectIssueSearchResponse
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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_search_request = flowhunt.ProjectIssueSearchRequest() # ProjectIssueSearchRequest | 

    try:
        # Search Project Issues
        api_response = api_instance.search_project_issues(project_id, workspace_id, project_issue_search_request)
        print("The response of ProjectIssuesApi->search_project_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->search_project_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_search_request** | [**ProjectIssueSearchRequest**](ProjectIssueSearchRequest.md)|  | 

### Return type

[**ProjectIssueSearchResponse**](ProjectIssueSearchResponse.md)

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

# **update_project_issue**
> ProjectIssueResponse update_project_issue(project_id, issue_id, workspace_id, project_issue_update)

Update Project Issue

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_issue_response import ProjectIssueResponse
from flowhunt.models.project_issue_update import ProjectIssueUpdate
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
    api_instance = flowhunt.ProjectIssuesApi(api_client)
    project_id = 'project_id_example' # str | 
    issue_id = 'issue_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_issue_update = flowhunt.ProjectIssueUpdate() # ProjectIssueUpdate | 

    try:
        # Update Project Issue
        api_response = api_instance.update_project_issue(project_id, issue_id, workspace_id, project_issue_update)
        print("The response of ProjectIssuesApi->update_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssuesApi->update_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **issue_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_issue_update** | [**ProjectIssueUpdate**](ProjectIssueUpdate.md)|  | 

### Return type

[**ProjectIssueResponse**](ProjectIssueResponse.md)

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

