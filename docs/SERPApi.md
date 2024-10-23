# flowhunt.SERPApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serp_search**](SERPApi.md#serp_search) | **POST** /v2/serp/serp/search | Serp Search
[**serp_volumes**](SERPApi.md#serp_volumes) | **POST** /v2/serp/serp/volumes | Serp Volumes
[**serp_volumes_pingback**](SERPApi.md#serp_volumes_pingback) | **GET** /v2/serp/serp/volumes/pingback/{id}/{tag} | Serp Volumes Pingback


# **serp_search**
> List[TaskResponse] serp_search(workspace_id, serp_search_requests)

Serp Search

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_search_requests import SerpSearchRequests
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.SERPApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    serp_search_requests = flowhunt.SerpSearchRequests() # SerpSearchRequests | 

    try:
        # Serp Search
        api_response = api_instance.serp_search(workspace_id, serp_search_requests)
        print("The response of SERPApi->serp_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_search_requests** | [**SerpSearchRequests**](SerpSearchRequests.md)|  | 

### Return type

[**List[TaskResponse]**](TaskResponse.md)

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

# **serp_volumes**
> TaskResponse serp_volumes(workspace_id, serp_volume_request)

Serp Volumes

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_volume_request import SerpVolumeRequest
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.SERPApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    serp_volume_request = flowhunt.SerpVolumeRequest() # SerpVolumeRequest | 

    try:
        # Serp Volumes
        api_response = api_instance.serp_volumes(workspace_id, serp_volume_request)
        print("The response of SERPApi->serp_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_volume_request** | [**SerpVolumeRequest**](SerpVolumeRequest.md)|  | 

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

# **serp_volumes_pingback**
> TaskResponse serp_volumes_pingback(id, tag)

Serp Volumes Pingback

### Example


```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.SERPApi(api_client)
    id = 'id_example' # str | 
    tag = 'tag_example' # str | 

    try:
        # Serp Volumes Pingback
        api_response = api_instance.serp_volumes_pingback(id, tag)
        print("The response of SERPApi->serp_volumes_pingback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_volumes_pingback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

