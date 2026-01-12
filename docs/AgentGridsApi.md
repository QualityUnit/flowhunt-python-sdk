# flowhunt.AgentGridsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_grid**](AgentGridsApi.md#create_agent_grid) | **POST** /v2/agent_grids/ | Create a Flow Table
[**delete_agent_grid**](AgentGridsApi.md#delete_agent_grid) | **DELETE** /v2/agent_grids/{agent_grid_id} | Delete a Flow Table
[**delete_row**](AgentGridsApi.md#delete_row) | **DELETE** /v2/agent_grids/{agent_grid_id}/rows/{row_id} | Delete a row
[**get_agent_grid**](AgentGridsApi.md#get_agent_grid) | **GET** /v2/agent_grids/{agent_grid_id} | Get a Flow Table
[**get_agent_grid_preview**](AgentGridsApi.md#get_agent_grid_preview) | **GET** /v2/agent_grids/{agent_grid_id}/preview | Get Flow Table preview
[**get_import_status**](AgentGridsApi.md#get_import_status) | **GET** /v2/agent_grids/{agent_grid_id}/import-status/{import_id} | Get import status
[**import_csv**](AgentGridsApi.md#import_csv) | **POST** /v2/agent_grids/{agent_grid_id}/import-csv | Import CSV
[**insert_row**](AgentGridsApi.md#insert_row) | **POST** /v2/agent_grids/{agent_grid_id}/rows | Insert a row
[**insert_rows_bulk**](AgentGridsApi.md#insert_rows_bulk) | **POST** /v2/agent_grids/{agent_grid_id}/rows/bulk | Bulk insert rows
[**list_agent_grids**](AgentGridsApi.md#list_agent_grids) | **GET** /v2/agent_grids/ | List all Flow Tables
[**search_rows**](AgentGridsApi.md#search_rows) | **POST** /v2/agent_grids/{agent_grid_id}/search | Search rows


# **create_agent_grid**
> AgentGridResponse create_agent_grid(workspace_id, agent_grid_create_request)

Create a Flow Table

Creates a new Flow Table with the specified schema.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_create_request import AgentGridCreateRequest
from flowhunt.models.agent_grid_response import AgentGridResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    agent_grid_create_request = flowhunt.AgentGridCreateRequest() # AgentGridCreateRequest | 

    try:
        # Create a Flow Table
        api_response = api_instance.create_agent_grid(workspace_id, agent_grid_create_request)
        print("The response of AgentGridsApi->create_agent_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->create_agent_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **agent_grid_create_request** | [**AgentGridCreateRequest**](AgentGridCreateRequest.md)|  | 

### Return type

[**AgentGridResponse**](AgentGridResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_grid**
> Completed delete_agent_grid(agent_grid_id, workspace_id)

Delete a Flow Table

Deletes a Flow Table and all its data.

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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete a Flow Table
        api_response = api_instance.delete_agent_grid(agent_grid_id, workspace_id)
        print("The response of AgentGridsApi->delete_agent_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->delete_agent_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
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

# **delete_row**
> Completed delete_row(agent_grid_id, row_id, workspace_id)

Delete a row

Deletes a single row from the Flow Table.

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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete a row
        api_response = api_instance.delete_row(agent_grid_id, row_id, workspace_id)
        print("The response of AgentGridsApi->delete_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->delete_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **row_id** | **str**|  | 
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

# **get_agent_grid**
> AgentGridResponse get_agent_grid(agent_grid_id, workspace_id)

Get a Flow Table

Returns details of a specific Flow Table by ID.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_response import AgentGridResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get a Flow Table
        api_response = api_instance.get_agent_grid(agent_grid_id, workspace_id)
        print("The response of AgentGridsApi->get_agent_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->get_agent_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**AgentGridResponse**](AgentGridResponse.md)

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

# **get_agent_grid_preview**
> AgentGridPreviewResponse get_agent_grid_preview(agent_grid_id, workspace_id, limit=limit)

Get Flow Table preview

Returns the first N rows of a Flow Table.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_preview_response import AgentGridPreviewResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    limit = 50 # int | Number of rows to return (optional) (default to 50)

    try:
        # Get Flow Table preview
        api_response = api_instance.get_agent_grid_preview(agent_grid_id, workspace_id, limit=limit)
        print("The response of AgentGridsApi->get_agent_grid_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->get_agent_grid_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **limit** | **int**| Number of rows to return | [optional] [default to 50]

### Return type

[**AgentGridPreviewResponse**](AgentGridPreviewResponse.md)

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

# **get_import_status**
> AgentGridImportStatusResponse get_import_status(agent_grid_id, import_id, workspace_id)

Get import status

Poll for the status of a CSV import. Returns progress, errors, and completion status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_import_status_response import AgentGridImportStatusResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    import_id = 'import_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get import status
        api_response = api_instance.get_import_status(agent_grid_id, import_id, workspace_id)
        print("The response of AgentGridsApi->get_import_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->get_import_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **import_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**AgentGridImportStatusResponse**](AgentGridImportStatusResponse.md)

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

# **import_csv**
> AgentGridImportStartResponse import_csv(agent_grid_id, workspace_id, file)

Import CSV

Start importing rows from a CSV file. The import runs asynchronously. Use the returned import_id to poll for status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_import_start_response import AgentGridImportStartResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file = None # bytearray | CSV file to import

    try:
        # Import CSV
        api_response = api_instance.import_csv(agent_grid_id, workspace_id, file)
        print("The response of AgentGridsApi->import_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->import_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file** | **bytearray**| CSV file to import | 

### Return type

[**AgentGridImportStartResponse**](AgentGridImportStartResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_row**
> AgentGridRowInsertResponse insert_row(agent_grid_id, workspace_id, agent_grid_row_insert_request)

Insert a row

Inserts a single row into the Flow Table.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_row_insert_request import AgentGridRowInsertRequest
from flowhunt.models.agent_grid_row_insert_response import AgentGridRowInsertResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    agent_grid_row_insert_request = flowhunt.AgentGridRowInsertRequest() # AgentGridRowInsertRequest | 

    try:
        # Insert a row
        api_response = api_instance.insert_row(agent_grid_id, workspace_id, agent_grid_row_insert_request)
        print("The response of AgentGridsApi->insert_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->insert_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **agent_grid_row_insert_request** | [**AgentGridRowInsertRequest**](AgentGridRowInsertRequest.md)|  | 

### Return type

[**AgentGridRowInsertResponse**](AgentGridRowInsertResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_rows_bulk**
> AgentGridBulkInsertResponse insert_rows_bulk(agent_grid_id, workspace_id, agent_grid_rows_bulk_insert_request)

Bulk insert rows

Inserts multiple rows into the Flow Table.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_bulk_insert_response import AgentGridBulkInsertResponse
from flowhunt.models.agent_grid_rows_bulk_insert_request import AgentGridRowsBulkInsertRequest
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    agent_grid_rows_bulk_insert_request = flowhunt.AgentGridRowsBulkInsertRequest() # AgentGridRowsBulkInsertRequest | 

    try:
        # Bulk insert rows
        api_response = api_instance.insert_rows_bulk(agent_grid_id, workspace_id, agent_grid_rows_bulk_insert_request)
        print("The response of AgentGridsApi->insert_rows_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->insert_rows_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **agent_grid_rows_bulk_insert_request** | [**AgentGridRowsBulkInsertRequest**](AgentGridRowsBulkInsertRequest.md)|  | 

### Return type

[**AgentGridBulkInsertResponse**](AgentGridBulkInsertResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_grids**
> List[AgentGridResponse] list_agent_grids(workspace_id)

List all Flow Tables

Returns a list of all Flow Tables (Agent Grids) for the workspace.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_response import AgentGridResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List all Flow Tables
        api_response = api_instance.list_agent_grids(workspace_id)
        print("The response of AgentGridsApi->list_agent_grids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->list_agent_grids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[AgentGridResponse]**](AgentGridResponse.md)

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

# **search_rows**
> AgentGridSearchResponse search_rows(agent_grid_id, workspace_id, agent_grid_search_request)

Search rows

Search rows in the Flow Table using full-text search.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.agent_grid_search_request import AgentGridSearchRequest
from flowhunt.models.agent_grid_search_response import AgentGridSearchResponse
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
    api_instance = flowhunt.AgentGridsApi(api_client)
    agent_grid_id = 'agent_grid_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    agent_grid_search_request = flowhunt.AgentGridSearchRequest() # AgentGridSearchRequest | 

    try:
        # Search rows
        api_response = api_instance.search_rows(agent_grid_id, workspace_id, agent_grid_search_request)
        print("The response of AgentGridsApi->search_rows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGridsApi->search_rows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grid_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **agent_grid_search_request** | [**AgentGridSearchRequest**](AgentGridSearchRequest.md)|  | 

### Return type

[**AgentGridSearchResponse**](AgentGridSearchResponse.md)

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

