# flowhunt.ReindexApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reindex_status**](ReindexApi.md#get_reindex_status) | **GET** /v2/reindex/status | Get Reindex Status
[**trigger_reindex**](ReindexApi.md#trigger_reindex) | **POST** /v2/reindex/ | Trigger Reindex


# **get_reindex_status**
> ReindexStatusResponse get_reindex_status(task_id)

Get Reindex Status

Get the status of a reindex operation.

The task_id format is: {workspace_id}_{embedding_model} or installation_{embedding_model}

### Example

* Api Key Authentication (sudo_api_key_header):

```python
import flowhunt
from flowhunt.models.reindex_status_response import ReindexStatusResponse
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

# Configure API key authorization: sudo_api_key_header
configuration.api_key['sudo_api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo_api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ReindexApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get Reindex Status
        api_response = api_instance.get_reindex_status(task_id)
        print("The response of ReindexApi->get_reindex_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReindexApi->get_reindex_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**ReindexStatusResponse**](ReindexStatusResponse.md)

### Authorization

[sudo_api_key_header](../README.md#sudo_api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_reindex**
> ReindexStartResponse trigger_reindex(reindex_request)

Trigger Reindex

Trigger a reindex operation for all data or a specific workspace.

This endpoint requires sudo API key authentication.

The reindex operation will:
1. Create a new versioned Qdrant collection
2. Reindex all documents, FAQs, and schedules
3. Support resume capability via Redis cursor
4. Be idempotent - can be called multiple times safely

### Example

* Api Key Authentication (sudo_api_key_header):

```python
import flowhunt
from flowhunt.models.reindex_request import ReindexRequest
from flowhunt.models.reindex_start_response import ReindexStartResponse
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

# Configure API key authorization: sudo_api_key_header
configuration.api_key['sudo_api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo_api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ReindexApi(api_client)
    reindex_request = flowhunt.ReindexRequest() # ReindexRequest | 

    try:
        # Trigger Reindex
        api_response = api_instance.trigger_reindex(reindex_request)
        print("The response of ReindexApi->trigger_reindex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReindexApi->trigger_reindex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reindex_request** | [**ReindexRequest**](ReindexRequest.md)|  | 

### Return type

[**ReindexStartResponse**](ReindexStartResponse.md)

### Authorization

[sudo_api_key_header](../README.md#sudo_api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

