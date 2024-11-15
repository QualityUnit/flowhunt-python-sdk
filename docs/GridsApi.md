# flowhunt.GridsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_column**](GridsApi.md#create_column) | **POST** /v2/grids/{grid_id}/create | Create Column
[**create_grid**](GridsApi.md#create_grid) | **POST** /v2/grids/create | Create Grid
[**create_grid_row**](GridsApi.md#create_grid_row) | **POST** /v2/grids/{grid_id}/create_row | Create Grid Row
[**delete_grid**](GridsApi.md#delete_grid) | **DELETE** /v2/grids/{grid_id} | Delete Grid
[**delete_grid_row**](GridsApi.md#delete_grid_row) | **DELETE** /v2/grids/{grid_id}/{col_id} | Delete Grid Row
[**search_columns**](GridsApi.md#search_columns) | **POST** /v2/grids/{grid_id}/search | Search Columns
[**search_grid_rows**](GridsApi.md#search_grid_rows) | **POST** /v2/grids/{grid_id}/search_rows | Search Grid Rows
[**search_grids**](GridsApi.md#search_grids) | **POST** /v2/grids/search | Search Grids
[**update_column**](GridsApi.md#update_column) | **PUT** /v2/grids/{grid_id}/{col_id} | Update Column
[**update_grid**](GridsApi.md#update_grid) | **PUT** /v2/grids/{grid_id} | Update Grid
[**update_grid_row**](GridsApi.md#update_grid_row) | **PUT** /v2/grids/{grid_id}/row_id | Update Grid Row


# **create_column**
> GridColumnResponse create_column(grid_id, workspace_id, grid_column_create_request)

Create Column

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_column_create_request import GridColumnCreateRequest
from flowhunt.models.grid_column_response import GridColumnResponse
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    grid_column_create_request = flowhunt.GridColumnCreateRequest() # GridColumnCreateRequest | 

    try:
        # Create Column
        api_response = api_instance.create_column(grid_id, workspace_id, grid_column_create_request)
        print("The response of GridsApi->create_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->create_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **grid_column_create_request** | [**GridColumnCreateRequest**](GridColumnCreateRequest.md)|  | 

### Return type

[**GridColumnResponse**](GridColumnResponse.md)

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

# **create_grid**
> GridResponse create_grid(workspace_id, grid_create_request)

Create Grid

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_create_request import GridCreateRequest
from flowhunt.models.grid_response import GridResponse
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
    api_instance = flowhunt.GridsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    grid_create_request = flowhunt.GridCreateRequest() # GridCreateRequest | 

    try:
        # Create Grid
        api_response = api_instance.create_grid(workspace_id, grid_create_request)
        print("The response of GridsApi->create_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->create_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **grid_create_request** | [**GridCreateRequest**](GridCreateRequest.md)|  | 

### Return type

[**GridResponse**](GridResponse.md)

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

# **create_grid_row**
> GridRowResponse create_grid_row(grid_id, workspace_id, grid_row_create_request)

Create Grid Row

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_row_create_request import GridRowCreateRequest
from flowhunt.models.grid_row_response import GridRowResponse
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    grid_row_create_request = flowhunt.GridRowCreateRequest() # GridRowCreateRequest | 

    try:
        # Create Grid Row
        api_response = api_instance.create_grid_row(grid_id, workspace_id, grid_row_create_request)
        print("The response of GridsApi->create_grid_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->create_grid_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **grid_row_create_request** | [**GridRowCreateRequest**](GridRowCreateRequest.md)|  | 

### Return type

[**GridRowResponse**](GridRowResponse.md)

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

# **delete_grid**
> Completed delete_grid(grid_id, workspace_id)

Delete Grid

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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Grid
        api_response = api_instance.delete_grid(grid_id, workspace_id)
        print("The response of GridsApi->delete_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->delete_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
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

# **delete_grid_row**
> Completed delete_grid_row(grid_id, col_id, workspace_id)

Delete Grid Row

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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    col_id = 'col_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Grid Row
        api_response = api_instance.delete_grid_row(grid_id, col_id, workspace_id)
        print("The response of GridsApi->delete_grid_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->delete_grid_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **col_id** | **str**|  | 
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

# **search_columns**
> List[GridColumnResponse] search_columns(grid_id, workspace_id, grid_column_search_request)

Search Columns

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_column_response import GridColumnResponse
from flowhunt.models.grid_column_search_request import GridColumnSearchRequest
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    grid_column_search_request = flowhunt.GridColumnSearchRequest() # GridColumnSearchRequest | 

    try:
        # Search Columns
        api_response = api_instance.search_columns(grid_id, workspace_id, grid_column_search_request)
        print("The response of GridsApi->search_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->search_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **grid_column_search_request** | [**GridColumnSearchRequest**](GridColumnSearchRequest.md)|  | 

### Return type

[**List[GridColumnResponse]**](GridColumnResponse.md)

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

# **search_grid_rows**
> List[GridRowResponse] search_grid_rows(grid_id, workspace_id, grid_row_search_request)

Search Grid Rows

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_row_response import GridRowResponse
from flowhunt.models.grid_row_search_request import GridRowSearchRequest
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    grid_row_search_request = flowhunt.GridRowSearchRequest() # GridRowSearchRequest | 

    try:
        # Search Grid Rows
        api_response = api_instance.search_grid_rows(grid_id, workspace_id, grid_row_search_request)
        print("The response of GridsApi->search_grid_rows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->search_grid_rows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **grid_row_search_request** | [**GridRowSearchRequest**](GridRowSearchRequest.md)|  | 

### Return type

[**List[GridRowResponse]**](GridRowResponse.md)

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

# **search_grids**
> List[GridResponse] search_grids(workspace_id, grid_search_request)

Search Grids

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_response import GridResponse
from flowhunt.models.grid_search_request import GridSearchRequest
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
    api_instance = flowhunt.GridsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    grid_search_request = flowhunt.GridSearchRequest() # GridSearchRequest | 

    try:
        # Search Grids
        api_response = api_instance.search_grids(workspace_id, grid_search_request)
        print("The response of GridsApi->search_grids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->search_grids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **grid_search_request** | [**GridSearchRequest**](GridSearchRequest.md)|  | 

### Return type

[**List[GridResponse]**](GridResponse.md)

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

# **update_column**
> GridColumnResponse update_column(grid_id, col_id, workspace_id, grid_column_update_request)

Update Column

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_column_response import GridColumnResponse
from flowhunt.models.grid_column_update_request import GridColumnUpdateRequest
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    col_id = 'col_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    grid_column_update_request = flowhunt.GridColumnUpdateRequest() # GridColumnUpdateRequest | 

    try:
        # Update Column
        api_response = api_instance.update_column(grid_id, col_id, workspace_id, grid_column_update_request)
        print("The response of GridsApi->update_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->update_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **col_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **grid_column_update_request** | [**GridColumnUpdateRequest**](GridColumnUpdateRequest.md)|  | 

### Return type

[**GridColumnResponse**](GridColumnResponse.md)

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

# **update_grid**
> GridResponse update_grid(grid_id, workspace_id, grid_update_request)

Update Grid

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_response import GridResponse
from flowhunt.models.grid_update_request import GridUpdateRequest
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    grid_update_request = flowhunt.GridUpdateRequest() # GridUpdateRequest | 

    try:
        # Update Grid
        api_response = api_instance.update_grid(grid_id, workspace_id, grid_update_request)
        print("The response of GridsApi->update_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->update_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **grid_update_request** | [**GridUpdateRequest**](GridUpdateRequest.md)|  | 

### Return type

[**GridResponse**](GridResponse.md)

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

# **update_grid_row**
> GridRowResponse update_grid_row(grid_id, workspace_id, row_id, grid_row_update_request)

Update Grid Row

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.grid_row_response import GridRowResponse
from flowhunt.models.grid_row_update_request import GridRowUpdateRequest
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
    api_instance = flowhunt.GridsApi(api_client)
    grid_id = 'grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    row_id = 'row_id_example' # str | 
    grid_row_update_request = flowhunt.GridRowUpdateRequest() # GridRowUpdateRequest | 

    try:
        # Update Grid Row
        api_response = api_instance.update_grid_row(grid_id, workspace_id, row_id, grid_row_update_request)
        print("The response of GridsApi->update_grid_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->update_grid_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **row_id** | **str**|  | 
 **grid_row_update_request** | [**GridRowUpdateRequest**](GridRowUpdateRequest.md)|  | 

### Return type

[**GridRowResponse**](GridRowResponse.md)

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

