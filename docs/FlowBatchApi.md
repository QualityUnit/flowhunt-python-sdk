# flowhunt.FlowBatchApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rows**](FlowBatchApi.md#add_rows) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/rows | Add Rows
[**add_rows_0**](FlowBatchApi.md#add_rows_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/rows | Add Rows
[**create_batch_run**](FlowBatchApi.md#create_batch_run) | **POST** /v2/flows/{flow_id}/batch | Create Batch Run
[**create_batch_run_0**](FlowBatchApi.md#create_batch_run_0) | **POST** /v2/flows/{flow_id}/batch | Create Batch Run
[**delete_batch_run**](FlowBatchApi.md#delete_batch_run) | **DELETE** /v2/flows/{flow_id}/batch/{batch_run_id} | Delete Batch Run
[**delete_batch_run_0**](FlowBatchApi.md#delete_batch_run_0) | **DELETE** /v2/flows/{flow_id}/batch/{batch_run_id} | Delete Batch Run
[**delete_row**](FlowBatchApi.md#delete_row) | **DELETE** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id} | Delete Row
[**delete_row_0**](FlowBatchApi.md#delete_row_0) | **DELETE** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id} | Delete Row
[**execute_batch**](FlowBatchApi.md#execute_batch) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/execute | Execute Batch
[**execute_batch_0**](FlowBatchApi.md#execute_batch_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/execute | Execute Batch
[**execute_filtered**](FlowBatchApi.md#execute_filtered) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/execute-filtered | Execute Filtered
[**execute_filtered_0**](FlowBatchApi.md#execute_filtered_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/execute-filtered | Execute Filtered
[**execute_row**](FlowBatchApi.md#execute_row) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id}/execute | Execute Row
[**execute_row_0**](FlowBatchApi.md#execute_row_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id}/execute | Execute Row
[**export_csv**](FlowBatchApi.md#export_csv) | **GET** /v2/flows/{flow_id}/batch/{batch_run_id}/export-csv | Export Csv
[**export_csv_0**](FlowBatchApi.md#export_csv_0) | **GET** /v2/flows/{flow_id}/batch/{batch_run_id}/export-csv | Export Csv
[**get_batch_run**](FlowBatchApi.md#get_batch_run) | **GET** /v2/flows/{flow_id}/batch/{batch_run_id} | Get Batch Run
[**get_batch_run_0**](FlowBatchApi.md#get_batch_run_0) | **GET** /v2/flows/{flow_id}/batch/{batch_run_id} | Get Batch Run
[**get_export_zip_status**](FlowBatchApi.md#get_export_zip_status) | **GET** /v2/flows/{flow_id}/batch/{batch_run_id}/export-zip/{task_id} | Get Export Zip Status
[**get_export_zip_status_0**](FlowBatchApi.md#get_export_zip_status_0) | **GET** /v2/flows/{flow_id}/batch/{batch_run_id}/export-zip/{task_id} | Get Export Zip Status
[**import_csv**](FlowBatchApi.md#import_csv) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/import-csv | Import Csv
[**import_csv_0**](FlowBatchApi.md#import_csv_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/import-csv | Import Csv
[**list_batch_runs**](FlowBatchApi.md#list_batch_runs) | **GET** /v2/flows/{flow_id}/batch | List Batch Runs
[**list_batch_runs_0**](FlowBatchApi.md#list_batch_runs_0) | **GET** /v2/flows/{flow_id}/batch | List Batch Runs
[**start_export_zip**](FlowBatchApi.md#start_export_zip) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/export-zip | Start Export Zip
[**start_export_zip_0**](FlowBatchApi.md#start_export_zip_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/export-zip | Start Export Zip
[**stop_all_rows**](FlowBatchApi.md#stop_all_rows) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/stop-all | Stop All Rows
[**stop_all_rows_0**](FlowBatchApi.md#stop_all_rows_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/stop-all | Stop All Rows
[**stop_row**](FlowBatchApi.md#stop_row) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id}/stop | Stop Row
[**stop_row_0**](FlowBatchApi.md#stop_row_0) | **POST** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id}/stop | Stop Row
[**update_batch_run**](FlowBatchApi.md#update_batch_run) | **PUT** /v2/flows/{flow_id}/batch/{batch_run_id} | Update Batch Run
[**update_batch_run_0**](FlowBatchApi.md#update_batch_run_0) | **PUT** /v2/flows/{flow_id}/batch/{batch_run_id} | Update Batch Run
[**update_row**](FlowBatchApi.md#update_row) | **PUT** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id} | Update Row
[**update_row_0**](FlowBatchApi.md#update_row_0) | **PUT** /v2/flows/{flow_id}/batch/{batch_run_id}/rows/{row_id} | Update Row


# **add_rows**
> List[FlowBatchRowResponse] add_rows(flow_id, batch_run_id, workspace_id, flow_batch_rows_bulk_create_request)

Add Rows

Add one or more rows to a batch run.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
from flowhunt.models.flow_batch_rows_bulk_create_request import FlowBatchRowsBulkCreateRequest
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_rows_bulk_create_request = flowhunt.FlowBatchRowsBulkCreateRequest() # FlowBatchRowsBulkCreateRequest | 

    try:
        # Add Rows
        api_response = api_instance.add_rows(flow_id, batch_run_id, workspace_id, flow_batch_rows_bulk_create_request)
        print("The response of FlowBatchApi->add_rows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->add_rows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_rows_bulk_create_request** | [**FlowBatchRowsBulkCreateRequest**](FlowBatchRowsBulkCreateRequest.md)|  | 

### Return type

[**List[FlowBatchRowResponse]**](FlowBatchRowResponse.md)

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

# **add_rows_0**
> List[FlowBatchRowResponse] add_rows_0(flow_id, batch_run_id, workspace_id, flow_batch_rows_bulk_create_request)

Add Rows

Add one or more rows to a batch run.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
from flowhunt.models.flow_batch_rows_bulk_create_request import FlowBatchRowsBulkCreateRequest
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_rows_bulk_create_request = flowhunt.FlowBatchRowsBulkCreateRequest() # FlowBatchRowsBulkCreateRequest | 

    try:
        # Add Rows
        api_response = api_instance.add_rows_0(flow_id, batch_run_id, workspace_id, flow_batch_rows_bulk_create_request)
        print("The response of FlowBatchApi->add_rows_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->add_rows_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_rows_bulk_create_request** | [**FlowBatchRowsBulkCreateRequest**](FlowBatchRowsBulkCreateRequest.md)|  | 

### Return type

[**List[FlowBatchRowResponse]**](FlowBatchRowResponse.md)

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

# **create_batch_run**
> FlowBatchRunResponse create_batch_run(flow_id, workspace_id, flow_batch_run_create_request)

Create Batch Run

Create a new batch run for a flow.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_create_request import FlowBatchRunCreateRequest
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_run_create_request = flowhunt.FlowBatchRunCreateRequest() # FlowBatchRunCreateRequest | 

    try:
        # Create Batch Run
        api_response = api_instance.create_batch_run(flow_id, workspace_id, flow_batch_run_create_request)
        print("The response of FlowBatchApi->create_batch_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->create_batch_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_run_create_request** | [**FlowBatchRunCreateRequest**](FlowBatchRunCreateRequest.md)|  | 

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **create_batch_run_0**
> FlowBatchRunResponse create_batch_run_0(flow_id, workspace_id, flow_batch_run_create_request)

Create Batch Run

Create a new batch run for a flow.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_create_request import FlowBatchRunCreateRequest
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_run_create_request = flowhunt.FlowBatchRunCreateRequest() # FlowBatchRunCreateRequest | 

    try:
        # Create Batch Run
        api_response = api_instance.create_batch_run_0(flow_id, workspace_id, flow_batch_run_create_request)
        print("The response of FlowBatchApi->create_batch_run_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->create_batch_run_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_run_create_request** | [**FlowBatchRunCreateRequest**](FlowBatchRunCreateRequest.md)|  | 

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **delete_batch_run**
> Completed delete_batch_run(flow_id, batch_run_id, workspace_id)

Delete Batch Run

Delete a batch run and all its rows.

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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Batch Run
        api_response = api_instance.delete_batch_run(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->delete_batch_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->delete_batch_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
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

# **delete_batch_run_0**
> Completed delete_batch_run_0(flow_id, batch_run_id, workspace_id)

Delete Batch Run

Delete a batch run and all its rows.

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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Batch Run
        api_response = api_instance.delete_batch_run_0(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->delete_batch_run_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->delete_batch_run_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
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
> Completed delete_row(flow_id, batch_run_id, row_id, workspace_id)

Delete Row

Delete a row from a batch run.

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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Row
        api_response = api_instance.delete_row(flow_id, batch_run_id, row_id, workspace_id)
        print("The response of FlowBatchApi->delete_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->delete_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
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

# **delete_row_0**
> Completed delete_row_0(flow_id, batch_run_id, row_id, workspace_id)

Delete Row

Delete a row from a batch run.

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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Row
        api_response = api_instance.delete_row_0(flow_id, batch_run_id, row_id, workspace_id)
        print("The response of FlowBatchApi->delete_row_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->delete_row_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
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

# **execute_batch**
> FlowBatchRunResponse execute_batch(flow_id, batch_run_id, workspace_id, rerun_all=rerun_all)

Execute Batch

Execute pending rows (or all non-running rows when rerun_all=true) in the batch run.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    rerun_all = False # bool |  (optional) (default to False)

    try:
        # Execute Batch
        api_response = api_instance.execute_batch(flow_id, batch_run_id, workspace_id, rerun_all=rerun_all)
        print("The response of FlowBatchApi->execute_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->execute_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **rerun_all** | **bool**|  | [optional] [default to False]

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **execute_batch_0**
> FlowBatchRunResponse execute_batch_0(flow_id, batch_run_id, workspace_id, rerun_all=rerun_all)

Execute Batch

Execute pending rows (or all non-running rows when rerun_all=true) in the batch run.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    rerun_all = False # bool |  (optional) (default to False)

    try:
        # Execute Batch
        api_response = api_instance.execute_batch_0(flow_id, batch_run_id, workspace_id, rerun_all=rerun_all)
        print("The response of FlowBatchApi->execute_batch_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->execute_batch_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **rerun_all** | **bool**|  | [optional] [default to False]

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **execute_filtered**
> FlowBatchRunResponse execute_filtered(flow_id, batch_run_id, workspace_id, flow_batch_filtered_execute_request)

Execute Filtered

Execute rows matching an optional search filter.

- ``rerun_all=false`` — run only **pending** rows matching the filter.
- ``rerun_all=true``  — reset matching completed/failed rows to pending,
  then run them.
- ``max_concurrency`` — optional override for ``max_parallel`` (capped by
  the subscription plan limit).

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_filtered_execute_request import FlowBatchFilteredExecuteRequest
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_filtered_execute_request = flowhunt.FlowBatchFilteredExecuteRequest() # FlowBatchFilteredExecuteRequest | 

    try:
        # Execute Filtered
        api_response = api_instance.execute_filtered(flow_id, batch_run_id, workspace_id, flow_batch_filtered_execute_request)
        print("The response of FlowBatchApi->execute_filtered:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->execute_filtered: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_filtered_execute_request** | [**FlowBatchFilteredExecuteRequest**](FlowBatchFilteredExecuteRequest.md)|  | 

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **execute_filtered_0**
> FlowBatchRunResponse execute_filtered_0(flow_id, batch_run_id, workspace_id, flow_batch_filtered_execute_request)

Execute Filtered

Execute rows matching an optional search filter.

- ``rerun_all=false`` — run only **pending** rows matching the filter.
- ``rerun_all=true``  — reset matching completed/failed rows to pending,
  then run them.
- ``max_concurrency`` — optional override for ``max_parallel`` (capped by
  the subscription plan limit).

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_filtered_execute_request import FlowBatchFilteredExecuteRequest
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_filtered_execute_request = flowhunt.FlowBatchFilteredExecuteRequest() # FlowBatchFilteredExecuteRequest | 

    try:
        # Execute Filtered
        api_response = api_instance.execute_filtered_0(flow_id, batch_run_id, workspace_id, flow_batch_filtered_execute_request)
        print("The response of FlowBatchApi->execute_filtered_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->execute_filtered_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_filtered_execute_request** | [**FlowBatchFilteredExecuteRequest**](FlowBatchFilteredExecuteRequest.md)|  | 

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **execute_row**
> FlowBatchRowResponse execute_row(flow_id, batch_run_id, row_id, workspace_id)

Execute Row

Execute a single row in the batch run.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Execute Row
        api_response = api_instance.execute_row(flow_id, batch_run_id, row_id, workspace_id)
        print("The response of FlowBatchApi->execute_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->execute_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **row_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**FlowBatchRowResponse**](FlowBatchRowResponse.md)

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

# **execute_row_0**
> FlowBatchRowResponse execute_row_0(flow_id, batch_run_id, row_id, workspace_id)

Execute Row

Execute a single row in the batch run.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Execute Row
        api_response = api_instance.execute_row_0(flow_id, batch_run_id, row_id, workspace_id)
        print("The response of FlowBatchApi->execute_row_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->execute_row_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **row_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**FlowBatchRowResponse**](FlowBatchRowResponse.md)

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

# **export_csv**
> object export_csv(flow_id, batch_run_id, workspace_id)

Export Csv

Export batch results as CSV.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Export Csv
        api_response = api_instance.export_csv(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->export_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->export_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

**object**

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

# **export_csv_0**
> object export_csv_0(flow_id, batch_run_id, workspace_id)

Export Csv

Export batch results as CSV.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Export Csv
        api_response = api_instance.export_csv_0(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->export_csv_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->export_csv_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

**object**

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

# **get_batch_run**
> FlowBatchRunDetailResponse get_batch_run(flow_id, batch_run_id, workspace_id, rows_limit=rows_limit, rows_cursor=rows_cursor, rows_status=rows_status)

Get Batch Run

Get batch run details with cursor-based paginated rows.

Use ``rows_cursor`` (the ``next_cursor`` from a previous response) to
fetch subsequent pages.  ``rows_status`` filters rows by their execution
status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_status import FlowBatchRowStatus
from flowhunt.models.flow_batch_run_detail_response import FlowBatchRunDetailResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    rows_limit = 50 # int |  (optional) (default to 50)
    rows_cursor = 56 # int |  (optional)
    rows_status = flowhunt.FlowBatchRowStatus() # FlowBatchRowStatus |  (optional)

    try:
        # Get Batch Run
        api_response = api_instance.get_batch_run(flow_id, batch_run_id, workspace_id, rows_limit=rows_limit, rows_cursor=rows_cursor, rows_status=rows_status)
        print("The response of FlowBatchApi->get_batch_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->get_batch_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **rows_limit** | **int**|  | [optional] [default to 50]
 **rows_cursor** | **int**|  | [optional] 
 **rows_status** | [**FlowBatchRowStatus**](.md)|  | [optional] 

### Return type

[**FlowBatchRunDetailResponse**](FlowBatchRunDetailResponse.md)

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

# **get_batch_run_0**
> FlowBatchRunDetailResponse get_batch_run_0(flow_id, batch_run_id, workspace_id, rows_limit=rows_limit, rows_cursor=rows_cursor, rows_status=rows_status)

Get Batch Run

Get batch run details with cursor-based paginated rows.

Use ``rows_cursor`` (the ``next_cursor`` from a previous response) to
fetch subsequent pages.  ``rows_status`` filters rows by their execution
status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_status import FlowBatchRowStatus
from flowhunt.models.flow_batch_run_detail_response import FlowBatchRunDetailResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    rows_limit = 50 # int |  (optional) (default to 50)
    rows_cursor = 56 # int |  (optional)
    rows_status = flowhunt.FlowBatchRowStatus() # FlowBatchRowStatus |  (optional)

    try:
        # Get Batch Run
        api_response = api_instance.get_batch_run_0(flow_id, batch_run_id, workspace_id, rows_limit=rows_limit, rows_cursor=rows_cursor, rows_status=rows_status)
        print("The response of FlowBatchApi->get_batch_run_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->get_batch_run_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **rows_limit** | **int**|  | [optional] [default to 50]
 **rows_cursor** | **int**|  | [optional] 
 **rows_status** | [**FlowBatchRowStatus**](.md)|  | [optional] 

### Return type

[**FlowBatchRunDetailResponse**](FlowBatchRunDetailResponse.md)

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

# **get_export_zip_status**
> TaskResponse get_export_zip_status(flow_id, batch_run_id, task_id, workspace_id)

Get Export Zip Status

Poll the status of a batch ZIP export task. Returns a presigned URL on success.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Export Zip Status
        api_response = api_instance.get_export_zip_status(flow_id, batch_run_id, task_id, workspace_id)
        print("The response of FlowBatchApi->get_export_zip_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->get_export_zip_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **get_export_zip_status_0**
> TaskResponse get_export_zip_status_0(flow_id, batch_run_id, task_id, workspace_id)

Get Export Zip Status

Poll the status of a batch ZIP export task. Returns a presigned URL on success.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Export Zip Status
        api_response = api_instance.get_export_zip_status_0(flow_id, batch_run_id, task_id, workspace_id)
        print("The response of FlowBatchApi->get_export_zip_status_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->get_export_zip_status_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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
> FlowBatchRunDetailResponse import_csv(flow_id, batch_run_id, workspace_id, file)

Import Csv

Import CSV file to populate batch rows.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_detail_response import FlowBatchRunDetailResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file = 'file_example' # str | 

    try:
        # Import Csv
        api_response = api_instance.import_csv(flow_id, batch_run_id, workspace_id, file)
        print("The response of FlowBatchApi->import_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->import_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**FlowBatchRunDetailResponse**](FlowBatchRunDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv_0**
> FlowBatchRunDetailResponse import_csv_0(flow_id, batch_run_id, workspace_id, file)

Import Csv

Import CSV file to populate batch rows.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_detail_response import FlowBatchRunDetailResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    file = 'file_example' # str | 

    try:
        # Import Csv
        api_response = api_instance.import_csv_0(flow_id, batch_run_id, workspace_id, file)
        print("The response of FlowBatchApi->import_csv_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->import_csv_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**FlowBatchRunDetailResponse**](FlowBatchRunDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_batch_runs**
> List[FlowBatchRunResponse] list_batch_runs(flow_id, workspace_id, limit=limit, offset=offset)

List Batch Runs

List all batch runs for a flow.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Batch Runs
        api_response = api_instance.list_batch_runs(flow_id, workspace_id, limit=limit, offset=offset)
        print("The response of FlowBatchApi->list_batch_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->list_batch_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[FlowBatchRunResponse]**](FlowBatchRunResponse.md)

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

# **list_batch_runs_0**
> List[FlowBatchRunResponse] list_batch_runs_0(flow_id, workspace_id, limit=limit, offset=offset)

List Batch Runs

List all batch runs for a flow.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Batch Runs
        api_response = api_instance.list_batch_runs_0(flow_id, workspace_id, limit=limit, offset=offset)
        print("The response of FlowBatchApi->list_batch_runs_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->list_batch_runs_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[FlowBatchRunResponse]**](FlowBatchRunResponse.md)

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

# **start_export_zip**
> TaskResponse start_export_zip(flow_id, batch_run_id, workspace_id)

Start Export Zip

Start an async batch ZIP export. Returns a task ID for polling.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Start Export Zip
        api_response = api_instance.start_export_zip(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->start_export_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->start_export_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **start_export_zip_0**
> TaskResponse start_export_zip_0(flow_id, batch_run_id, workspace_id)

Start Export Zip

Start an async batch ZIP export. Returns a task ID for polling.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.task_response import TaskResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Start Export Zip
        api_response = api_instance.start_export_zip_0(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->start_export_zip_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->start_export_zip_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **stop_all_rows**
> Completed stop_all_rows(flow_id, batch_run_id, workspace_id)

Stop All Rows

Stop all running rows in a batch run, resetting them to pending.

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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Stop All Rows
        api_response = api_instance.stop_all_rows(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->stop_all_rows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->stop_all_rows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
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

# **stop_all_rows_0**
> Completed stop_all_rows_0(flow_id, batch_run_id, workspace_id)

Stop All Rows

Stop all running rows in a batch run, resetting them to pending.

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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Stop All Rows
        api_response = api_instance.stop_all_rows_0(flow_id, batch_run_id, workspace_id)
        print("The response of FlowBatchApi->stop_all_rows_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->stop_all_rows_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
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

# **stop_row**
> FlowBatchRowResponse stop_row(flow_id, batch_run_id, row_id, workspace_id)

Stop Row

Stop a running row and reset it to pending status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Stop Row
        api_response = api_instance.stop_row(flow_id, batch_run_id, row_id, workspace_id)
        print("The response of FlowBatchApi->stop_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->stop_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **row_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**FlowBatchRowResponse**](FlowBatchRowResponse.md)

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

# **stop_row_0**
> FlowBatchRowResponse stop_row_0(flow_id, batch_run_id, row_id, workspace_id)

Stop Row

Stop a running row and reset it to pending status.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Stop Row
        api_response = api_instance.stop_row_0(flow_id, batch_run_id, row_id, workspace_id)
        print("The response of FlowBatchApi->stop_row_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->stop_row_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **row_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**FlowBatchRowResponse**](FlowBatchRowResponse.md)

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

# **update_batch_run**
> FlowBatchRunResponse update_batch_run(flow_id, batch_run_id, workspace_id, flow_batch_run_update_request)

Update Batch Run

Update batch run metadata.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
from flowhunt.models.flow_batch_run_update_request import FlowBatchRunUpdateRequest
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_run_update_request = flowhunt.FlowBatchRunUpdateRequest() # FlowBatchRunUpdateRequest | 

    try:
        # Update Batch Run
        api_response = api_instance.update_batch_run(flow_id, batch_run_id, workspace_id, flow_batch_run_update_request)
        print("The response of FlowBatchApi->update_batch_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->update_batch_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_run_update_request** | [**FlowBatchRunUpdateRequest**](FlowBatchRunUpdateRequest.md)|  | 

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **update_batch_run_0**
> FlowBatchRunResponse update_batch_run_0(flow_id, batch_run_id, workspace_id, flow_batch_run_update_request)

Update Batch Run

Update batch run metadata.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse
from flowhunt.models.flow_batch_run_update_request import FlowBatchRunUpdateRequest
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_run_update_request = flowhunt.FlowBatchRunUpdateRequest() # FlowBatchRunUpdateRequest | 

    try:
        # Update Batch Run
        api_response = api_instance.update_batch_run_0(flow_id, batch_run_id, workspace_id, flow_batch_run_update_request)
        print("The response of FlowBatchApi->update_batch_run_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->update_batch_run_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_run_update_request** | [**FlowBatchRunUpdateRequest**](FlowBatchRunUpdateRequest.md)|  | 

### Return type

[**FlowBatchRunResponse**](FlowBatchRunResponse.md)

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

# **update_row**
> FlowBatchRowResponse update_row(flow_id, batch_run_id, row_id, workspace_id, flow_batch_row_update_request)

Update Row

Update a row's input data.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
from flowhunt.models.flow_batch_row_update_request import FlowBatchRowUpdateRequest
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_row_update_request = flowhunt.FlowBatchRowUpdateRequest() # FlowBatchRowUpdateRequest | 

    try:
        # Update Row
        api_response = api_instance.update_row(flow_id, batch_run_id, row_id, workspace_id, flow_batch_row_update_request)
        print("The response of FlowBatchApi->update_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->update_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **row_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_row_update_request** | [**FlowBatchRowUpdateRequest**](FlowBatchRowUpdateRequest.md)|  | 

### Return type

[**FlowBatchRowResponse**](FlowBatchRowResponse.md)

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

# **update_row_0**
> FlowBatchRowResponse update_row_0(flow_id, batch_run_id, row_id, workspace_id, flow_batch_row_update_request)

Update Row

Update a row's input data.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse
from flowhunt.models.flow_batch_row_update_request import FlowBatchRowUpdateRequest
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
    api_instance = flowhunt.FlowBatchApi(api_client)
    flow_id = 'flow_id_example' # str | 
    batch_run_id = 'batch_run_id_example' # str | 
    row_id = 'row_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    flow_batch_row_update_request = flowhunt.FlowBatchRowUpdateRequest() # FlowBatchRowUpdateRequest | 

    try:
        # Update Row
        api_response = api_instance.update_row_0(flow_id, batch_run_id, row_id, workspace_id, flow_batch_row_update_request)
        print("The response of FlowBatchApi->update_row_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowBatchApi->update_row_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **batch_run_id** | **str**|  | 
 **row_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **flow_batch_row_update_request** | [**FlowBatchRowUpdateRequest**](FlowBatchRowUpdateRequest.md)|  | 

### Return type

[**FlowBatchRowResponse**](FlowBatchRowResponse.md)

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

