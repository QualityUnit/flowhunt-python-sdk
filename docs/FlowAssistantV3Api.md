# flowhunt.FlowAssistantV3Api

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_v3_flow_assistant_session**](FlowAssistantV3Api.md#create_v3_flow_assistant_session) | **POST** /v3/flow-assistants/create | Create V3 Flow Assistant Session
[**invoke_v3_flow_assistant_response**](FlowAssistantV3Api.md#invoke_v3_flow_assistant_response) | **POST** /v3/flow-assistants/{session_id}/invoke | Invoke V3 Flow Assistant Response
[**poll_v3_flow_assistant_response**](FlowAssistantV3Api.md#poll_v3_flow_assistant_response) | **POST** /v3/flow-assistants/{session_id}/invocation_response/{from_timestamp} | Poll V3 Flow Assistant Response


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
    api_instance = flowhunt.FlowAssistantV3Api(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_assistant_session_create_request = flowhunt.FlowAssistantSessionCreateRequest() # FlowAssistantSessionCreateRequest | 

    try:
        # Create V3 Flow Assistant Session
        api_response = api_instance.create_v3_flow_assistant_session(workspace_id, flow_assistant_session_create_request)
        print("The response of FlowAssistantV3Api->create_v3_flow_assistant_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantV3Api->create_v3_flow_assistant_session: %s\n" % e)
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
    api_instance = flowhunt.FlowAssistantV3Api(api_client)
    session_id = 'session_id_example' # str | 
    flow_assistant_invoke_request = flowhunt.FlowAssistantInvokeRequest() # FlowAssistantInvokeRequest | 

    try:
        # Invoke V3 Flow Assistant Response
        api_response = api_instance.invoke_v3_flow_assistant_response(session_id, flow_assistant_invoke_request)
        print("The response of FlowAssistantV3Api->invoke_v3_flow_assistant_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantV3Api->invoke_v3_flow_assistant_response: %s\n" % e)
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
    api_instance = flowhunt.FlowAssistantV3Api(api_client)
    session_id = 'session_id_example' # str | 
    from_timestamp = 'from_timestamp_example' # str | 

    try:
        # Poll V3 Flow Assistant Response
        api_response = api_instance.poll_v3_flow_assistant_response(session_id, from_timestamp)
        print("The response of FlowAssistantV3Api->poll_v3_flow_assistant_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantV3Api->poll_v3_flow_assistant_response: %s\n" % e)
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

