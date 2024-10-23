# flowhunt.FlowSessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_chatbot_session_view**](FlowSessionsApi.md#delete_chatbot_session_view) | **DELETE** /v2/chatbots/sessions/{session_id} | Delete Chatbot Session View
[**get_chatbot_session_view**](FlowSessionsApi.md#get_chatbot_session_view) | **GET** /v2/chatbots/sessions/{session_id} | Get Chatbot Session View
[**search_chatbot_sessions_view**](FlowSessionsApi.md#search_chatbot_sessions_view) | **POST** /v2/chatbots/sessions/search | Search Chatbot Sessions View
[**update_chatbot_session_view**](FlowSessionsApi.md#update_chatbot_session_view) | **PUT** /v2/chatbots/sessions/{session_id} | Update Chatbot Session View


# **delete_chatbot_session_view**
> Completed delete_chatbot_session_view(session_id, workspace_id)

Delete Chatbot Session View

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FlowSessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Chatbot Session View
        api_response = api_instance.delete_chatbot_session_view(session_id, workspace_id)
        print("The response of FlowSessionsApi->delete_chatbot_session_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowSessionsApi->delete_chatbot_session_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_chatbot_session_view**
> FlowSessionViewResponse get_chatbot_session_view(session_id, workspace_id)

Get Chatbot Session View

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_view_response import FlowSessionViewResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FlowSessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Chatbot Session View
        api_response = api_instance.get_chatbot_session_view(session_id, workspace_id)
        print("The response of FlowSessionsApi->get_chatbot_session_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowSessionsApi->get_chatbot_session_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **search_chatbot_sessions_view**
> List[FlowSessionViewResponse] search_chatbot_sessions_view(workspace_id, flow_session_view_search_request)

Search Chatbot Sessions View

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_view_response import FlowSessionViewResponse
from flowhunt.models.flow_session_view_search_request import FlowSessionViewSearchRequest
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FlowSessionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_session_view_search_request = flowhunt.FlowSessionViewSearchRequest() # FlowSessionViewSearchRequest | 

    try:
        # Search Chatbot Sessions View
        api_response = api_instance.search_chatbot_sessions_view(workspace_id, flow_session_view_search_request)
        print("The response of FlowSessionsApi->search_chatbot_sessions_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowSessionsApi->search_chatbot_sessions_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_session_view_search_request** | [**FlowSessionViewSearchRequest**](FlowSessionViewSearchRequest.md)|  | 

### Return type

[**List[FlowSessionViewResponse]**](FlowSessionViewResponse.md)

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

# **update_chatbot_session_view**
> FlowSessionViewResponse update_chatbot_session_view(session_id, workspace_id, flow_session_view_update_request)

Update Chatbot Session View

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_view_response import FlowSessionViewResponse
from flowhunt.models.flow_session_view_update_request import FlowSessionViewUpdateRequest
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
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
    api_instance = flowhunt.FlowSessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_session_view_update_request = flowhunt.FlowSessionViewUpdateRequest() # FlowSessionViewUpdateRequest | 

    try:
        # Update Chatbot Session View
        api_response = api_instance.update_chatbot_session_view(session_id, workspace_id, flow_session_view_update_request)
        print("The response of FlowSessionsApi->update_chatbot_session_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowSessionsApi->update_chatbot_session_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_session_view_update_request** | [**FlowSessionViewUpdateRequest**](FlowSessionViewUpdateRequest.md)|  | 

### Return type

[**FlowSessionViewResponse**](FlowSessionViewResponse.md)

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

