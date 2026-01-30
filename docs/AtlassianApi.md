# flowhunt.AtlassianApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_confluence_pages**](AtlassianApi.md#get_confluence_pages) | **GET** /v2/integrations/atlassian/confluence/spaces/{space_key}/pages | Get Confluence Pages
[**get_confluence_spaces**](AtlassianApi.md#get_confluence_spaces) | **GET** /v2/integrations/atlassian/confluence/spaces | Get Confluence Spaces
[**get_jira_assignees**](AtlassianApi.md#get_jira_assignees) | **GET** /v2/integrations/atlassian/jira/projects/{project_key}/assignees | Get Jira Assignees
[**get_jira_issues**](AtlassianApi.md#get_jira_issues) | **GET** /v2/integrations/atlassian/jira/projects/{project_key}/issues | Get Jira Issues
[**get_jira_projects**](AtlassianApi.md#get_jira_projects) | **GET** /v2/integrations/atlassian/jira/projects | Get Jira Projects
[**get_jira_transitions**](AtlassianApi.md#get_jira_transitions) | **GET** /v2/integrations/atlassian/jira/issues/{issue_key}/transitions | Get Jira Transitions


# **get_confluence_pages**
> ConfluencePagesResponse get_confluence_pages(space_key, workspace_id)

Get Confluence Pages

Get all pages in a Confluence space.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.confluence_pages_response import ConfluencePagesResponse
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
    api_instance = flowhunt.AtlassianApi(api_client)
    space_key = 'space_key_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Confluence Pages
        api_response = api_instance.get_confluence_pages(space_key, workspace_id)
        print("The response of AtlassianApi->get_confluence_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtlassianApi->get_confluence_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_key** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ConfluencePagesResponse**](ConfluencePagesResponse.md)

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

# **get_confluence_spaces**
> ConfluenceSpacesResponse get_confluence_spaces(workspace_id)

Get Confluence Spaces

Get all Confluence spaces accessible through the workspace's Atlassian integration.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.confluence_spaces_response import ConfluenceSpacesResponse
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
    api_instance = flowhunt.AtlassianApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Confluence Spaces
        api_response = api_instance.get_confluence_spaces(workspace_id)
        print("The response of AtlassianApi->get_confluence_spaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtlassianApi->get_confluence_spaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**ConfluenceSpacesResponse**](ConfluenceSpacesResponse.md)

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

# **get_jira_assignees**
> JiraAssigneesResponse get_jira_assignees(project_key, workspace_id)

Get Jira Assignees

Get assignable users for a Jira project.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.jira_assignees_response import JiraAssigneesResponse
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
    api_instance = flowhunt.AtlassianApi(api_client)
    project_key = 'project_key_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Jira Assignees
        api_response = api_instance.get_jira_assignees(project_key, workspace_id)
        print("The response of AtlassianApi->get_jira_assignees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtlassianApi->get_jira_assignees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**JiraAssigneesResponse**](JiraAssigneesResponse.md)

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

# **get_jira_issues**
> JiraIssuesResponse get_jira_issues(project_key, workspace_id)

Get Jira Issues

Get issues for a Jira project.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.jira_issues_response import JiraIssuesResponse
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
    api_instance = flowhunt.AtlassianApi(api_client)
    project_key = 'project_key_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Jira Issues
        api_response = api_instance.get_jira_issues(project_key, workspace_id)
        print("The response of AtlassianApi->get_jira_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtlassianApi->get_jira_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**JiraIssuesResponse**](JiraIssuesResponse.md)

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

# **get_jira_projects**
> JiraProjectsResponse get_jira_projects(workspace_id)

Get Jira Projects

Get all Jira projects accessible through the workspace's Atlassian integration.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.jira_projects_response import JiraProjectsResponse
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
    api_instance = flowhunt.AtlassianApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Jira Projects
        api_response = api_instance.get_jira_projects(workspace_id)
        print("The response of AtlassianApi->get_jira_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtlassianApi->get_jira_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**JiraProjectsResponse**](JiraProjectsResponse.md)

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

# **get_jira_transitions**
> JiraTransitionsResponse get_jira_transitions(issue_key, workspace_id)

Get Jira Transitions

Get available transitions for a Jira issue.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.jira_transitions_response import JiraTransitionsResponse
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
    api_instance = flowhunt.AtlassianApi(api_client)
    issue_key = 'issue_key_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Jira Transitions
        api_response = api_instance.get_jira_transitions(issue_key, workspace_id)
        print("The response of AtlassianApi->get_jira_transitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtlassianApi->get_jira_transitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_key** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**JiraTransitionsResponse**](JiraTransitionsResponse.md)

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

