# flowhunt.AirtableApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_airtable_bases**](AirtableApi.md#get_airtable_bases) | **GET** /v2/integrations/airtable/ | Get Airtable Bases
[**get_airtable_tables**](AirtableApi.md#get_airtable_tables) | **GET** /v2/integrations/airtable/bases/{base_id}/tables | Get Airtable Tables


# **get_airtable_bases**
> AirtableBasesResponse get_airtable_bases(workspace_id)

Get Airtable Bases

Get all Airtable bases accessible through the workspace's Airtable integration.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.airtable_bases_response import AirtableBasesResponse
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
    api_instance = flowhunt.AirtableApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Airtable Bases
        api_response = api_instance.get_airtable_bases(workspace_id)
        print("The response of AirtableApi->get_airtable_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirtableApi->get_airtable_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**AirtableBasesResponse**](AirtableBasesResponse.md)

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

# **get_airtable_tables**
> AirtableTablesResponse get_airtable_tables(base_id, workspace_id)

Get Airtable Tables

Get all tables for a specific Airtable base.

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.airtable_tables_response import AirtableTablesResponse
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
    api_instance = flowhunt.AirtableApi(api_client)
    base_id = 'base_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Airtable Tables
        api_response = api_instance.get_airtable_tables(base_id, workspace_id)
        print("The response of AirtableApi->get_airtable_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirtableApi->get_airtable_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**AirtableTablesResponse**](AirtableTablesResponse.md)

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

