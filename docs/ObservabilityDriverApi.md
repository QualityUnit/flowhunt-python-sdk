# flowhunt.ObservabilityDriverApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_langfuse_observability_driver**](ObservabilityDriverApi.md#activate_langfuse_observability_driver) | **POST** /v2/observability_driver/langfuse | Activate Langfuse Observability Driver
[**activate_power_bi_observability_driver**](ObservabilityDriverApi.md#activate_power_bi_observability_driver) | **POST** /v2/observability_driver/power_bi | Activate Power Bi Observability Driver
[**create_power_bi_push_dataset**](ObservabilityDriverApi.md#create_power_bi_push_dataset) | **POST** /v2/observability_driver/power_bi/push_dataset | Create Power Bi Push Dataset
[**delete_observability_driver**](ObservabilityDriverApi.md#delete_observability_driver) | **DELETE** /v2/observability_driver/{driver_type} | Delete Observability Driver
[**get_observability_driver**](ObservabilityDriverApi.md#get_observability_driver) | **GET** /v2/observability_driver/{driver_type} | Get Observability Driver
[**get_observability_driver_workspace**](ObservabilityDriverApi.md#get_observability_driver_workspace) | **POST** /v2/observability_driver/ | Get Observability Driver Workspace
[**list_power_bi_datasets**](ObservabilityDriverApi.md#list_power_bi_datasets) | **POST** /v2/observability_driver/power_bi/datasets | List Power Bi Datasets
[**list_power_bi_tables**](ObservabilityDriverApi.md#list_power_bi_tables) | **POST** /v2/observability_driver/power_bi/tables | List Power Bi Tables
[**list_power_bi_workspaces**](ObservabilityDriverApi.md#list_power_bi_workspaces) | **GET** /v2/observability_driver/power_bi/workspaces | List Power Bi Workspaces
[**update_langfuse_observability_driver**](ObservabilityDriverApi.md#update_langfuse_observability_driver) | **PUT** /v2/observability_driver/langfuse | Update Langfuse Observability Driver
[**update_power_bi_observability_driver**](ObservabilityDriverApi.md#update_power_bi_observability_driver) | **PUT** /v2/observability_driver/power_bi | Update Power Bi Observability Driver
[**validate_push_dataset_table**](ObservabilityDriverApi.md#validate_push_dataset_table) | **POST** /v2/observability_driver/power_bi/validate_push_dataset | Validate Push Dataset Table


# **activate_langfuse_observability_driver**
> ObservabilityDriverResponse activate_langfuse_observability_driver(workspace_id, langfuse_request)

Activate Langfuse Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.langfuse_request import LangfuseRequest
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    langfuse_request = flowhunt.LangfuseRequest() # LangfuseRequest | 

    try:
        # Activate Langfuse Observability Driver
        api_response = api_instance.activate_langfuse_observability_driver(workspace_id, langfuse_request)
        print("The response of ObservabilityDriverApi->activate_langfuse_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->activate_langfuse_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **langfuse_request** | [**LangfuseRequest**](LangfuseRequest.md)|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_power_bi_observability_driver**
> ObservabilityDriverResponse activate_power_bi_observability_driver(workspace_id, power_bi_request)

Activate Power Bi Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
from flowhunt.models.power_bi_request import PowerBiRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    power_bi_request = flowhunt.PowerBiRequest() # PowerBiRequest | 

    try:
        # Activate Power Bi Observability Driver
        api_response = api_instance.activate_power_bi_observability_driver(workspace_id, power_bi_request)
        print("The response of ObservabilityDriverApi->activate_power_bi_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->activate_power_bi_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **power_bi_request** | [**PowerBiRequest**](PowerBiRequest.md)|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_power_bi_push_dataset**
> MicrosoftPowerBiPushDatasetResponse create_power_bi_push_dataset(workspace_id, power_bi_push_dataset_request)

Create Power Bi Push Dataset

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.microsoft_power_bi_push_dataset_response import MicrosoftPowerBiPushDatasetResponse
from flowhunt.models.power_bi_push_dataset_request import PowerBiPushDatasetRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    power_bi_push_dataset_request = flowhunt.PowerBiPushDatasetRequest() # PowerBiPushDatasetRequest | 

    try:
        # Create Power Bi Push Dataset
        api_response = api_instance.create_power_bi_push_dataset(workspace_id, power_bi_push_dataset_request)
        print("The response of ObservabilityDriverApi->create_power_bi_push_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->create_power_bi_push_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **power_bi_push_dataset_request** | [**PowerBiPushDatasetRequest**](PowerBiPushDatasetRequest.md)|  | 

### Return type

[**MicrosoftPowerBiPushDatasetResponse**](MicrosoftPowerBiPushDatasetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_observability_driver**
> DriverSuccessResponse delete_observability_driver(driver_type, workspace_id)

Delete Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.driver_success_response import DriverSuccessResponse
from flowhunt.models.driver_type import DriverType
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    driver_type = flowhunt.DriverType() # DriverType | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Observability Driver
        api_response = api_instance.delete_observability_driver(driver_type, workspace_id)
        print("The response of ObservabilityDriverApi->delete_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->delete_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_type** | [**DriverType**](.md)|  | 
 **workspace_id** | **str**|  | 

### Return type

[**DriverSuccessResponse**](DriverSuccessResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_driver**
> ObservabilityDriverResponse get_observability_driver(driver_type, workspace_id)

Get Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.driver_type import DriverType
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    driver_type = flowhunt.DriverType() # DriverType | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Observability Driver
        api_response = api_instance.get_observability_driver(driver_type, workspace_id)
        print("The response of ObservabilityDriverApi->get_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->get_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_type** | [**DriverType**](.md)|  | 
 **workspace_id** | **str**|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_driver_workspace**
> List[ObservabilityDriverResponse] get_observability_driver_workspace(workspace_id)

Get Observability Driver Workspace

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Observability Driver Workspace
        api_response = api_instance.get_observability_driver_workspace(workspace_id)
        print("The response of ObservabilityDriverApi->get_observability_driver_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->get_observability_driver_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[ObservabilityDriverResponse]**](ObservabilityDriverResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_power_bi_datasets**
> MicrosoftPowerBiDatasetsResponse list_power_bi_datasets(workspace_id, power_bi_dataset_request)

List Power Bi Datasets

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.microsoft_power_bi_datasets_response import MicrosoftPowerBiDatasetsResponse
from flowhunt.models.power_bi_dataset_request import PowerBiDatasetRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    power_bi_dataset_request = flowhunt.PowerBiDatasetRequest() # PowerBiDatasetRequest | 

    try:
        # List Power Bi Datasets
        api_response = api_instance.list_power_bi_datasets(workspace_id, power_bi_dataset_request)
        print("The response of ObservabilityDriverApi->list_power_bi_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->list_power_bi_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **power_bi_dataset_request** | [**PowerBiDatasetRequest**](PowerBiDatasetRequest.md)|  | 

### Return type

[**MicrosoftPowerBiDatasetsResponse**](MicrosoftPowerBiDatasetsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_power_bi_tables**
> MicrosoftPowerBiTablesResponse list_power_bi_tables(workspace_id, power_bi_table_request)

List Power Bi Tables

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.microsoft_power_bi_tables_response import MicrosoftPowerBiTablesResponse
from flowhunt.models.power_bi_table_request import PowerBiTableRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    power_bi_table_request = flowhunt.PowerBiTableRequest() # PowerBiTableRequest | 

    try:
        # List Power Bi Tables
        api_response = api_instance.list_power_bi_tables(workspace_id, power_bi_table_request)
        print("The response of ObservabilityDriverApi->list_power_bi_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->list_power_bi_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **power_bi_table_request** | [**PowerBiTableRequest**](PowerBiTableRequest.md)|  | 

### Return type

[**MicrosoftPowerBiTablesResponse**](MicrosoftPowerBiTablesResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_power_bi_workspaces**
> MicrosoftPowerBiWorkspacesResponse list_power_bi_workspaces(workspace_id)

List Power Bi Workspaces

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.microsoft_power_bi_workspaces_response import MicrosoftPowerBiWorkspacesResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Power Bi Workspaces
        api_response = api_instance.list_power_bi_workspaces(workspace_id)
        print("The response of ObservabilityDriverApi->list_power_bi_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->list_power_bi_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**MicrosoftPowerBiWorkspacesResponse**](MicrosoftPowerBiWorkspacesResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_langfuse_observability_driver**
> ObservabilityDriverResponse update_langfuse_observability_driver(workspace_id, langfuse_request)

Update Langfuse Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.langfuse_request import LangfuseRequest
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    langfuse_request = flowhunt.LangfuseRequest() # LangfuseRequest | 

    try:
        # Update Langfuse Observability Driver
        api_response = api_instance.update_langfuse_observability_driver(workspace_id, langfuse_request)
        print("The response of ObservabilityDriverApi->update_langfuse_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->update_langfuse_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **langfuse_request** | [**LangfuseRequest**](LangfuseRequest.md)|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_bi_observability_driver**
> ObservabilityDriverResponse update_power_bi_observability_driver(workspace_id, power_bi_request)

Update Power Bi Observability Driver

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse
from flowhunt.models.power_bi_request import PowerBiRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    power_bi_request = flowhunt.PowerBiRequest() # PowerBiRequest | 

    try:
        # Update Power Bi Observability Driver
        api_response = api_instance.update_power_bi_observability_driver(workspace_id, power_bi_request)
        print("The response of ObservabilityDriverApi->update_power_bi_observability_driver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->update_power_bi_observability_driver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **power_bi_request** | [**PowerBiRequest**](PowerBiRequest.md)|  | 

### Return type

[**ObservabilityDriverResponse**](ObservabilityDriverResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_push_dataset_table**
> MicrosoftPowerBiTableValidateResponse validate_push_dataset_table(workspace_id, power_bi_request)

Validate Push Dataset Table

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.microsoft_power_bi_table_validate_response import MicrosoftPowerBiTableValidateResponse
from flowhunt.models.power_bi_request import PowerBiRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ObservabilityDriverApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    power_bi_request = flowhunt.PowerBiRequest() # PowerBiRequest | 

    try:
        # Validate Push Dataset Table
        api_response = api_instance.validate_push_dataset_table(workspace_id, power_bi_request)
        print("The response of ObservabilityDriverApi->validate_push_dataset_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityDriverApi->validate_push_dataset_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **power_bi_request** | [**PowerBiRequest**](PowerBiRequest.md)|  | 

### Return type

[**MicrosoftPowerBiTableValidateResponse**](MicrosoftPowerBiTableValidateResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

