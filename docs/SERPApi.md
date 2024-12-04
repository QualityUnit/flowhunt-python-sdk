# flowhunt.SERPApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_cluster_group**](SERPApi.md#search_cluster_group) | **POST** /v2/serp/cluster/search | Search Cluster Group
[**search_cluster_query**](SERPApi.md#search_cluster_query) | **POST** /v2/serp/cluster/{group_id}/search | Search Cluster Query
[**serp_cluster_add_group**](SERPApi.md#serp_cluster_add_group) | **POST** /v2/serp/cluster/create | Serp Cluster Add Group
[**serp_cluster_add_queries**](SERPApi.md#serp_cluster_add_queries) | **POST** /v2/serp/cluster/add_queries | Serp Cluster Add Queries
[**serp_cluster_delete_all**](SERPApi.md#serp_cluster_delete_all) | **DELETE** /v2/serp/cluster/delete_all | Serp Cluster Delete All
[**serp_cluster_delete_group**](SERPApi.md#serp_cluster_delete_group) | **DELETE** /v2/serp/cluster/{group_id} | Serp Cluster Delete Group
[**serp_cluster_delete_query**](SERPApi.md#serp_cluster_delete_query) | **DELETE** /v2/serp/cluster/{group_id}/{query_id} | Serp Cluster Delete Query
[**serp_cluster_get_bulk_query_intersections**](SERPApi.md#serp_cluster_get_bulk_query_intersections) | **POST** /v2/serp/cluster/bulk_query_intersections | Serp Cluster Get Bulk Query Intersections
[**serp_cluster_get_query_intersections**](SERPApi.md#serp_cluster_get_query_intersections) | **POST** /v2/serp/cluster/query_intersections | Serp Cluster Get Query Intersections
[**serp_search**](SERPApi.md#serp_search) | **POST** /v2/serp/serp/search | Serp Search
[**serp_volumes**](SERPApi.md#serp_volumes) | **POST** /v2/serp/serp/volumes | Serp Volumes
[**serp_volumes_pingback**](SERPApi.md#serp_volumes_pingback) | **GET** /v2/serp/serp/volumes/pingback/{id}/{tag} | Serp Volumes Pingback


# **search_cluster_group**
> List[SerpClusterGroupResponse] search_cluster_group(workspace_id, serp_cluster_group_search_request)

Search Cluster Group

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_group_response import SerpClusterGroupResponse
from flowhunt.models.serp_cluster_group_search_request import SerpClusterGroupSearchRequest
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
    serp_cluster_group_search_request = flowhunt.SerpClusterGroupSearchRequest() # SerpClusterGroupSearchRequest | 

    try:
        # Search Cluster Group
        api_response = api_instance.search_cluster_group(workspace_id, serp_cluster_group_search_request)
        print("The response of SERPApi->search_cluster_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->search_cluster_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_group_search_request** | [**SerpClusterGroupSearchRequest**](SerpClusterGroupSearchRequest.md)|  | 

### Return type

[**List[SerpClusterGroupResponse]**](SerpClusterGroupResponse.md)

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

# **search_cluster_query**
> List[SerpClusterQueryResponse] search_cluster_query(group_id, workspace_id, serp_cluster_group_search_request)

Search Cluster Query

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_group_search_request import SerpClusterGroupSearchRequest
from flowhunt.models.serp_cluster_query_response import SerpClusterQueryResponse
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
    group_id = 'group_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    serp_cluster_group_search_request = flowhunt.SerpClusterGroupSearchRequest() # SerpClusterGroupSearchRequest | 

    try:
        # Search Cluster Query
        api_response = api_instance.search_cluster_query(group_id, workspace_id, serp_cluster_group_search_request)
        print("The response of SERPApi->search_cluster_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->search_cluster_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **serp_cluster_group_search_request** | [**SerpClusterGroupSearchRequest**](SerpClusterGroupSearchRequest.md)|  | 

### Return type

[**List[SerpClusterQueryResponse]**](SerpClusterQueryResponse.md)

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

# **serp_cluster_add_group**
> SerpClusterGroupResponse serp_cluster_add_group(workspace_id, serp_cluster_add_group_request)

Serp Cluster Add Group

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_add_group_request import SerpClusterAddGroupRequest
from flowhunt.models.serp_cluster_group_response import SerpClusterGroupResponse
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
    serp_cluster_add_group_request = flowhunt.SerpClusterAddGroupRequest() # SerpClusterAddGroupRequest | 

    try:
        # Serp Cluster Add Group
        api_response = api_instance.serp_cluster_add_group(workspace_id, serp_cluster_add_group_request)
        print("The response of SERPApi->serp_cluster_add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_add_group_request** | [**SerpClusterAddGroupRequest**](SerpClusterAddGroupRequest.md)|  | 

### Return type

[**SerpClusterGroupResponse**](SerpClusterGroupResponse.md)

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

# **serp_cluster_add_queries**
> List[TaskResponse] serp_cluster_add_queries(workspace_id, serp_cluster_add_query_requests)

Serp Cluster Add Queries

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_add_query_requests import SerpClusterAddQueryRequests
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
    serp_cluster_add_query_requests = flowhunt.SerpClusterAddQueryRequests() # SerpClusterAddQueryRequests | 

    try:
        # Serp Cluster Add Queries
        api_response = api_instance.serp_cluster_add_queries(workspace_id, serp_cluster_add_query_requests)
        print("The response of SERPApi->serp_cluster_add_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_add_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_add_query_requests** | [**SerpClusterAddQueryRequests**](SerpClusterAddQueryRequests.md)|  | 

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

# **serp_cluster_delete_all**
> Completed serp_cluster_delete_all(workspace_id)

Serp Cluster Delete All

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
    api_instance = flowhunt.SERPApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Serp Cluster Delete All
        api_response = api_instance.serp_cluster_delete_all(workspace_id)
        print("The response of SERPApi->serp_cluster_delete_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serp_cluster_delete_group**
> Completed serp_cluster_delete_group(group_id, workspace_id)

Serp Cluster Delete Group

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
    api_instance = flowhunt.SERPApi(api_client)
    group_id = 'group_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Serp Cluster Delete Group
        api_response = api_instance.serp_cluster_delete_group(group_id, workspace_id)
        print("The response of SERPApi->serp_cluster_delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
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

# **serp_cluster_delete_query**
> Completed serp_cluster_delete_query(group_id, query_id, workspace_id)

Serp Cluster Delete Query

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
    api_instance = flowhunt.SERPApi(api_client)
    group_id = 'group_id_example' # str | 
    query_id = 'query_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Serp Cluster Delete Query
        api_response = api_instance.serp_cluster_delete_query(group_id, query_id, workspace_id)
        print("The response of SERPApi->serp_cluster_delete_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **query_id** | **str**|  | 
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

# **serp_cluster_get_bulk_query_intersections**
> List[TaskResponse] serp_cluster_get_bulk_query_intersections(workspace_id, serp_cluster_query_intersections_request)

Serp Cluster Get Bulk Query Intersections

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_query_intersections_request import SerpClusterQueryIntersectionsRequest
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
    serp_cluster_query_intersections_request = [flowhunt.SerpClusterQueryIntersectionsRequest()] # List[SerpClusterQueryIntersectionsRequest] | 

    try:
        # Serp Cluster Get Bulk Query Intersections
        api_response = api_instance.serp_cluster_get_bulk_query_intersections(workspace_id, serp_cluster_query_intersections_request)
        print("The response of SERPApi->serp_cluster_get_bulk_query_intersections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_get_bulk_query_intersections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_query_intersections_request** | [**List[SerpClusterQueryIntersectionsRequest]**](SerpClusterQueryIntersectionsRequest.md)|  | 

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

# **serp_cluster_get_query_intersections**
> TaskResponse serp_cluster_get_query_intersections(workspace_id, serp_cluster_query_intersections_request)

Serp Cluster Get Query Intersections

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_query_intersections_request import SerpClusterQueryIntersectionsRequest
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
    serp_cluster_query_intersections_request = flowhunt.SerpClusterQueryIntersectionsRequest() # SerpClusterQueryIntersectionsRequest | 

    try:
        # Serp Cluster Get Query Intersections
        api_response = api_instance.serp_cluster_get_query_intersections(workspace_id, serp_cluster_query_intersections_request)
        print("The response of SERPApi->serp_cluster_get_query_intersections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_get_query_intersections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_query_intersections_request** | [**SerpClusterQueryIntersectionsRequest**](SerpClusterQueryIntersectionsRequest.md)|  | 

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

