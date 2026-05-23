# flowhunt.MeApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_user_onboarding**](MeApi.md#complete_user_onboarding) | **PATCH** /v2/users/me/onboarding | Complete User Onboarding
[**get_user_onboarding**](MeApi.md#get_user_onboarding) | **GET** /v2/users/me/onboarding | Get User Onboarding


# **complete_user_onboarding**
> OnboardingStateResponse complete_user_onboarding(complete_onboarding_request)

Complete User Onboarding

Mark onboarding complete with the user's selected primary goal.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.complete_onboarding_request import CompleteOnboardingRequest
from flowhunt.models.onboarding_state_response import OnboardingStateResponse
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
    api_instance = flowhunt.MeApi(api_client)
    complete_onboarding_request = flowhunt.CompleteOnboardingRequest() # CompleteOnboardingRequest | 

    try:
        # Complete User Onboarding
        api_response = api_instance.complete_user_onboarding(complete_onboarding_request)
        print("The response of MeApi->complete_user_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->complete_user_onboarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complete_onboarding_request** | [**CompleteOnboardingRequest**](CompleteOnboardingRequest.md)|  | 

### Return type

[**OnboardingStateResponse**](OnboardingStateResponse.md)

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

# **get_user_onboarding**
> OnboardingStateResponse get_user_onboarding()

Get User Onboarding

Return the current user's onboarding state.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.onboarding_state_response import OnboardingStateResponse
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
    api_instance = flowhunt.MeApi(api_client)

    try:
        # Get User Onboarding
        api_response = api_instance.get_user_onboarding()
        print("The response of MeApi->get_user_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_user_onboarding: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnboardingStateResponse**](OnboardingStateResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

