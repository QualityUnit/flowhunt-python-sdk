# flowhunt.AgentTeamProjectsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_chat**](AgentTeamProjectsApi.md#cancel_chat) | **POST** /v2/projects/{project_id}/chat/{session_id}/cancel | Cancel Chat
[**create_project**](AgentTeamProjectsApi.md#create_project) | **POST** /v2/projects/create | Create Project
[**delete_agent_team_project**](AgentTeamProjectsApi.md#delete_agent_team_project) | **DELETE** /v2/projects/{project_id} | Delete Agent Team Project
[**generate_suggestions**](AgentTeamProjectsApi.md#generate_suggestions) | **POST** /v2/projects/{project_id}/suggestions/generate | Generate Suggestions
[**generate_title**](AgentTeamProjectsApi.md#generate_title) | **POST** /v2/projects/{project_id}/chat/{session_id}/generate-title | Generate Title
[**get_project**](AgentTeamProjectsApi.md#get_project) | **GET** /v2/projects/{project_id} | Get Project
[**get_suggestions**](AgentTeamProjectsApi.md#get_suggestions) | **GET** /v2/projects/{project_id}/suggestions | Get Suggestions
[**hitl_respond**](AgentTeamProjectsApi.md#hitl_respond) | **POST** /v2/projects/{project_id}/chat/{session_id}/hitl-respond | Hitl Respond
[**poll_chat**](AgentTeamProjectsApi.md#poll_chat) | **POST** /v2/projects/{project_id}/chat/{session_id}/events/{from_timestamp} | Poll Chat
[**poll_generate_agent_config**](AgentTeamProjectsApi.md#poll_generate_agent_config) | **POST** /v2/projects/generate-agent-config/{session_id}/events/{from_timestamp} | Poll Generate Agent Config
[**search_projects**](AgentTeamProjectsApi.md#search_projects) | **POST** /v2/projects/ | Search Projects
[**start_chat**](AgentTeamProjectsApi.md#start_chat) | **POST** /v2/projects/{project_id}/chat | Start Chat
[**start_generate_agent_config**](AgentTeamProjectsApi.md#start_generate_agent_config) | **POST** /v2/projects/generate-agent-config | Start Generate Agent Config
[**test_channel_connection**](AgentTeamProjectsApi.md#test_channel_connection) | **POST** /v2/projects/channels/test | Test Channel Connection
[**update_project**](AgentTeamProjectsApi.md#update_project) | **PUT** /v2/projects/{project_id} | Update Project


# **cancel_chat**
> Completed cancel_chat(project_id, session_id, workspace_id)

Cancel Chat

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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    session_id = 'session_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Cancel Chat
        api_response = api_instance.cancel_chat(project_id, session_id, workspace_id)
        print("The response of AgentTeamProjectsApi->cancel_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->cancel_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **session_id** | **str**|  | 
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

# **create_project**
> AgentTeamProjectResponse create_project(workspace_id, agent_team_project_create)

Create Project

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_team_project_create import AgentTeamProjectCreate
from flowhunt.models.agent_team_project_response import AgentTeamProjectResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    agent_team_project_create = flowhunt.AgentTeamProjectCreate() # AgentTeamProjectCreate | 

    try:
        # Create Project
        api_response = api_instance.create_project(workspace_id, agent_team_project_create)
        print("The response of AgentTeamProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **agent_team_project_create** | [**AgentTeamProjectCreate**](AgentTeamProjectCreate.md)|  | 

### Return type

[**AgentTeamProjectResponse**](AgentTeamProjectResponse.md)

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

# **delete_agent_team_project**
> Completed delete_agent_team_project(project_id, workspace_id)

Delete Agent Team Project

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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Agent Team Project
        api_response = api_instance.delete_agent_team_project(project_id, workspace_id)
        print("The response of AgentTeamProjectsApi->delete_agent_team_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->delete_agent_team_project: %s\n" % e)
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

# **generate_suggestions**
> List[SuggestionResponse] generate_suggestions(project_id, workspace_id)

Generate Suggestions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.suggestion_response import SuggestionResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Generate Suggestions
        api_response = api_instance.generate_suggestions(project_id, workspace_id)
        print("The response of AgentTeamProjectsApi->generate_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->generate_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[SuggestionResponse]**](SuggestionResponse.md)

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

# **generate_title**
> FlowSessionViewResponse generate_title(project_id, session_id, workspace_id)

Generate Title

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_view_response import FlowSessionViewResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    session_id = 'session_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Generate Title
        api_response = api_instance.generate_title(project_id, session_id, workspace_id)
        print("The response of AgentTeamProjectsApi->generate_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->generate_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **session_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**FlowSessionViewResponse**](FlowSessionViewResponse.md)

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

# **get_project**
> AgentTeamProjectResponse get_project(project_id, workspace_id)

Get Project

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_team_project_response import AgentTeamProjectResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Project
        api_response = api_instance.get_project(project_id, workspace_id)
        print("The response of AgentTeamProjectsApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**AgentTeamProjectResponse**](AgentTeamProjectResponse.md)

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

# **get_suggestions**
> List[SuggestionResponse] get_suggestions(project_id, workspace_id)

Get Suggestions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.suggestion_response import SuggestionResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Suggestions
        api_response = api_instance.get_suggestions(project_id, workspace_id)
        print("The response of AgentTeamProjectsApi->get_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->get_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[SuggestionResponse]**](SuggestionResponse.md)

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

# **hitl_respond**
> Completed hitl_respond(project_id, session_id, workspace_id, hitl_respond_request)

Hitl Respond

Respond to an HITL tool approval request from the dashboard UI.

Emits a ``task.hitl_resolved`` signal on the ``agent_team_comms`` stream
so the stream step resumes and the router can re-spawn the agent.
This is durable and works across process restarts / multiple nodes.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.hitl_respond_request import HITLRespondRequest
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    session_id = 'session_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    hitl_respond_request = flowhunt.HITLRespondRequest() # HITLRespondRequest | 

    try:
        # Hitl Respond
        api_response = api_instance.hitl_respond(project_id, session_id, workspace_id, hitl_respond_request)
        print("The response of AgentTeamProjectsApi->hitl_respond:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->hitl_respond: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **session_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **hitl_respond_request** | [**HITLRespondRequest**](HITLRespondRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **poll_chat**
> List[FlowSessionEvent] poll_chat(project_id, session_id, from_timestamp, workspace_id)

Poll Chat

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_event import FlowSessionEvent
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    session_id = 'session_id_example' # str | 
    from_timestamp = 'from_timestamp_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Poll Chat
        api_response = api_instance.poll_chat(project_id, session_id, from_timestamp, workspace_id)
        print("The response of AgentTeamProjectsApi->poll_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->poll_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **session_id** | **str**|  | 
 **from_timestamp** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[FlowSessionEvent]**](FlowSessionEvent.md)

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

# **poll_generate_agent_config**
> List[FlowSessionEvent] poll_generate_agent_config(session_id, from_timestamp, workspace_id)

Poll Generate Agent Config

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_event import FlowSessionEvent
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    session_id = 'session_id_example' # str | 
    from_timestamp = 'from_timestamp_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Poll Generate Agent Config
        api_response = api_instance.poll_generate_agent_config(session_id, from_timestamp, workspace_id)
        print("The response of AgentTeamProjectsApi->poll_generate_agent_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->poll_generate_agent_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **from_timestamp** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[FlowSessionEvent]**](FlowSessionEvent.md)

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

# **search_projects**
> List[AgentTeamProjectResponse] search_projects(workspace_id, agent_team_project_search_request)

Search Projects

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_team_project_response import AgentTeamProjectResponse
from flowhunt.models.agent_team_project_search_request import AgentTeamProjectSearchRequest
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    agent_team_project_search_request = flowhunt.AgentTeamProjectSearchRequest() # AgentTeamProjectSearchRequest | 

    try:
        # Search Projects
        api_response = api_instance.search_projects(workspace_id, agent_team_project_search_request)
        print("The response of AgentTeamProjectsApi->search_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->search_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **agent_team_project_search_request** | [**AgentTeamProjectSearchRequest**](AgentTeamProjectSearchRequest.md)|  | 

### Return type

[**List[AgentTeamProjectResponse]**](AgentTeamProjectResponse.md)

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

# **start_chat**
> ChatStartResponse start_chat(project_id, workspace_id, agent_team_project_chat_request)

Start Chat

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_team_project_chat_request import AgentTeamProjectChatRequest
from flowhunt.models.chat_start_response import ChatStartResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    agent_team_project_chat_request = flowhunt.AgentTeamProjectChatRequest() # AgentTeamProjectChatRequest | 

    try:
        # Start Chat
        api_response = api_instance.start_chat(project_id, workspace_id, agent_team_project_chat_request)
        print("The response of AgentTeamProjectsApi->start_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->start_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **agent_team_project_chat_request** | [**AgentTeamProjectChatRequest**](AgentTeamProjectChatRequest.md)|  | 

### Return type

[**ChatStartResponse**](ChatStartResponse.md)

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

# **start_generate_agent_config**
> GenerateAgentConfigStartResponse start_generate_agent_config(workspace_id, generate_agent_config_request)

Start Generate Agent Config

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.generate_agent_config_request import GenerateAgentConfigRequest
from flowhunt.models.generate_agent_config_start_response import GenerateAgentConfigStartResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    generate_agent_config_request = flowhunt.GenerateAgentConfigRequest() # GenerateAgentConfigRequest | 

    try:
        # Start Generate Agent Config
        api_response = api_instance.start_generate_agent_config(workspace_id, generate_agent_config_request)
        print("The response of AgentTeamProjectsApi->start_generate_agent_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->start_generate_agent_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **generate_agent_config_request** | [**GenerateAgentConfigRequest**](GenerateAgentConfigRequest.md)|  | 

### Return type

[**GenerateAgentConfigStartResponse**](GenerateAgentConfigStartResponse.md)

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

# **test_channel_connection**
> ChannelTestResponse test_channel_connection(workspace_id, channel_test_request)

Test Channel Connection

Send a test message to the configured channel.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.channel_test_request import ChannelTestRequest
from flowhunt.models.channel_test_response import ChannelTestResponse
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    channel_test_request = flowhunt.ChannelTestRequest() # ChannelTestRequest | 

    try:
        # Test Channel Connection
        api_response = api_instance.test_channel_connection(workspace_id, channel_test_request)
        print("The response of AgentTeamProjectsApi->test_channel_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->test_channel_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **channel_test_request** | [**ChannelTestRequest**](ChannelTestRequest.md)|  | 

### Return type

[**ChannelTestResponse**](ChannelTestResponse.md)

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

# **update_project**
> AgentTeamProjectResponse update_project(project_id, workspace_id, agent_team_project_update)

Update Project

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_team_project_response import AgentTeamProjectResponse
from flowhunt.models.agent_team_project_update import AgentTeamProjectUpdate
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
    api_instance = flowhunt.AgentTeamProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    agent_team_project_update = flowhunt.AgentTeamProjectUpdate() # AgentTeamProjectUpdate | 

    try:
        # Update Project
        api_response = api_instance.update_project(project_id, workspace_id, agent_team_project_update)
        print("The response of AgentTeamProjectsApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentTeamProjectsApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **agent_team_project_update** | [**AgentTeamProjectUpdate**](AgentTeamProjectUpdate.md)|  | 

### Return type

[**AgentTeamProjectResponse**](AgentTeamProjectResponse.md)

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

