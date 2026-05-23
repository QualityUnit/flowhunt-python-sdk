# flowhunt.GatewayApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_integration_gateway_token**](GatewayApi.md#resolve_integration_gateway_token) | **GET** /v2/integrations/integrate/gateway/{token} | Resolve an integration gateway token


# **resolve_integration_gateway_token**
> IntegrationGatewayResponse resolve_integration_gateway_token(token)

Resolve an integration gateway token

Resolves a temporary token issued by an AI agent when a required integration is missing.  Returns the workspace and slug so the frontend can redirect to the integration setup page.

### Example


```python
import flowhunt
from flowhunt.models.integration_gateway_response import IntegrationGatewayResponse
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.GatewayApi(api_client)
    token = 'token_example' # str | 

    try:
        # Resolve an integration gateway token
        api_response = api_instance.resolve_integration_gateway_token(token)
        print("The response of GatewayApi->resolve_integration_gateway_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewayApi->resolve_integration_gateway_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**IntegrationGatewayResponse**](IntegrationGatewayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

