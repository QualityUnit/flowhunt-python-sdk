# flowhunt.TrackingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_events**](TrackingApi.md#search_events) | **POST** /v2/tracking/events | Search Events
[**search_links**](TrackingApi.md#search_links) | **POST** /v2/tracking/links | Search Links
[**search_sources**](TrackingApi.md#search_sources) | **POST** /v2/tracking/sources | Search Sources
[**track_click**](TrackingApi.md#track_click) | **POST** /v2/tracking/clk | Track Click
[**track_event**](TrackingApi.md#track_event) | **POST** /v2/tracking/evnt | Track Event
[**track_link**](TrackingApi.md#track_link) | **POST** /v2/tracking/lnk | Track Link


# **search_events**
> TrackingEventsResponse search_events(workspace_id, tracking_event_search_request)

Search Events

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.tracking_event_search_request import TrackingEventSearchRequest
from flowhunt.models.tracking_events_response import TrackingEventsResponse
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
    api_instance = flowhunt.TrackingApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    tracking_event_search_request = flowhunt.TrackingEventSearchRequest() # TrackingEventSearchRequest | 

    try:
        # Search Events
        api_response = api_instance.search_events(workspace_id, tracking_event_search_request)
        print("The response of TrackingApi->search_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->search_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **tracking_event_search_request** | [**TrackingEventSearchRequest**](TrackingEventSearchRequest.md)|  | 

### Return type

[**TrackingEventsResponse**](TrackingEventsResponse.md)

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

# **search_links**
> TrackingLinksResponse search_links(workspace_id, tracking_link_search_request)

Search Links

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.tracking_link_search_request import TrackingLinkSearchRequest
from flowhunt.models.tracking_links_response import TrackingLinksResponse
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
    api_instance = flowhunt.TrackingApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    tracking_link_search_request = flowhunt.TrackingLinkSearchRequest() # TrackingLinkSearchRequest | 

    try:
        # Search Links
        api_response = api_instance.search_links(workspace_id, tracking_link_search_request)
        print("The response of TrackingApi->search_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->search_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **tracking_link_search_request** | [**TrackingLinkSearchRequest**](TrackingLinkSearchRequest.md)|  | 

### Return type

[**TrackingLinksResponse**](TrackingLinksResponse.md)

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

# **search_sources**
> TrackingSourcesResponse search_sources(workspace_id, tracking_source_search_request)

Search Sources

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.tracking_source_search_request import TrackingSourceSearchRequest
from flowhunt.models.tracking_sources_response import TrackingSourcesResponse
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
    api_instance = flowhunt.TrackingApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    tracking_source_search_request = flowhunt.TrackingSourceSearchRequest() # TrackingSourceSearchRequest | 

    try:
        # Search Sources
        api_response = api_instance.search_sources(workspace_id, tracking_source_search_request)
        print("The response of TrackingApi->search_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->search_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **tracking_source_search_request** | [**TrackingSourceSearchRequest**](TrackingSourceSearchRequest.md)|  | 

### Return type

[**TrackingSourcesResponse**](TrackingSourcesResponse.md)

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

# **track_click**
> Completed track_click(workspace_id, tracking_source_create_request)

Track Click

### Example


```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.tracking_source_create_request import TrackingSourceCreateRequest
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
    api_instance = flowhunt.TrackingApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    tracking_source_create_request = flowhunt.TrackingSourceCreateRequest() # TrackingSourceCreateRequest | 

    try:
        # Track Click
        api_response = api_instance.track_click(workspace_id, tracking_source_create_request)
        print("The response of TrackingApi->track_click:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->track_click: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **tracking_source_create_request** | [**TrackingSourceCreateRequest**](TrackingSourceCreateRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **track_event**
> Completed track_event(workspace_id, tracking_event_create_requests)

Track Event

### Example


```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.tracking_event_create_requests import TrackingEventCreateRequests
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
    api_instance = flowhunt.TrackingApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    tracking_event_create_requests = flowhunt.TrackingEventCreateRequests() # TrackingEventCreateRequests | 

    try:
        # Track Event
        api_response = api_instance.track_event(workspace_id, tracking_event_create_requests)
        print("The response of TrackingApi->track_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->track_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **tracking_event_create_requests** | [**TrackingEventCreateRequests**](TrackingEventCreateRequests.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **track_link**
> Completed track_link(workspace_id, tracking_links_create_request)

Track Link

### Example


```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.tracking_links_create_request import TrackingLinksCreateRequest
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
    api_instance = flowhunt.TrackingApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    tracking_links_create_request = flowhunt.TrackingLinksCreateRequest() # TrackingLinksCreateRequest | 

    try:
        # Track Link
        api_response = api_instance.track_link(workspace_id, tracking_links_create_request)
        print("The response of TrackingApi->track_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->track_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **tracking_links_create_request** | [**TrackingLinksCreateRequest**](TrackingLinksCreateRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

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

