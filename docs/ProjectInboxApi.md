# flowhunt.ProjectInboxApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive**](ProjectInboxApi.md#archive) | **POST** /v2/projects/{project_id}/inbox/{entry_id}/archive | Archive
[**delete_entry**](ProjectInboxApi.md#delete_entry) | **DELETE** /v2/projects/{project_id}/inbox/{entry_id} | Delete Entry
[**get_entry**](ProjectInboxApi.md#get_entry) | **GET** /v2/projects/{project_id}/inbox/{entry_id} | Get Entry
[**mark_all_read**](ProjectInboxApi.md#mark_all_read) | **POST** /v2/projects/{project_id}/inbox/mark-all-read | Mark All Read
[**mark_read**](ProjectInboxApi.md#mark_read) | **POST** /v2/projects/{project_id}/inbox/{entry_id}/read | Mark Read
[**search_project_inbox**](ProjectInboxApi.md#search_project_inbox) | **POST** /v2/projects/{project_id}/inbox/ | Search Project Inbox
[**unread_count**](ProjectInboxApi.md#unread_count) | **GET** /v2/projects/{project_id}/inbox/unread-count | Unread Count


# **archive**
> ProjectInboxEntryResponse archive(project_id, entry_id, workspace_id)

Archive

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_inbox_entry_response import ProjectInboxEntryResponse
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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Archive
        api_response = api_instance.archive(project_id, entry_id, workspace_id)
        print("The response of ProjectInboxApi->archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectInboxEntryResponse**](ProjectInboxEntryResponse.md)

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

# **delete_entry**
> Completed delete_entry(project_id, entry_id, workspace_id)

Delete Entry

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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Entry
        api_response = api_instance.delete_entry(project_id, entry_id, workspace_id)
        print("The response of ProjectInboxApi->delete_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->delete_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **entry_id** | **str**|  | 
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

# **get_entry**
> ProjectInboxEntryResponse get_entry(project_id, entry_id, workspace_id)

Get Entry

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_inbox_entry_response import ProjectInboxEntryResponse
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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Entry
        api_response = api_instance.get_entry(project_id, entry_id, workspace_id)
        print("The response of ProjectInboxApi->get_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->get_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectInboxEntryResponse**](ProjectInboxEntryResponse.md)

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

# **mark_all_read**
> Completed mark_all_read(project_id, workspace_id)

Mark All Read

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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Mark All Read
        api_response = api_instance.mark_all_read(project_id, workspace_id)
        print("The response of ProjectInboxApi->mark_all_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->mark_all_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **mark_read**
> ProjectInboxEntryResponse mark_read(project_id, entry_id, workspace_id)

Mark Read

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_inbox_entry_response import ProjectInboxEntryResponse
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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Mark Read
        api_response = api_instance.mark_read(project_id, entry_id, workspace_id)
        print("The response of ProjectInboxApi->mark_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->mark_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectInboxEntryResponse**](ProjectInboxEntryResponse.md)

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

# **search_project_inbox**
> ProjectInboxSearchResponse search_project_inbox(project_id, workspace_id, project_inbox_search_request)

Search Project Inbox

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_inbox_search_request import ProjectInboxSearchRequest
from flowhunt.models.project_inbox_search_response import ProjectInboxSearchResponse
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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    project_inbox_search_request = flowhunt.ProjectInboxSearchRequest() # ProjectInboxSearchRequest | 

    try:
        # Search Project Inbox
        api_response = api_instance.search_project_inbox(project_id, workspace_id, project_inbox_search_request)
        print("The response of ProjectInboxApi->search_project_inbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->search_project_inbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **project_inbox_search_request** | [**ProjectInboxSearchRequest**](ProjectInboxSearchRequest.md)|  | 

### Return type

[**ProjectInboxSearchResponse**](ProjectInboxSearchResponse.md)

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

# **unread_count**
> ProjectInboxUnreadCountResponse unread_count(project_id, workspace_id)

Unread Count

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.project_inbox_unread_count_response import ProjectInboxUnreadCountResponse
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
    api_instance = flowhunt.ProjectInboxApi(api_client)
    project_id = 'project_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Unread Count
        api_response = api_instance.unread_count(project_id, workspace_id)
        print("The response of ProjectInboxApi->unread_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInboxApi->unread_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ProjectInboxUnreadCountResponse**](ProjectInboxUnreadCountResponse.md)

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

