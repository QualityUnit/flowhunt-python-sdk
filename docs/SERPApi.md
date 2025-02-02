# flowhunt.SERPApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_cluster_query**](SERPApi.md#search_cluster_query) | **POST** /v2/serp/clusters/keywords | Search Cluster Query
[**serp_cluster_add_queries**](SERPApi.md#serp_cluster_add_queries) | **POST** /v2/serp/clusters/{customer_id}/{campaign_id}/{group_id}/add_keywords | Serp Cluster Add Queries
[**serp_cluster_delete_campaign**](SERPApi.md#serp_cluster_delete_campaign) | **DELETE** /v2/serp/clusters/{customer_id}/{campaign_id} | Serp Cluster Delete Campaign
[**serp_cluster_delete_customer**](SERPApi.md#serp_cluster_delete_customer) | **DELETE** /v2/serp/clusters/{customer_id} | Serp Cluster Delete Customer
[**serp_cluster_delete_group**](SERPApi.md#serp_cluster_delete_group) | **DELETE** /v2/serp/clusters/{customer_id}/{campaign_id}/{group_id} | Serp Cluster Delete Group
[**serp_cluster_delete_group_queries**](SERPApi.md#serp_cluster_delete_group_queries) | **DELETE** /v2/serp/clusters/{customer_id}/{campaign_id}/{group_id}/delete_queries | Serp Cluster Delete Group Queries
[**serp_cluster_get_graph_nodes**](SERPApi.md#serp_cluster_get_graph_nodes) | **POST** /v2/serp/clusters/graph_nodes | Serp Cluster Get Graph Nodes
[**serp_cluster_get_matching_groups_to_query**](SERPApi.md#serp_cluster_get_matching_groups_to_query) | **POST** /v2/serp/clusters/recommended_groups | Serp Cluster Get Matching Groups To Query
[**serp_cluster_get_related_keywords_to_query**](SERPApi.md#serp_cluster_get_related_keywords_to_query) | **POST** /v2/serp/clusters/related_keywords | Serp Cluster Get Related Keywords To Query
[**serp_cluster_split_to_sub_clusters**](SERPApi.md#serp_cluster_split_to_sub_clusters) | **POST** /v2/serp/clusters/split_sub_clusters | Serp Cluster Split To Sub Clusters
[**serp_search**](SERPApi.md#serp_search) | **POST** /v2/serp/serp/search | Serp Search
[**serp_volumes**](SERPApi.md#serp_volumes) | **POST** /v2/serp/serp/volumes | Serp Volumes
[**serp_volumes_pingback**](SERPApi.md#serp_volumes_pingback) | **GET** /v2/serp/serp/volumes/pingback/{id}/{tag} | Serp Volumes Pingback


# **search_cluster_query**
> List[SerpClusterKeywordResponse] search_cluster_query(workspace_id, serp_cluster_group_search_request)

Search Cluster Query

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_group_search_request import SerpClusterGroupSearchRequest
from flowhunt.models.serp_cluster_keyword_response import SerpClusterKeywordResponse
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
        # Search Cluster Query
        api_response = api_instance.search_cluster_query(workspace_id, serp_cluster_group_search_request)
        print("The response of SERPApi->search_cluster_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->search_cluster_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_group_search_request** | [**SerpClusterGroupSearchRequest**](SerpClusterGroupSearchRequest.md)|  | 

### Return type

[**List[SerpClusterKeywordResponse]**](SerpClusterKeywordResponse.md)

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
> Completed serp_cluster_add_queries(customer_id, campaign_id, group_id, workspace_id, serp_cluster_add_query_requests)

Serp Cluster Add Queries

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.serp_cluster_add_query_requests import SerpClusterAddQueryRequests
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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    group_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 
    serp_cluster_add_query_requests = flowhunt.SerpClusterAddQueryRequests() # SerpClusterAddQueryRequests | 

    try:
        # Serp Cluster Add Queries
        api_response = api_instance.serp_cluster_add_queries(customer_id, campaign_id, group_id, workspace_id, serp_cluster_add_query_requests)
        print("The response of SERPApi->serp_cluster_add_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_add_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **group_id** | **int**|  | 
 **workspace_id** | **str**|  | 
 **serp_cluster_add_query_requests** | [**SerpClusterAddQueryRequests**](SerpClusterAddQueryRequests.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **serp_cluster_delete_campaign**
> Completed serp_cluster_delete_campaign(customer_id, campaign_id, workspace_id)

Serp Cluster Delete Campaign

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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Serp Cluster Delete Campaign
        api_response = api_instance.serp_cluster_delete_campaign(customer_id, campaign_id, workspace_id)
        print("The response of SERPApi->serp_cluster_delete_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
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

# **serp_cluster_delete_customer**
> Completed serp_cluster_delete_customer(customer_id, workspace_id)

Serp Cluster Delete Customer

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
    customer_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Serp Cluster Delete Customer
        api_response = api_instance.serp_cluster_delete_customer(customer_id, workspace_id)
        print("The response of SERPApi->serp_cluster_delete_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
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
> Completed serp_cluster_delete_group(customer_id, campaign_id, group_id, workspace_id)

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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    group_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Serp Cluster Delete Group
        api_response = api_instance.serp_cluster_delete_group(customer_id, campaign_id, group_id, workspace_id)
        print("The response of SERPApi->serp_cluster_delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **group_id** | **int**|  | 
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

# **serp_cluster_delete_group_queries**
> Completed serp_cluster_delete_group_queries(customer_id, campaign_id, group_id, workspace_id, serp_query_request)

Serp Cluster Delete Group Queries

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.serp_query_request import SerpQueryRequest
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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    group_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 
    serp_query_request = flowhunt.SerpQueryRequest() # SerpQueryRequest | 

    try:
        # Serp Cluster Delete Group Queries
        api_response = api_instance.serp_cluster_delete_group_queries(customer_id, campaign_id, group_id, workspace_id, serp_query_request)
        print("The response of SERPApi->serp_cluster_delete_group_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_delete_group_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **group_id** | **int**|  | 
 **workspace_id** | **str**|  | 
 **serp_query_request** | [**SerpQueryRequest**](SerpQueryRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **serp_cluster_get_graph_nodes**
> List[SerpKeywordRelation] serp_cluster_get_graph_nodes(workspace_id, serp_cluster_group_intersections_request)

Serp Cluster Get Graph Nodes

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_group_intersections_request import SerpClusterGroupIntersectionsRequest
from flowhunt.models.serp_keyword_relation import SerpKeywordRelation
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
    serp_cluster_group_intersections_request = flowhunt.SerpClusterGroupIntersectionsRequest() # SerpClusterGroupIntersectionsRequest | 

    try:
        # Serp Cluster Get Graph Nodes
        api_response = api_instance.serp_cluster_get_graph_nodes(workspace_id, serp_cluster_group_intersections_request)
        print("The response of SERPApi->serp_cluster_get_graph_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_get_graph_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_group_intersections_request** | [**SerpClusterGroupIntersectionsRequest**](SerpClusterGroupIntersectionsRequest.md)|  | 

### Return type

[**List[SerpKeywordRelation]**](SerpKeywordRelation.md)

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

# **serp_cluster_get_matching_groups_to_query**
> List[SerpGroupIntersection] serp_cluster_get_matching_groups_to_query(workspace_id, serp_cluster_best_groups_request)

Serp Cluster Get Matching Groups To Query

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_best_groups_request import SerpClusterBestGroupsRequest
from flowhunt.models.serp_group_intersection import SerpGroupIntersection
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
    serp_cluster_best_groups_request = flowhunt.SerpClusterBestGroupsRequest() # SerpClusterBestGroupsRequest | 

    try:
        # Serp Cluster Get Matching Groups To Query
        api_response = api_instance.serp_cluster_get_matching_groups_to_query(workspace_id, serp_cluster_best_groups_request)
        print("The response of SERPApi->serp_cluster_get_matching_groups_to_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_get_matching_groups_to_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_best_groups_request** | [**SerpClusterBestGroupsRequest**](SerpClusterBestGroupsRequest.md)|  | 

### Return type

[**List[SerpGroupIntersection]**](SerpGroupIntersection.md)

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

# **serp_cluster_get_related_keywords_to_query**
> List[SerpKeywordRelation] serp_cluster_get_related_keywords_to_query(workspace_id, serp_cluster_keyword_intersections_request)

Serp Cluster Get Related Keywords To Query

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_keyword_intersections_request import SerpClusterKeywordIntersectionsRequest
from flowhunt.models.serp_keyword_relation import SerpKeywordRelation
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
    serp_cluster_keyword_intersections_request = flowhunt.SerpClusterKeywordIntersectionsRequest() # SerpClusterKeywordIntersectionsRequest | 

    try:
        # Serp Cluster Get Related Keywords To Query
        api_response = api_instance.serp_cluster_get_related_keywords_to_query(workspace_id, serp_cluster_keyword_intersections_request)
        print("The response of SERPApi->serp_cluster_get_related_keywords_to_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_get_related_keywords_to_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_keyword_intersections_request** | [**SerpClusterKeywordIntersectionsRequest**](SerpClusterKeywordIntersectionsRequest.md)|  | 

### Return type

[**List[SerpKeywordRelation]**](SerpKeywordRelation.md)

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

# **serp_cluster_split_to_sub_clusters**
> List[List[str]] serp_cluster_split_to_sub_clusters(workspace_id, serp_cluster_group_sub_clusters_request)

Serp Cluster Split To Sub Clusters

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.serp_cluster_group_sub_clusters_request import SerpClusterGroupSubClustersRequest
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
    serp_cluster_group_sub_clusters_request = flowhunt.SerpClusterGroupSubClustersRequest() # SerpClusterGroupSubClustersRequest | 

    try:
        # Serp Cluster Split To Sub Clusters
        api_response = api_instance.serp_cluster_split_to_sub_clusters(workspace_id, serp_cluster_group_sub_clusters_request)
        print("The response of SERPApi->serp_cluster_split_to_sub_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPApi->serp_cluster_split_to_sub_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **serp_cluster_group_sub_clusters_request** | [**SerpClusterGroupSubClustersRequest**](SerpClusterGroupSubClustersRequest.md)|  | 

### Return type

**List[List[str]]**

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

