# flowhunt.MicrosoftOutlookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_admin_consent**](MicrosoftOutlookApi.md#update_admin_consent) | **POST** /v2/integrations/microsoft_entra_id/admin_consent | Update Admin Consent


# **update_admin_consent**
> IntegrationDetailResponse update_admin_consent(workspace_id, integration_id)

Update Admin Consent

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_detail_response import IntegrationDetailResponse
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
    api_instance = flowhunt.MicrosoftOutlookApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    integration_id = 'integration_id_example' # str | 

    try:
        # Update Admin Consent
        api_response = api_instance.update_admin_consent(workspace_id, integration_id)
        print("The response of MicrosoftOutlookApi->update_admin_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrosoftOutlookApi->update_admin_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **integration_id** | **str**|  | 

### Return type

[**IntegrationDetailResponse**](IntegrationDetailResponse.md)

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

