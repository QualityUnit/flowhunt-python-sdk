# flowhunt.FlowsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chatbot_session**](FlowsApi.md#create_chatbot_session) | **POST** /v2/flows/sessions/create | Create Chatbot Session
[**create_flow**](FlowsApi.md#create_flow) | **POST** /v2/flows/create | Create Flow
[**create_flow_category**](FlowsApi.md#create_flow_category) | **POST** /v2/flows/categories/create | Create Flow Category
[**create_flow_cron**](FlowsApi.md#create_flow_cron) | **POST** /v2/flows/crons/create | Create Flow Cron
[**create_flow_session**](FlowsApi.md#create_flow_session) | **POST** /v2/flows/sessions/from_flow/create | Create Flow Session
[**delete_attachment**](FlowsApi.md#delete_attachment) | **DELETE** /v2/flows/sessions/{session_id}/attachments/{file_id} | Delete Attachment
[**delete_flow**](FlowsApi.md#delete_flow) | **DELETE** /v2/flows/{flow_id} | Delete Flow
[**delete_flow_category**](FlowsApi.md#delete_flow_category) | **DELETE** /v2/flows/categories/{cat_id} | Delete Flow Category
[**delete_flow_cron**](FlowsApi.md#delete_flow_cron) | **DELETE** /v2/flows/crons/{flow_id}/{cron_id} | Delete Flow Cron
[**execute_flow_cron**](FlowsApi.md#execute_flow_cron) | **POST** /v2/flows/crons/{flow_id}/{cron_id}/execute | Execute Flow Cron
[**generate_commit_message**](FlowsApi.md#generate_commit_message) | **POST** /v2/flows/{flow_id}/generate-commit-msg | Generate Commit Message
[**get**](FlowsApi.md#get) | **GET** /v2/flows/{flow_id} | Get
[**get_all_components**](FlowsApi.md#get_all_components) | **GET** /v2/flows/components/all | Get All Components
[**get_attachments**](FlowsApi.md#get_attachments) | **GET** /v2/flows/sessions/{session_id}/attachments | Get Attachments
[**get_flow_versions**](FlowsApi.md#get_flow_versions) | **GET** /v2/flows/{flow_id}/version_history | Get Flow Versions
[**get_invoked_flow_results**](FlowsApi.md#get_invoked_flow_results) | **GET** /v2/flows/{flow_id}/{task_id} | Get Invoked Flow Results
[**get_public_flow**](FlowsApi.md#get_public_flow) | **GET** /v2/flows/public/{flow_id} | Get Public Flow
[**get_trigger_types**](FlowsApi.md#get_trigger_types) | **POST** /v2/flows/{flow_id}/triggers | Get Trigger Types
[**invoke_flow**](FlowsApi.md#invoke_flow) | **POST** /v2/flows/{flow_id}/invoke | Invoke Flow
[**invoke_flow_response**](FlowsApi.md#invoke_flow_response) | **POST** /v2/flows/sessions/{session_id}/invoke | Invoke Flow Response
[**invoke_flow_singleton**](FlowsApi.md#invoke_flow_singleton) | **POST** /v2/flows/{flow_id}/invoke_singleton | Invoke Flow Singleton
[**poll_flow_response**](FlowsApi.md#poll_flow_response) | **POST** /v2/flows/sessions/{session_id}/invocation_response/{from_timestamp} | Poll Flow Response
[**publish_flow**](FlowsApi.md#publish_flow) | **POST** /v2/flows/{flow_id}/publish | Publish Flow
[**restore_flow_version**](FlowsApi.md#restore_flow_version) | **POST** /v2/flows/{flow_id}/version_history/{branch}/restore | Restore Flow Version
[**search**](FlowsApi.md#search) | **POST** /v2/flows/ | Search
[**search_all**](FlowsApi.md#search_all) | **POST** /v2/flows/all | Search All
[**search_flow_categories**](FlowsApi.md#search_flow_categories) | **POST** /v2/flows/categories/search | Search Flow Categories
[**search_flow_crons**](FlowsApi.md#search_flow_crons) | **POST** /v2/flows/crons/search | Search Flow Crons
[**update_flow**](FlowsApi.md#update_flow) | **PUT** /v2/flows/{flow_id} | Update Flow
[**update_flow_category**](FlowsApi.md#update_flow_category) | **PUT** /v2/flows/categories/{cat_id} | Update Flow Category
[**update_flow_cron**](FlowsApi.md#update_flow_cron) | **PUT** /v2/flows/crons/{flow_id}/{cron_id} | Update Flow Cron
[**upload_attachments**](FlowsApi.md#upload_attachments) | **POST** /v2/flows/sessions/{session_id}/attachments | Upload Attachments


# **create_chatbot_session**
> FlowSessionResponse create_chatbot_session(workspace_id, flow_session_create_request)

Create Chatbot Session

### Example


```python
import flowhunt
from flowhunt.models.flow_session_create_request import FlowSessionCreateRequest
from flowhunt.models.flow_session_response import FlowSessionResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_session_create_request = flowhunt.FlowSessionCreateRequest() # FlowSessionCreateRequest | 

    try:
        # Create Chatbot Session
        api_response = api_instance.create_chatbot_session(workspace_id, flow_session_create_request)
        print("The response of FlowsApi->create_chatbot_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_chatbot_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_session_create_request** | [**FlowSessionCreateRequest**](FlowSessionCreateRequest.md)|  | 

### Return type

[**FlowSessionResponse**](FlowSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flow**
> FlowDetailResponse create_flow(workspace_id, flow_create)

Create Flow

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_create import FlowCreate
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_create = flowhunt.FlowCreate() # FlowCreate | 

    try:
        # Create Flow
        api_response = api_instance.create_flow(workspace_id, flow_create)
        print("The response of FlowsApi->create_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_create** | [**FlowCreate**](FlowCreate.md)|  | 

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

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

# **create_flow_category**
> FlowCategoryResponse create_flow_category(workspace_id, flow_category_create_request)

Create Flow Category

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_category_create_request import FlowCategoryCreateRequest
from flowhunt.models.flow_category_response import FlowCategoryResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_category_create_request = flowhunt.FlowCategoryCreateRequest() # FlowCategoryCreateRequest | 

    try:
        # Create Flow Category
        api_response = api_instance.create_flow_category(workspace_id, flow_category_create_request)
        print("The response of FlowsApi->create_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_category_create_request** | [**FlowCategoryCreateRequest**](FlowCategoryCreateRequest.md)|  | 

### Return type

[**FlowCategoryResponse**](FlowCategoryResponse.md)

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

# **create_flow_cron**
> FlowCronResponse create_flow_cron(workspace_id, flow_cron_create_request)

Create Flow Cron

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_cron_create_request import FlowCronCreateRequest
from flowhunt.models.flow_cron_response import FlowCronResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_cron_create_request = flowhunt.FlowCronCreateRequest() # FlowCronCreateRequest | 

    try:
        # Create Flow Cron
        api_response = api_instance.create_flow_cron(workspace_id, flow_cron_create_request)
        print("The response of FlowsApi->create_flow_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_cron_create_request** | [**FlowCronCreateRequest**](FlowCronCreateRequest.md)|  | 

### Return type

[**FlowCronResponse**](FlowCronResponse.md)

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

# **create_flow_session**
> FlowSessionResponse create_flow_session(workspace_id, flow_session_create_from_flow_request)

Create Flow Session

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_session_create_from_flow_request import FlowSessionCreateFromFlowRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_session_create_from_flow_request = flowhunt.FlowSessionCreateFromFlowRequest() # FlowSessionCreateFromFlowRequest | 

    try:
        # Create Flow Session
        api_response = api_instance.create_flow_session(workspace_id, flow_session_create_from_flow_request)
        print("The response of FlowsApi->create_flow_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_session_create_from_flow_request** | [**FlowSessionCreateFromFlowRequest**](FlowSessionCreateFromFlowRequest.md)|  | 

### Return type

[**FlowSessionResponse**](FlowSessionResponse.md)

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

# **delete_attachment**
> Completed delete_attachment(session_id, file_id)

Delete Attachment

### Example


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


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.FlowsApi(api_client)
    session_id = 'session_id_example' # str | 
    file_id = 'file_id_example' # str | 

    try:
        # Delete Attachment
        api_response = api_instance.delete_attachment(session_id, file_id)
        print("The response of FlowsApi->delete_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->delete_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **delete_flow**
> Completed delete_flow(flow_id, workspace_id)

Delete Flow

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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Flow
        api_response = api_instance.delete_flow(flow_id, workspace_id)
        print("The response of FlowsApi->delete_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->delete_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
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

# **delete_flow_category**
> Completed delete_flow_category(cat_id, workspace_id)

Delete Flow Category

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
    api_instance = flowhunt.FlowsApi(api_client)
    cat_id = 'cat_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Flow Category
        api_response = api_instance.delete_flow_category(cat_id, workspace_id)
        print("The response of FlowsApi->delete_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->delete_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat_id** | **str**|  | 
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

# **delete_flow_cron**
> Completed delete_flow_cron(flow_id, cron_id, workspace_id)

Delete Flow Cron

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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    cron_id = 'cron_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Flow Cron
        api_response = api_instance.delete_flow_cron(flow_id, cron_id, workspace_id)
        print("The response of FlowsApi->delete_flow_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->delete_flow_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **cron_id** | **str**|  | 
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

# **execute_flow_cron**
> TaskResponse execute_flow_cron(cron_id, flow_id, workspace_id)

Execute Flow Cron

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    cron_id = 'cron_id_example' # str | 
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Execute Flow Cron
        api_response = api_instance.execute_flow_cron(cron_id, flow_id, workspace_id)
        print("The response of FlowsApi->execute_flow_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->execute_flow_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cron_id** | **str**|  | 
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **generate_commit_message**
> FlowCommitResponse generate_commit_message(flow_id, workspace_id)

Generate Commit Message

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_commit_response import FlowCommitResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Generate Commit Message
        api_response = api_instance.generate_commit_message(flow_id, workspace_id)
        print("The response of FlowsApi->generate_commit_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->generate_commit_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**FlowCommitResponse**](FlowCommitResponse.md)

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

# **get**
> FlowDetailResponse get(flow_id, workspace_id, branch=branch)

Get

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    branch = 'D' # str |  (optional) (default to 'D')

    try:
        # Get
        api_response = api_instance.get(flow_id, workspace_id, branch=branch)
        print("The response of FlowsApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **branch** | **str**|  | [optional] [default to &#39;D&#39;]

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

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

# **get_all_components**
> object get_all_components()

Get All Components

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
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
    api_instance = flowhunt.FlowsApi(api_client)

    try:
        # Get All Components
        api_response = api_instance.get_all_components()
        print("The response of FlowsApi->get_all_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_all_components: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> List[FlowSessionAttachmentResponse] get_attachments(session_id)

Get Attachments

### Example


```python
import flowhunt
from flowhunt.models.flow_session_attachment_response import FlowSessionAttachmentResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Get Attachments
        api_response = api_instance.get_attachments(session_id)
        print("The response of FlowsApi->get_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**List[FlowSessionAttachmentResponse]**](FlowSessionAttachmentResponse.md)

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

# **get_flow_versions**
> List[FlowVersionHistoryResponse] get_flow_versions(flow_id, workspace_id)

Get Flow Versions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_version_history_response import FlowVersionHistoryResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Flow Versions
        api_response = api_instance.get_flow_versions(flow_id, workspace_id)
        print("The response of FlowsApi->get_flow_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[FlowVersionHistoryResponse]**](FlowVersionHistoryResponse.md)

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

# **get_invoked_flow_results**
> TaskResponse get_invoked_flow_results(flow_id, task_id, workspace_id)

Get Invoked Flow Results

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    task_id = 'task_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Invoked Flow Results
        api_response = api_instance.get_invoked_flow_results(flow_id, task_id, workspace_id)
        print("The response of FlowsApi->get_invoked_flow_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_invoked_flow_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **task_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **get_public_flow**
> FlowDetailResponse get_public_flow(flow_id)

Get Public Flow

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 

    try:
        # Get Public Flow
        api_response = api_instance.get_public_flow(flow_id)
        print("The response of FlowsApi->get_public_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_public_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

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

# **get_trigger_types**
> TriggerResponse get_trigger_types(flow_id, workspace_id)

Get Trigger Types

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.trigger_response import TriggerResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Trigger Types
        api_response = api_instance.get_trigger_types(flow_id, workspace_id)
        print("The response of FlowsApi->get_trigger_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_trigger_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

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

# **invoke_flow**
> TaskResponse invoke_flow(flow_id, workspace_id, flow_invoke_request)

Invoke Flow

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_invoke_request import FlowInvokeRequest
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_invoke_request = flowhunt.FlowInvokeRequest() # FlowInvokeRequest | 

    try:
        # Invoke Flow
        api_response = api_instance.invoke_flow(flow_id, workspace_id, flow_invoke_request)
        print("The response of FlowsApi->invoke_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->invoke_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_invoke_request** | [**FlowInvokeRequest**](FlowInvokeRequest.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **invoke_flow_response**
> FlowSessionInvocationResponse invoke_flow_response(session_id, flow_session_invoke_request)

Invoke Flow Response

### Example


```python
import flowhunt
from flowhunt.models.flow_session_invocation_response import FlowSessionInvocationResponse
from flowhunt.models.flow_session_invoke_request import FlowSessionInvokeRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    session_id = 'session_id_example' # str | 
    flow_session_invoke_request = flowhunt.FlowSessionInvokeRequest() # FlowSessionInvokeRequest | 

    try:
        # Invoke Flow Response
        api_response = api_instance.invoke_flow_response(session_id, flow_session_invoke_request)
        print("The response of FlowsApi->invoke_flow_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->invoke_flow_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **flow_session_invoke_request** | [**FlowSessionInvokeRequest**](FlowSessionInvokeRequest.md)|  | 

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

# **invoke_flow_singleton**
> TaskResponse invoke_flow_singleton(flow_id, workspace_id, flow_invoke_request)

Invoke Flow Singleton

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_invoke_request import FlowInvokeRequest
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_invoke_request = flowhunt.FlowInvokeRequest() # FlowInvokeRequest | 

    try:
        # Invoke Flow Singleton
        api_response = api_instance.invoke_flow_singleton(flow_id, workspace_id, flow_invoke_request)
        print("The response of FlowsApi->invoke_flow_singleton:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->invoke_flow_singleton: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_invoke_request** | [**FlowInvokeRequest**](FlowInvokeRequest.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **poll_flow_response**
> List[FlowSessionEvent] poll_flow_response(session_id, from_timestamp)

Poll Flow Response

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
    api_instance = flowhunt.FlowsApi(api_client)
    session_id = 'session_id_example' # str | 
    from_timestamp = 'from_timestamp_example' # str | 

    try:
        # Poll Flow Response
        api_response = api_instance.poll_flow_response(session_id, from_timestamp)
        print("The response of FlowsApi->poll_flow_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->poll_flow_response: %s\n" % e)
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

# **publish_flow**
> FlowDetailResponse publish_flow(flow_id, workspace_id, flow_commit_request)

Publish Flow

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_commit_request import FlowCommitRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_commit_request = flowhunt.FlowCommitRequest() # FlowCommitRequest | 

    try:
        # Publish Flow
        api_response = api_instance.publish_flow(flow_id, workspace_id, flow_commit_request)
        print("The response of FlowsApi->publish_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->publish_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_commit_request** | [**FlowCommitRequest**](FlowCommitRequest.md)|  | 

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

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

# **restore_flow_version**
> Completed restore_flow_version(flow_id, branch, workspace_id)

Restore Flow Version

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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    branch = 'branch_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Restore Flow Version
        api_response = api_instance.restore_flow_version(flow_id, branch, workspace_id)
        print("The response of FlowsApi->restore_flow_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->restore_flow_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **branch** | **str**|  | 
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

# **search**
> List[FlowResponse] search(workspace_id, flow_search_request)

Search

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_response import FlowResponse
from flowhunt.models.flow_search_request import FlowSearchRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_search_request = flowhunt.FlowSearchRequest() # FlowSearchRequest | 

    try:
        # Search
        api_response = api_instance.search(workspace_id, flow_search_request)
        print("The response of FlowsApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_search_request** | [**FlowSearchRequest**](FlowSearchRequest.md)|  | 

### Return type

[**List[FlowResponse]**](FlowResponse.md)

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

# **search_all**
> List[FlowResponse] search_all(workspace_id, all_flows_search_request)

Search All

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.all_flows_search_request import AllFlowsSearchRequest
from flowhunt.models.flow_response import FlowResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    all_flows_search_request = flowhunt.AllFlowsSearchRequest() # AllFlowsSearchRequest | 

    try:
        # Search All
        api_response = api_instance.search_all(workspace_id, all_flows_search_request)
        print("The response of FlowsApi->search_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->search_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **all_flows_search_request** | [**AllFlowsSearchRequest**](AllFlowsSearchRequest.md)|  | 

### Return type

[**List[FlowResponse]**](FlowResponse.md)

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

# **search_flow_categories**
> List[FlowCategoryResponse] search_flow_categories(workspace_id, flow_category_search_request)

Search Flow Categories

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_category_response import FlowCategoryResponse
from flowhunt.models.flow_category_search_request import FlowCategorySearchRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_category_search_request = flowhunt.FlowCategorySearchRequest() # FlowCategorySearchRequest | 

    try:
        # Search Flow Categories
        api_response = api_instance.search_flow_categories(workspace_id, flow_category_search_request)
        print("The response of FlowsApi->search_flow_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->search_flow_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_category_search_request** | [**FlowCategorySearchRequest**](FlowCategorySearchRequest.md)|  | 

### Return type

[**List[FlowCategoryResponse]**](FlowCategoryResponse.md)

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

# **search_flow_crons**
> List[FlowCronResponse] search_flow_crons(workspace_id, flow_cron_search_request)

Search Flow Crons

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_cron_response import FlowCronResponse
from flowhunt.models.flow_cron_search_request import FlowCronSearchRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    flow_cron_search_request = flowhunt.FlowCronSearchRequest() # FlowCronSearchRequest | 

    try:
        # Search Flow Crons
        api_response = api_instance.search_flow_crons(workspace_id, flow_cron_search_request)
        print("The response of FlowsApi->search_flow_crons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->search_flow_crons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **flow_cron_search_request** | [**FlowCronSearchRequest**](FlowCronSearchRequest.md)|  | 

### Return type

[**List[FlowCronResponse]**](FlowCronResponse.md)

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

# **update_flow**
> FlowDetailResponse update_flow(flow_id, workspace_id, flow_update)

Update Flow

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_detail_response import FlowDetailResponse
from flowhunt.models.flow_update import FlowUpdate
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
    api_instance = flowhunt.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_update = flowhunt.FlowUpdate() # FlowUpdate | 

    try:
        # Update Flow
        api_response = api_instance.update_flow(flow_id, workspace_id, flow_update)
        print("The response of FlowsApi->update_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->update_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_update** | [**FlowUpdate**](FlowUpdate.md)|  | 

### Return type

[**FlowDetailResponse**](FlowDetailResponse.md)

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

# **update_flow_category**
> FlowCategoryResponse update_flow_category(cat_id, workspace_id, flow_category_create_request)

Update Flow Category

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_category_create_request import FlowCategoryCreateRequest
from flowhunt.models.flow_category_response import FlowCategoryResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    cat_id = 'cat_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_category_create_request = flowhunt.FlowCategoryCreateRequest() # FlowCategoryCreateRequest | 

    try:
        # Update Flow Category
        api_response = api_instance.update_flow_category(cat_id, workspace_id, flow_category_create_request)
        print("The response of FlowsApi->update_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->update_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_category_create_request** | [**FlowCategoryCreateRequest**](FlowCategoryCreateRequest.md)|  | 

### Return type

[**FlowCategoryResponse**](FlowCategoryResponse.md)

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

# **update_flow_cron**
> FlowCronResponse update_flow_cron(cron_id, flow_id, workspace_id, flow_cron_update_request)

Update Flow Cron

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_cron_response import FlowCronResponse
from flowhunt.models.flow_cron_update_request import FlowCronUpdateRequest
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
    api_instance = flowhunt.FlowsApi(api_client)
    cron_id = 'cron_id_example' # str | 
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_cron_update_request = flowhunt.FlowCronUpdateRequest() # FlowCronUpdateRequest | 

    try:
        # Update Flow Cron
        api_response = api_instance.update_flow_cron(cron_id, flow_id, workspace_id, flow_cron_update_request)
        print("The response of FlowsApi->update_flow_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->update_flow_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cron_id** | **str**|  | 
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_cron_update_request** | [**FlowCronUpdateRequest**](FlowCronUpdateRequest.md)|  | 

### Return type

[**FlowCronResponse**](FlowCronResponse.md)

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

# **upload_attachments**
> FlowSessionAttachmentResponse upload_attachments(session_id, file)

Upload Attachments

### Example


```python
import flowhunt
from flowhunt.models.flow_session_attachment_response import FlowSessionAttachmentResponse
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
    api_instance = flowhunt.FlowsApi(api_client)
    session_id = 'session_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload Attachments
        api_response = api_instance.upload_attachments(session_id, file)
        print("The response of FlowsApi->upload_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->upload_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**FlowSessionAttachmentResponse**](FlowSessionAttachmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

