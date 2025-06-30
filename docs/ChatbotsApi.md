# flowhunt.ChatbotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chatbot**](ChatbotsApi.md#create_chatbot) | **POST** /v2/chatbots/create | Create Chatbot
[**delete_chatbot**](ChatbotsApi.md#delete_chatbot) | **DELETE** /v2/chatbots/{chatbot_id} | Delete Chatbot
[**get_chatbot**](ChatbotsApi.md#get_chatbot) | **GET** /v2/chatbots/{chatbot_id} | Get Chatbot
[**search_chatbots**](ChatbotsApi.md#search_chatbots) | **POST** /v2/chatbots/ | Search Chatbots
[**update_chatbot**](ChatbotsApi.md#update_chatbot) | **PUT** /v2/chatbots/{chatbot_id} | Update Chatbot


# **create_chatbot**
> ChatbotResponse create_chatbot(workspace_id, chatbot_create_request)

Create Chatbot

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.chatbot_create_request import ChatbotCreateRequest
from flowhunt.models.chatbot_response import ChatbotResponse
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
    api_instance = flowhunt.ChatbotsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    chatbot_create_request = flowhunt.ChatbotCreateRequest() # ChatbotCreateRequest | 

    try:
        # Create Chatbot
        api_response = api_instance.create_chatbot(workspace_id, chatbot_create_request)
        print("The response of ChatbotsApi->create_chatbot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatbotsApi->create_chatbot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **chatbot_create_request** | [**ChatbotCreateRequest**](ChatbotCreateRequest.md)|  | 

### Return type

[**ChatbotResponse**](ChatbotResponse.md)

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

# **delete_chatbot**
> Completed delete_chatbot(chatbot_id, workspace_id)

Delete Chatbot

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
    api_instance = flowhunt.ChatbotsApi(api_client)
    chatbot_id = 'chatbot_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Chatbot
        api_response = api_instance.delete_chatbot(chatbot_id, workspace_id)
        print("The response of ChatbotsApi->delete_chatbot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatbotsApi->delete_chatbot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatbot_id** | **str**|  | 
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

# **get_chatbot**
> ChatbotResponse get_chatbot(chatbot_id, workspace_id)

Get Chatbot

### Example


```python
import flowhunt
from flowhunt.models.chatbot_response import ChatbotResponse
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
    api_instance = flowhunt.ChatbotsApi(api_client)
    chatbot_id = 'chatbot_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Chatbot
        api_response = api_instance.get_chatbot(chatbot_id, workspace_id)
        print("The response of ChatbotsApi->get_chatbot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatbotsApi->get_chatbot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatbot_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ChatbotResponse**](ChatbotResponse.md)

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

# **search_chatbots**
> List[ChatbotResponse] search_chatbots(workspace_id, chatbot_search_request)

Search Chatbots

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.chatbot_response import ChatbotResponse
from flowhunt.models.chatbot_search_request import ChatbotSearchRequest
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
    api_instance = flowhunt.ChatbotsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    chatbot_search_request = flowhunt.ChatbotSearchRequest() # ChatbotSearchRequest | 

    try:
        # Search Chatbots
        api_response = api_instance.search_chatbots(workspace_id, chatbot_search_request)
        print("The response of ChatbotsApi->search_chatbots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatbotsApi->search_chatbots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **chatbot_search_request** | [**ChatbotSearchRequest**](ChatbotSearchRequest.md)|  | 

### Return type

[**List[ChatbotResponse]**](ChatbotResponse.md)

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

# **update_chatbot**
> ChatbotResponse update_chatbot(chatbot_id, workspace_id, chatbot_update_request)

Update Chatbot

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.chatbot_response import ChatbotResponse
from flowhunt.models.chatbot_update_request import ChatbotUpdateRequest
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
    api_instance = flowhunt.ChatbotsApi(api_client)
    chatbot_id = 'chatbot_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    chatbot_update_request = flowhunt.ChatbotUpdateRequest() # ChatbotUpdateRequest | 

    try:
        # Update Chatbot
        api_response = api_instance.update_chatbot(chatbot_id, workspace_id, chatbot_update_request)
        print("The response of ChatbotsApi->update_chatbot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatbotsApi->update_chatbot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatbot_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **chatbot_update_request** | [**ChatbotUpdateRequest**](ChatbotUpdateRequest.md)|  | 

### Return type

[**ChatbotResponse**](ChatbotResponse.md)

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

