# flowhunt.V3Api

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_migration_readiness**](V3Api.md#check_migration_readiness) | **GET** /v3/flows/{flow_id}/migration-readiness | Check Migration Readiness
[**create_v3_flow_assistant_session**](V3Api.md#create_v3_flow_assistant_session) | **POST** /v3/flow-assistants/create | Create V3 Flow Assistant Session
[**get_all_components_v3**](V3Api.md#get_all_components_v3) | **GET** /v3/flows/components/all | Get All Components V3
[**get_tool**](V3Api.md#get_tool) | **GET** /v3/tools/{step_name} | Get Tool
[**get_v3_components**](V3Api.md#get_v3_components) | **GET** /v3/flows/components/v3 | Get V3 Components
[**invoke_v3_flow_assistant_response**](V3Api.md#invoke_v3_flow_assistant_response) | **POST** /v3/flow-assistants/{session_id}/invoke | Invoke V3 Flow Assistant Response
[**list_tools**](V3Api.md#list_tools) | **GET** /v3/tools | List Tools
[**migrate_flow_to_v3**](V3Api.md#migrate_flow_to_v3) | **POST** /v3/flows/{flow_id}/migrate-to-v3 | Migrate Flow To V3
[**poll_v3_flow_assistant_response**](V3Api.md#poll_v3_flow_assistant_response) | **POST** /v3/flow-assistants/{session_id}/invocation_response/{from_timestamp} | Poll V3 Flow Assistant Response
[**validate_component**](V3Api.md#validate_component) | **POST** /v3/flows/components/{component_id}/validate | Validate Component
[**validate_flow**](V3Api.md#validate_flow) | **POST** /v3/flows/validate | Validate Flow


# **check_migration_readiness**
> Dict[str, object] check_migration_readiness(flow_id, workspace_id)

Check Migration Readiness

Check if a flow is ready to be migrated to v3.

Returns information about:
- Whether the flow can be migrated
- Current engine version
- Incompatible components (if any)
- List of available v3 components

Args:
    workspace_id: The workspace ID
    flow_id: The flow ID to check
    flow_v3_controller: Injected controller
    user: Current authenticated user

Returns:
    Dict with migration readiness information

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Check Migration Readiness
        api_response = api_instance.check_migration_readiness(flow_id, workspace_id)
        print("The response of V3Api->check_migration_readiness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->check_migration_readiness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_v3_flow_assistant_session**
> FlowSessionResponse create_v3_flow_assistant_session(workspace_id, flow_assistant_session_create_request)

Create V3 Flow Assistant Session

Create a new assistant session.

Returns session_id and created_at for the new session.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_assistant_session_create_request import FlowAssistantSessionCreateRequest
from flowhunt.models.flow_session_response import FlowSessionResponse
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
    api_instance = flowhunt.V3Api(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_assistant_session_create_request = flowhunt.FlowAssistantSessionCreateRequest() # FlowAssistantSessionCreateRequest | 

    try:
        # Create V3 Flow Assistant Session
        api_response = api_instance.create_v3_flow_assistant_session(workspace_id, flow_assistant_session_create_request)
        print("The response of V3Api->create_v3_flow_assistant_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->create_v3_flow_assistant_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_assistant_session_create_request** | [**FlowAssistantSessionCreateRequest**](FlowAssistantSessionCreateRequest.md)|  | 

### Return type

[**FlowSessionResponse**](FlowSessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_components_v3**
> Dict[str, object] get_all_components_v3()

Get All Components V3

Get all v3 components with full metadata, organized by category.

Returns V2-compatible component structure with rich metadata including:
- display_name, description, icon
- Parameter definitions with types, defaults, UI field types
- Output field definitions
- Category organization

This endpoint is compatible with the v2 flow editor UI.

Returns:
    Dict mapping category names to component definitions.
    Example: {"inputs": {"ChatInput": {...}}, "llms": {"OpenAILLM": {...}}}

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)

    try:
        # Get All Components V3
        api_response = api_instance.get_all_components_v3()
        print("The response of V3Api->get_all_components_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->get_all_components_v3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tool**
> V3ToolResponse get_tool(step_name, workspace_id)

Get Tool

Get a specific tool with full parameter details.

Returns detailed information about a tool including all parameters
that can be configured or locked.

Args:
    workspace_id: The workspace ID
    step_name: The step name to retrieve
    tools_controller: Injected controller
    user: Current authenticated user

Returns:
    V3ToolResponse with full tool details

Raises:
    404: If tool not found

### Example


```python
import flowhunt
from flowhunt.models.v3_tool_response import V3ToolResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    step_name = 'step_name_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Tool
        api_response = api_instance.get_tool(step_name, workspace_id)
        print("The response of V3Api->get_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->get_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **step_name** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**V3ToolResponse**](V3ToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v3_components**
> Dict[str, object] get_v3_components()

Get V3 Components

Get list of v3-compatible components.

Returns:
    Dict with list of registered v3 components and count

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)

    try:
        # Get V3 Components
        api_response = api_instance.get_v3_components()
        print("The response of V3Api->get_v3_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->get_v3_components: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_v3_flow_assistant_response**
> FlowSessionInvocationResponse invoke_v3_flow_assistant_response(session_id, flow_assistant_invoke_request)

Invoke V3 Flow Assistant Response

Start an assistant invocation.

Returns immediately - client polls for events via invocation_response endpoint.

### Example


```python
import flowhunt
from flowhunt.models.flow_assistant_invoke_request import FlowAssistantInvokeRequest
from flowhunt.models.flow_session_invocation_response import FlowSessionInvocationResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    session_id = 'session_id_example' # str | 
    flow_assistant_invoke_request = flowhunt.FlowAssistantInvokeRequest() # FlowAssistantInvokeRequest | 

    try:
        # Invoke V3 Flow Assistant Response
        api_response = api_instance.invoke_v3_flow_assistant_response(session_id, flow_assistant_invoke_request)
        print("The response of V3Api->invoke_v3_flow_assistant_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->invoke_v3_flow_assistant_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **flow_assistant_invoke_request** | [**FlowAssistantInvokeRequest**](FlowAssistantInvokeRequest.md)|  | 

### Return type

[**FlowSessionInvocationResponse**](FlowSessionInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tools**
> V3ToolListResponse list_tools(workspace_id, search=search, category=category)

List Tools

List all available V3 tools.

Returns a list of tools that can be used with AI Agents.
Supports optional search and category filtering.

Args:
    workspace_id: The workspace ID
    search: Optional search query
    category: Optional category filter
    tools_controller: Injected controller
    user: Current authenticated user

Returns:
    V3ToolListResponse with list of available tools

### Example


```python
import flowhunt
from flowhunt.models.v3_tool_list_response import V3ToolListResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    workspace_id = 'workspace_id_example' # str | 
    search = 'search_example' # str | Search query for tool name, description, or category (optional)
    category = 'category_example' # str | Filter by category (optional)

    try:
        # List Tools
        api_response = api_instance.list_tools(workspace_id, search=search, category=category)
        print("The response of V3Api->list_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->list_tools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **search** | **str**| Search query for tool name, description, or category | [optional] 
 **category** | **str**| Filter by category | [optional] 

### Return type

[**V3ToolListResponse**](V3ToolListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_flow_to_v3**
> FlowDetailResponse migrate_flow_to_v3(flow_id, workspace_id, force=force, remove_incompatible=remove_incompatible)

Migrate Flow To V3

Migrate a v2 flow to v3 engine.

This endpoint:
1. Validates that all components in the flow are v3-compatible
2. Creates a new draft version of the flow with engine_version='v3'
3. Returns the migrated flow details

Args:
    workspace_id: The workspace ID
    flow_id: The flow ID to migrate
    force: If True, skip compatibility check (dangerous!)
    remove_incompatible: If True, remove incompatible components instead of failing
    flow_v3_controller: Injected controller
    user: Current authenticated user

Returns:
    FlowDetailResponse with the migrated flow

### Example


```python
import flowhunt
from flowhunt.models.flow_detail_response import FlowDetailResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    force = False # bool | Skip compatibility check if True (optional) (default to False)
    remove_incompatible = False # bool | Remove incompatible components instead of failing (optional) (default to False)

    try:
        # Migrate Flow To V3
        api_response = api_instance.migrate_flow_to_v3(flow_id, workspace_id, force=force, remove_incompatible=remove_incompatible)
        print("The response of V3Api->migrate_flow_to_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->migrate_flow_to_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **force** | **bool**| Skip compatibility check if True | [optional] [default to False]
 **remove_incompatible** | **bool**| Remove incompatible components instead of failing | [optional] [default to False]

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_v3_flow_assistant_response**
> List[FlowSessionEvent] poll_v3_flow_assistant_response(session_id, from_timestamp)

Poll V3 Flow Assistant Response

Poll for events after the given timestamp.

Used by client to receive streamed responses from the assistant.

### Example


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


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    session_id = 'session_id_example' # str | 
    from_timestamp = 'from_timestamp_example' # str | 

    try:
        # Poll V3 Flow Assistant Response
        api_response = api_instance.poll_v3_flow_assistant_response(session_id, from_timestamp)
        print("The response of V3Api->poll_v3_flow_assistant_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->poll_v3_flow_assistant_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **from_timestamp** | **str**|  | 

### Return type

[**List[FlowSessionEvent]**](FlowSessionEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_component**
> ComponentValidationResponse validate_component(component_id, component_validate_request)

Validate Component

Validate a V3 component configuration.

Validates that all required parameters have values and performs
any component-specific validation rules.

Args:
    component_id: The component type to validate (e.g., "OpenAILLM")
    request: Request body with template values

Returns:
    ComponentValidationResponse with is_valid flag and error list

### Example


```python
import flowhunt
from flowhunt.models.component_validate_request import ComponentValidateRequest
from flowhunt.models.component_validation_response import ComponentValidationResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    component_id = 'component_id_example' # str | 
    component_validate_request = flowhunt.ComponentValidateRequest() # ComponentValidateRequest | 

    try:
        # Validate Component
        api_response = api_instance.validate_component(component_id, component_validate_request)
        print("The response of V3Api->validate_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->validate_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**|  | 
 **component_validate_request** | [**ComponentValidateRequest**](ComponentValidateRequest.md)|  | 

### Return type

[**ComponentValidationResponse**](ComponentValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_flow**
> FlowValidationResponse validate_flow(flow_validate_request)

Validate Flow

Validate an entire V3 flow before publishing.

Validates all nodes in the flow, checking that required parameters
have values and all component configurations are valid.

Args:
    request: Request body with list of nodes to validate

Returns:
    FlowValidationResponse with is_valid flag and list of errors
    including node_id and component_type for each error

### Example


```python
import flowhunt
from flowhunt.models.flow_validate_request import FlowValidateRequest
from flowhunt.models.flow_validation_response import FlowValidationResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.V3Api(api_client)
    flow_validate_request = flowhunt.FlowValidateRequest() # FlowValidateRequest | 

    try:
        # Validate Flow
        api_response = api_instance.validate_flow(flow_validate_request)
        print("The response of V3Api->validate_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V3Api->validate_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_validate_request** | [**FlowValidateRequest**](FlowValidateRequest.md)|  | 

### Return type

[**FlowValidationResponse**](FlowValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

