# flowhunt.MemoryApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node**](MemoryApi.md#create_node) | **POST** /v2/memory/node/create | Create Node
[**delete_node**](MemoryApi.md#delete_node) | **DELETE** /v2/memory/node/{node_id} | Delete Node
[**get_node**](MemoryApi.md#get_node) | **POST** /v2/memory/node/{node_id} | Get Node
[**get_offloaded_content**](MemoryApi.md#get_offloaded_content) | **POST** /v2/memory/node/{node_id}/offload/{offload_id} | Get Offloaded Content
[**process_documents**](MemoryApi.md#process_documents) | **POST** /v2/memory/process-documents | Process Documents
[**search_memory_categories**](MemoryApi.md#search_memory_categories) | **POST** /v2/memory/search | Search Memory Categories
[**search_memory_node_name**](MemoryApi.md#search_memory_node_name) | **POST** /v2/memory/search_node_name | Search Memory Node Name
[**search_memory_node_path**](MemoryApi.md#search_memory_node_path) | **POST** /v2/memory/search_node_path | Search Memory Node Path
[**update_node**](MemoryApi.md#update_node) | **PUT** /v2/memory/node/{node_id} | Update Node
[**upload_memory_node_document**](MemoryApi.md#upload_memory_node_document) | **POST** /v2/memory/upload/{cat_id} | Upload Memory Node Document


# **create_node**
> MemoryNodeResponse create_node(workspace_id, node_detail_request)

Create Node

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_node_response import MemoryNodeResponse
from flowhunt.models.node_detail_request import NodeDetailRequest
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
    api_instance = flowhunt.MemoryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    node_detail_request = flowhunt.NodeDetailRequest() # NodeDetailRequest | 

    try:
        # Create Node
        api_response = api_instance.create_node(workspace_id, node_detail_request)
        print("The response of MemoryApi->create_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->create_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **node_detail_request** | [**NodeDetailRequest**](NodeDetailRequest.md)|  | 

### Return type

[**MemoryNodeResponse**](MemoryNodeResponse.md)

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

# **delete_node**
> MemoryMessageResponse delete_node(node_id, workspace_id, delete_node_request)

Delete Node

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.delete_node_request import DeleteNodeRequest
from flowhunt.models.memory_message_response import MemoryMessageResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    node_id = 'node_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    delete_node_request = flowhunt.DeleteNodeRequest() # DeleteNodeRequest | 

    try:
        # Delete Node
        api_response = api_instance.delete_node(node_id, workspace_id, delete_node_request)
        print("The response of MemoryApi->delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **delete_node_request** | [**DeleteNodeRequest**](DeleteNodeRequest.md)|  | 

### Return type

[**MemoryMessageResponse**](MemoryMessageResponse.md)

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

# **get_node**
> MemoryNodeDetailResponse get_node(node_id, workspace_id, get_node_request)

Get Node

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.get_node_request import GetNodeRequest
from flowhunt.models.memory_node_detail_response import MemoryNodeDetailResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    node_id = 'node_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    get_node_request = flowhunt.GetNodeRequest() # GetNodeRequest | 

    try:
        # Get Node
        api_response = api_instance.get_node(node_id, workspace_id, get_node_request)
        print("The response of MemoryApi->get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **get_node_request** | [**GetNodeRequest**](GetNodeRequest.md)|  | 

### Return type

[**MemoryNodeDetailResponse**](MemoryNodeDetailResponse.md)

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

# **get_offloaded_content**
> str get_offloaded_content(node_id, offload_id, workspace_id, get_node_request)

Get Offloaded Content

Get offloaded content for a memory node.

Args:
    workspace_id: The workspace ID
    node_id: The node ID
    offload_id: The offload ID to retrieve
    node_request: Request containing cat_id
    memory_controller: Memory controller dependency
    user: Current user

Returns:
    The offloaded content as plain text

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.get_node_request import GetNodeRequest
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
    api_instance = flowhunt.MemoryApi(api_client)
    node_id = 'node_id_example' # str | 
    offload_id = 'offload_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    get_node_request = flowhunt.GetNodeRequest() # GetNodeRequest | 

    try:
        # Get Offloaded Content
        api_response = api_instance.get_offloaded_content(node_id, offload_id, workspace_id, get_node_request)
        print("The response of MemoryApi->get_offloaded_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->get_offloaded_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **offload_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **get_node_request** | [**GetNodeRequest**](GetNodeRequest.md)|  | 

### Return type

**str**

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

# **process_documents**
> MemoryMessageResponse process_documents(workspace_id, memory_document_process_request)

Process Documents

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_document_process_request import MemoryDocumentProcessRequest
from flowhunt.models.memory_message_response import MemoryMessageResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    memory_document_process_request = flowhunt.MemoryDocumentProcessRequest() # MemoryDocumentProcessRequest | 

    try:
        # Process Documents
        api_response = api_instance.process_documents(workspace_id, memory_document_process_request)
        print("The response of MemoryApi->process_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->process_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **memory_document_process_request** | [**MemoryDocumentProcessRequest**](MemoryDocumentProcessRequest.md)|  | 

### Return type

[**MemoryMessageResponse**](MemoryMessageResponse.md)

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

# **search_memory_categories**
> List[MemorySearchResponse] search_memory_categories(workspace_id, memory_search_request)

Search Memory Categories

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_search_request import MemorySearchRequest
from flowhunt.models.memory_search_response import MemorySearchResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    memory_search_request = flowhunt.MemorySearchRequest() # MemorySearchRequest | 

    try:
        # Search Memory Categories
        api_response = api_instance.search_memory_categories(workspace_id, memory_search_request)
        print("The response of MemoryApi->search_memory_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->search_memory_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **memory_search_request** | [**MemorySearchRequest**](MemorySearchRequest.md)|  | 

### Return type

[**List[MemorySearchResponse]**](MemorySearchResponse.md)

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

# **search_memory_node_name**
> List[MemorySearchResponse] search_memory_node_name(workspace_id, memory_node_name_search_request)

Search Memory Node Name

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_node_name_search_request import MemoryNodeNameSearchRequest
from flowhunt.models.memory_search_response import MemorySearchResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    memory_node_name_search_request = flowhunt.MemoryNodeNameSearchRequest() # MemoryNodeNameSearchRequest | 

    try:
        # Search Memory Node Name
        api_response = api_instance.search_memory_node_name(workspace_id, memory_node_name_search_request)
        print("The response of MemoryApi->search_memory_node_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->search_memory_node_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **memory_node_name_search_request** | [**MemoryNodeNameSearchRequest**](MemoryNodeNameSearchRequest.md)|  | 

### Return type

[**List[MemorySearchResponse]**](MemorySearchResponse.md)

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

# **search_memory_node_path**
> List[MemorySearchResponse] search_memory_node_path(workspace_id, memory_node_path_search_request)

Search Memory Node Path

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_node_path_search_request import MemoryNodePathSearchRequest
from flowhunt.models.memory_search_response import MemorySearchResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    memory_node_path_search_request = flowhunt.MemoryNodePathSearchRequest() # MemoryNodePathSearchRequest | 

    try:
        # Search Memory Node Path
        api_response = api_instance.search_memory_node_path(workspace_id, memory_node_path_search_request)
        print("The response of MemoryApi->search_memory_node_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->search_memory_node_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **memory_node_path_search_request** | [**MemoryNodePathSearchRequest**](MemoryNodePathSearchRequest.md)|  | 

### Return type

[**List[MemorySearchResponse]**](MemorySearchResponse.md)

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

# **update_node**
> MemoryNodeResponse update_node(node_id, workspace_id, node_update_request)

Update Node

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_node_response import MemoryNodeResponse
from flowhunt.models.node_update_request import NodeUpdateRequest
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
    api_instance = flowhunt.MemoryApi(api_client)
    node_id = 'node_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    node_update_request = flowhunt.NodeUpdateRequest() # NodeUpdateRequest | 

    try:
        # Update Node
        api_response = api_instance.update_node(node_id, workspace_id, node_update_request)
        print("The response of MemoryApi->update_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->update_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **node_update_request** | [**NodeUpdateRequest**](NodeUpdateRequest.md)|  | 

### Return type

[**MemoryNodeResponse**](MemoryNodeResponse.md)

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

# **upload_memory_node_document**
> MemoryDocumentUploadResponse upload_memory_node_document(cat_id, workspace_id, file)

Upload Memory Node Document

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.memory_document_upload_response import MemoryDocumentUploadResponse
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
    api_instance = flowhunt.MemoryApi(api_client)
    cat_id = 'cat_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload Memory Node Document
        api_response = api_instance.upload_memory_node_document(cat_id, workspace_id, file)
        print("The response of MemoryApi->upload_memory_node_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->upload_memory_node_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**MemoryDocumentUploadResponse**](MemoryDocumentUploadResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

