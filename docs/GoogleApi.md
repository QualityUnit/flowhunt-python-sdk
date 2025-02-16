# flowhunt.GoogleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_picker_token_0**](GoogleApi.md#get_picker_token_0) | **GET** /v2/integrations/google/picker_token | Get Picker Token


# **get_picker_token_0**
> GooglePickerTokenResponse get_picker_token_0(workspace_id)

Get Picker Token

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_picker_token_response import GooglePickerTokenResponse
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
        api_response = api_instance.get_picker_token_0(workspace_id)
        print("The response of GoogleApi->get_picker_token_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->get_picker_token_0: %s\n" % e)
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

