# flowhunt.SemanticSearchApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_similar_docs_by_doc_id**](SemanticSearchApi.md#get_similar_docs_by_doc_id) | **POST** /v2/similarities/document/live | Get Similar Docs By Doc Id
[**get_similar_docs_by_query**](SemanticSearchApi.md#get_similar_docs_by_query) | **POST** /v2/similarities/query/live | Get Similar Docs By Query
[**schedule_similar_docs_by_doc_id**](SemanticSearchApi.md#schedule_similar_docs_by_doc_id) | **POST** /v2/similarities/document | Schedule Similar Docs By Doc Id
[**schedule_similar_docs_by_query**](SemanticSearchApi.md#schedule_similar_docs_by_query) | **POST** /v2/similarities/query | Schedule Similar Docs By Query


# **get_similar_docs_by_doc_id**
> List[VectorDocumentResponse] get_similar_docs_by_doc_id(workspace_id, document_similarity_request)

Get Similar Docs By Doc Id

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.document_similarity_request import DocumentSimilarityRequest
from flowhunt.models.vector_document_response import VectorDocumentResponse
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
    api_instance = flowhunt.SemanticSearchApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    document_similarity_request = flowhunt.DocumentSimilarityRequest() # DocumentSimilarityRequest | 

    try:
        # Get Similar Docs By Doc Id
        api_response = api_instance.get_similar_docs_by_doc_id(workspace_id, document_similarity_request)
        print("The response of SemanticSearchApi->get_similar_docs_by_doc_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticSearchApi->get_similar_docs_by_doc_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **document_similarity_request** | [**DocumentSimilarityRequest**](DocumentSimilarityRequest.md)|  | 

### Return type

[**List[VectorDocumentResponse]**](VectorDocumentResponse.md)

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

# **get_similar_docs_by_query**
> List[VectorDocumentResponse] get_similar_docs_by_query(workspace_id, query_similarity_request)

Get Similar Docs By Query

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.query_similarity_request import QuerySimilarityRequest
from flowhunt.models.vector_document_response import VectorDocumentResponse
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
    api_instance = flowhunt.SemanticSearchApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    query_similarity_request = flowhunt.QuerySimilarityRequest() # QuerySimilarityRequest | 

    try:
        # Get Similar Docs By Query
        api_response = api_instance.get_similar_docs_by_query(workspace_id, query_similarity_request)
        print("The response of SemanticSearchApi->get_similar_docs_by_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticSearchApi->get_similar_docs_by_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **query_similarity_request** | [**QuerySimilarityRequest**](QuerySimilarityRequest.md)|  | 

### Return type

[**List[VectorDocumentResponse]**](VectorDocumentResponse.md)

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

# **schedule_similar_docs_by_doc_id**
> VectorDocumentsTaskResponse schedule_similar_docs_by_doc_id(workspace_id, document_similarity_task_request)

Schedule Similar Docs By Doc Id

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.document_similarity_task_request import DocumentSimilarityTaskRequest
from flowhunt.models.vector_documents_task_response import VectorDocumentsTaskResponse
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
    api_instance = flowhunt.SemanticSearchApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    document_similarity_task_request = flowhunt.DocumentSimilarityTaskRequest() # DocumentSimilarityTaskRequest | 

    try:
        # Schedule Similar Docs By Doc Id
        api_response = api_instance.schedule_similar_docs_by_doc_id(workspace_id, document_similarity_task_request)
        print("The response of SemanticSearchApi->schedule_similar_docs_by_doc_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticSearchApi->schedule_similar_docs_by_doc_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **document_similarity_task_request** | [**DocumentSimilarityTaskRequest**](DocumentSimilarityTaskRequest.md)|  | 

### Return type

[**VectorDocumentsTaskResponse**](VectorDocumentsTaskResponse.md)

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

# **schedule_similar_docs_by_query**
> VectorDocumentsTaskResponse schedule_similar_docs_by_query(workspace_id, query_similarity_task_request)

Schedule Similar Docs By Query

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.query_similarity_task_request import QuerySimilarityTaskRequest
from flowhunt.models.vector_documents_task_response import VectorDocumentsTaskResponse
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
    api_instance = flowhunt.SemanticSearchApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    query_similarity_task_request = flowhunt.QuerySimilarityTaskRequest() # QuerySimilarityTaskRequest | 

    try:
        # Schedule Similar Docs By Query
        api_response = api_instance.schedule_similar_docs_by_query(workspace_id, query_similarity_task_request)
        print("The response of SemanticSearchApi->schedule_similar_docs_by_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticSearchApi->schedule_similar_docs_by_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **query_similarity_task_request** | [**QuerySimilarityTaskRequest**](QuerySimilarityTaskRequest.md)|  | 

### Return type

[**VectorDocumentsTaskResponse**](VectorDocumentsTaskResponse.md)

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

