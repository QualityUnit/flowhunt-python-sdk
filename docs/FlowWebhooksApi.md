# flowhunt.FlowWebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_webhook**](FlowWebhooksApi.md#execute_webhook) | **POST** /v2/flows/webhooks/{chatbot_id} | Execute Webhook
[**execute_webhook_from_flow**](FlowWebhooksApi.md#execute_webhook_from_flow) | **POST** /v2/flows/webhooks/from_flow/{flow_id} | Execute Webhook From Flow
[**poll_webhook_response**](FlowWebhooksApi.md#poll_webhook_response) | **POST** /v2/flows/webhooks/invocation_response/{message_id} | Poll Webhook Response


# **execute_webhook**
> FlowSessionInvocationResponse execute_webhook(chatbot_id, workspace_id, trigger_type)

Execute Webhook

### Example


```python
import flowhunt
from flowhunt.models.flow_session_invocation_response import FlowSessionInvocationResponse
from flowhunt.models.trigger_type import TriggerType
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.FlowWebhooksApi(api_client)
    chatbot_id = 'chatbot_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    trigger_type = flowhunt.TriggerType() # TriggerType | 

    try:
        # Execute Webhook
        api_response = api_instance.execute_webhook(chatbot_id, workspace_id, trigger_type)
        print("The response of FlowWebhooksApi->execute_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowWebhooksApi->execute_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatbot_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **trigger_type** | [**TriggerType**](.md)|  | 

### Return type

[**FlowSessionInvocationResponse**](FlowSessionInvocationResponse.md)

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

# **execute_webhook_from_flow**
> FlowSessionInvocationResponse execute_webhook_from_flow(flow_id, workspace_id, trigger_type)

Execute Webhook From Flow

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_invocation_response import FlowSessionInvocationResponse
from flowhunt.models.trigger_type import TriggerType
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
    api_instance = flowhunt.FlowWebhooksApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    trigger_type = flowhunt.TriggerType() # TriggerType | 

    try:
        # Execute Webhook From Flow
        api_response = api_instance.execute_webhook_from_flow(flow_id, workspace_id, trigger_type)
        print("The response of FlowWebhooksApi->execute_webhook_from_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowWebhooksApi->execute_webhook_from_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **trigger_type** | [**TriggerType**](.md)|  | 

### Return type

[**FlowSessionInvocationResponse**](FlowSessionInvocationResponse.md)

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

# **poll_webhook_response**
> FlowSessionInvocationMessageResponse poll_webhook_response(message_id)

Poll Webhook Response

### Example


```python
import flowhunt
from flowhunt.models.flow_session_invocation_message_response import FlowSessionInvocationMessageResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.FlowWebhooksApi(api_client)
    message_id = 'message_id_example' # str | 

    try:
        # Poll Webhook Response
        api_response = api_instance.poll_webhook_response(message_id)
        print("The response of FlowWebhooksApi->poll_webhook_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowWebhooksApi->poll_webhook_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

### Return type

[**FlowSessionInvocationMessageResponse**](FlowSessionInvocationMessageResponse.md)

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

