# flowhunt.SchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedules**](SchedulesApi.md#create_schedules) | **POST** /v2/schedules/create | Create Schedules
[**delete_schedule**](SchedulesApi.md#delete_schedule) | **DELETE** /v2/schedules/{schedule_id} | Delete Schedule
[**get_schedule**](SchedulesApi.md#get_schedule) | **GET** /v2/schedules/{schedule_id} | Get Schedule
[**get_schedule_url_details**](SchedulesApi.md#get_schedule_url_details) | **GET** /v2/schedules/{schedule_id}/urls/{domain_id}/{url_id} | Get Schedule Url Details
[**get_schedules**](SchedulesApi.md#get_schedules) | **POST** /v2/schedules/ | Get Schedules
[**run_schedule**](SchedulesApi.md#run_schedule) | **POST** /v2/schedules/run/{schedule_id} | Run Schedule
[**search_schedule_urls**](SchedulesApi.md#search_schedule_urls) | **POST** /v2/schedules/urls/ | Search Schedule Urls
[**update_schedule**](SchedulesApi.md#update_schedule) | **PUT** /v2/schedules/{schedule_id} | Update Schedule


# **create_schedules**
> List[ScheduleResponse] create_schedules(workspace_id, schedule_create_request)

Create Schedules

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.schedule_create_request import ScheduleCreateRequest
from flowhunt.models.schedule_response import ScheduleResponse
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
    api_instance = flowhunt.SchedulesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    schedule_create_request = [flowhunt.ScheduleCreateRequest()] # List[ScheduleCreateRequest] | 

    try:
        # Create Schedules
        api_response = api_instance.create_schedules(workspace_id, schedule_create_request)
        print("The response of SchedulesApi->create_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->create_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **schedule_create_request** | [**List[ScheduleCreateRequest]**](ScheduleCreateRequest.md)|  | 

### Return type

[**List[ScheduleResponse]**](ScheduleResponse.md)

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

# **delete_schedule**
> Completed delete_schedule(schedule_id, workspace_id)

Delete Schedule

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
    api_instance = flowhunt.SchedulesApi(api_client)
    schedule_id = 'schedule_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Schedule
        api_response = api_instance.delete_schedule(schedule_id, workspace_id)
        print("The response of SchedulesApi->delete_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->delete_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
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

# **get_schedule**
> ScheduleResponse get_schedule(schedule_id, workspace_id)

Get Schedule

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.schedule_response import ScheduleResponse
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
    api_instance = flowhunt.SchedulesApi(api_client)
    schedule_id = 'schedule_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Schedule
        api_response = api_instance.get_schedule(schedule_id, workspace_id)
        print("The response of SchedulesApi->get_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ScheduleResponse**](ScheduleResponse.md)

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

# **get_schedule_url_details**
> ScheduleUrlDetailResponse get_schedule_url_details(schedule_id, url_id, domain_id, workspace_id)

Get Schedule Url Details

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.schedule_url_detail_response import ScheduleUrlDetailResponse
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
    api_instance = flowhunt.SchedulesApi(api_client)
    schedule_id = 'schedule_id_example' # str | 
    url_id = 'url_id_example' # str | 
    domain_id = 'domain_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Schedule Url Details
        api_response = api_instance.get_schedule_url_details(schedule_id, url_id, domain_id, workspace_id)
        print("The response of SchedulesApi->get_schedule_url_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedule_url_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **url_id** | **str**|  | 
 **domain_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ScheduleUrlDetailResponse**](ScheduleUrlDetailResponse.md)

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

# **get_schedules**
> List[ScheduleResponse] get_schedules(workspace_id, schedule_search_request)

Get Schedules

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.schedule_response import ScheduleResponse
from flowhunt.models.schedule_search_request import ScheduleSearchRequest
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
    api_instance = flowhunt.SchedulesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    schedule_search_request = flowhunt.ScheduleSearchRequest() # ScheduleSearchRequest | 

    try:
        # Get Schedules
        api_response = api_instance.get_schedules(workspace_id, schedule_search_request)
        print("The response of SchedulesApi->get_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **schedule_search_request** | [**ScheduleSearchRequest**](ScheduleSearchRequest.md)|  | 

### Return type

[**List[ScheduleResponse]**](ScheduleResponse.md)

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

# **run_schedule**
> Completed run_schedule(schedule_id, workspace_id)

Run Schedule

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
    api_instance = flowhunt.SchedulesApi(api_client)
    schedule_id = 'schedule_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Run Schedule
        api_response = api_instance.run_schedule(schedule_id, workspace_id)
        print("The response of SchedulesApi->run_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->run_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
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

# **search_schedule_urls**
> List[ScheduleUrlResponse] search_schedule_urls(workspace_id, schedule_url_search_request)

Search Schedule Urls

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.schedule_url_response import ScheduleUrlResponse
from flowhunt.models.schedule_url_search_request import ScheduleUrlSearchRequest
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
    api_instance = flowhunt.SchedulesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    schedule_url_search_request = flowhunt.ScheduleUrlSearchRequest() # ScheduleUrlSearchRequest | 

    try:
        # Search Schedule Urls
        api_response = api_instance.search_schedule_urls(workspace_id, schedule_url_search_request)
        print("The response of SchedulesApi->search_schedule_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->search_schedule_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **schedule_url_search_request** | [**ScheduleUrlSearchRequest**](ScheduleUrlSearchRequest.md)|  | 

### Return type

[**List[ScheduleUrlResponse]**](ScheduleUrlResponse.md)

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

# **update_schedule**
> ScheduleResponse update_schedule(schedule_id, workspace_id, schedule_update_request)

Update Schedule

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.schedule_response import ScheduleResponse
from flowhunt.models.schedule_update_request import ScheduleUpdateRequest
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
    api_instance = flowhunt.SchedulesApi(api_client)
    schedule_id = 'schedule_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    schedule_update_request = flowhunt.ScheduleUpdateRequest() # ScheduleUpdateRequest | 

    try:
        # Update Schedule
        api_response = api_instance.update_schedule(schedule_id, workspace_id, schedule_update_request)
        print("The response of SchedulesApi->update_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->update_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **schedule_update_request** | [**ScheduleUpdateRequest**](ScheduleUpdateRequest.md)|  | 

### Return type

[**ScheduleResponse**](ScheduleResponse.md)

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

