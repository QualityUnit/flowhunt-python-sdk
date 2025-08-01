# flowhunt.GoogleApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calendars**](GoogleApi.md#get_calendars) | **GET** /v2/integrations/google/calendar | Get Calendars
[**get_picker_token**](GoogleApi.md#get_picker_token) | **GET** /v2/integrations/google/picker_token | Get Picker Token
[**get_sheets**](GoogleApi.md#get_sheets) | **GET** /v2/integrations/google/sheets/{document_id} | Get Sheets


# **get_calendars**
> GoogleCalendarsResponse get_calendars(workspace_id)

Get Calendars

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_calendars_response import GoogleCalendarsResponse
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
    api_instance = flowhunt.GoogleApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Calendars
        api_response = api_instance.get_calendars(workspace_id)
        print("The response of GoogleApi->get_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->get_calendars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GoogleCalendarsResponse**](GoogleCalendarsResponse.md)

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

# **get_picker_token**
> GooglePickerTokenResponse get_picker_token(workspace_id)

Get Picker Token

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_picker_token_response import GooglePickerTokenResponse
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
    api_instance = flowhunt.GoogleApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Picker Token
        api_response = api_instance.get_picker_token(workspace_id)
        print("The response of GoogleApi->get_picker_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->get_picker_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GooglePickerTokenResponse**](GooglePickerTokenResponse.md)

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

# **get_sheets**
> GoogleSheetsResponse get_sheets(document_id, workspace_id)

Get Sheets

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_sheets_response import GoogleSheetsResponse
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
    api_instance = flowhunt.GoogleApi(api_client)
    document_id = 'document_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Sheets
        api_response = api_instance.get_sheets(document_id, workspace_id)
        print("The response of GoogleApi->get_sheets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->get_sheets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleSheetsResponse**](GoogleSheetsResponse.md)

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

