# flowhunt.FlowAssistantApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_flow_assistant_changes**](FlowAssistantApi.md#apply_flow_assistant_changes) | **POST** /v2/flow_assistants/apply_changes | Apply Flow Assistant Changes
[**create_flow_assistant_session**](FlowAssistantApi.md#create_flow_assistant_session) | **POST** /v2/flow_assistants/create | Create Flow Assistant Session
[**invoke_flow_assistant_response**](FlowAssistantApi.md#invoke_flow_assistant_response) | **POST** /v2/flow_assistants/{session_id}/invoke | Invoke Flow Assistant Response
[**poll_flow_assistant_response**](FlowAssistantApi.md#poll_flow_assistant_response) | **POST** /v2/flow_assistants/{session_id}/invocation_response/{from_timestamp} | Poll Flow Assistant Response
[**reject_flow_assistant_changes**](FlowAssistantApi.md#reject_flow_assistant_changes) | **POST** /v2/flow_assistants/reject_changes | Reject Flow Assistant Changes


# **apply_flow_assistant_changes**
> FlowDetailResponse apply_flow_assistant_changes(workspace_id, flow_assistant_apply_reject_changes_request)

Apply Flow Assistant Changes

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_assistant_apply_reject_changes_request import FlowAssistantApplyRejectChangesRequest
from flowhunt.models.flow_detail_response import FlowDetailResponse
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
    api_instance = flowhunt.FlowAssistantApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_assistant_apply_reject_changes_request = flowhunt.FlowAssistantApplyRejectChangesRequest() # FlowAssistantApplyRejectChangesRequest | 

    try:
        # Apply Flow Assistant Changes
        api_response = api_instance.apply_flow_assistant_changes(workspace_id, flow_assistant_apply_reject_changes_request)
        print("The response of FlowAssistantApi->apply_flow_assistant_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantApi->apply_flow_assistant_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_assistant_apply_reject_changes_request** | [**FlowAssistantApplyRejectChangesRequest**](FlowAssistantApplyRejectChangesRequest.md)|  | 

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flow_assistant_session**
> FlowSessionResponse create_flow_assistant_session(workspace_id, flow_assistant_session_create_request)

Create Flow Assistant Session

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
    api_instance = flowhunt.FlowAssistantApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_assistant_session_create_request = flowhunt.FlowAssistantSessionCreateRequest() # FlowAssistantSessionCreateRequest | 

    try:
        # Create Flow Assistant Session
        api_response = api_instance.create_flow_assistant_session(workspace_id, flow_assistant_session_create_request)
        print("The response of FlowAssistantApi->create_flow_assistant_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantApi->create_flow_assistant_session: %s\n" % e)
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

# **invoke_flow_assistant_response**
> FlowSessionInvocationResponse invoke_flow_assistant_response(session_id, flow_assistant_invoke_request)

Invoke Flow Assistant Response

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
    api_instance = flowhunt.FlowAssistantApi(api_client)
    session_id = 'session_id_example' # str | 
    flow_assistant_invoke_request = flowhunt.FlowAssistantInvokeRequest() # FlowAssistantInvokeRequest | 

    try:
        # Invoke Flow Assistant Response
        api_response = api_instance.invoke_flow_assistant_response(session_id, flow_assistant_invoke_request)
        print("The response of FlowAssistantApi->invoke_flow_assistant_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantApi->invoke_flow_assistant_response: %s\n" % e)
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

# **poll_flow_assistant_response**
> List[FlowSessionEvent] poll_flow_assistant_response(session_id, from_timestamp)

Poll Flow Assistant Response

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
    api_instance = flowhunt.FlowAssistantApi(api_client)
    session_id = 'session_id_example' # str | 
    from_timestamp = 'from_timestamp_example' # str | 

    try:
        # Poll Flow Assistant Response
        api_response = api_instance.poll_flow_assistant_response(session_id, from_timestamp)
        print("The response of FlowAssistantApi->poll_flow_assistant_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantApi->poll_flow_assistant_response: %s\n" % e)
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

# **reject_flow_assistant_changes**
> FlowDetailResponse reject_flow_assistant_changes(workspace_id, flow_assistant_apply_reject_changes_request)

Reject Flow Assistant Changes

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_assistant_apply_reject_changes_request import FlowAssistantApplyRejectChangesRequest
from flowhunt.models.flow_detail_response import FlowDetailResponse
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
    api_instance = flowhunt.FlowAssistantApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_assistant_apply_reject_changes_request = flowhunt.FlowAssistantApplyRejectChangesRequest() # FlowAssistantApplyRejectChangesRequest | 

    try:
        # Reject Flow Assistant Changes
        api_response = api_instance.reject_flow_assistant_changes(workspace_id, flow_assistant_apply_reject_changes_request)
        print("The response of FlowAssistantApi->reject_flow_assistant_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowAssistantApi->reject_flow_assistant_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_assistant_apply_reject_changes_request** | [**FlowAssistantApplyRejectChangesRequest**](FlowAssistantApplyRejectChangesRequest.md)|  | 

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

