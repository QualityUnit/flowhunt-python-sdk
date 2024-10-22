# flowhunt-python-sdk.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](AuthApi.md#activate_user) | **GET** /v2/auth/activate | Activate User
[**get_third_party_token**](AuthApi.md#get_third_party_token) | **POST** /v2/auth/token/{provider_name} | Get Third Party Token
[**get_token**](AuthApi.md#get_token) | **POST** /v2/auth/token | Get Token
[**get_user**](AuthApi.md#get_user) | **GET** /v2/auth/me | Get User
[**recover_password**](AuthApi.md#recover_password) | **POST** /v2/auth/password-recovery/{email} | Recover Password
[**refresh_token**](AuthApi.md#refresh_token) | **POST** /v2/auth/refresh-token | Refresh Token
[**register_user**](AuthApi.md#register_user) | **POST** /v2/auth/ | Register User
[**reset_password**](AuthApi.md#reset_password) | **POST** /v2/auth/reset-password | Reset Password


# **activate_user**
> object activate_user(token)

Activate User

Activate User :param token: :param auth_controller: :return:

### Example


```python
import flowhunt-python-sdk
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # Activate User
        api_response = api_instance.activate_user(token)
        print("The response of AuthApi->activate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->activate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**object**

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

# **get_third_party_token**
> UserTokenResponse get_third_party_token(provider_name, thrid_party_login_request)

Get Third Party Token

### Example

* Api Key Authentication (sudo_api_key_header):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.thrid_party_login_request import ThridPartyLoginRequest
from flowhunt-python-sdk.models.user_token_response import UserTokenResponse
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sudo_api_key_header
configuration.api_key['sudo_api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo_api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    provider_name = 'provider_name_example' # str | 
    thrid_party_login_request = flowhunt-python-sdk.ThridPartyLoginRequest() # ThridPartyLoginRequest | 

    try:
        # Get Third Party Token
        api_response = api_instance.get_third_party_token(provider_name, thrid_party_login_request)
        print("The response of AuthApi->get_third_party_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_third_party_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | 
 **thrid_party_login_request** | [**ThridPartyLoginRequest**](ThridPartyLoginRequest.md)|  | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[sudo_api_key_header](../README.md#sudo_api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> UserTokenResponse get_token(login_user_request)

Get Token

### Example

* Api Key Authentication (sudo_api_key_header):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.login_user_request import LoginUserRequest
from flowhunt-python-sdk.models.user_token_response import UserTokenResponse
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sudo_api_key_header
configuration.api_key['sudo_api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo_api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    login_user_request = flowhunt-python-sdk.LoginUserRequest() # LoginUserRequest | 

    try:
        # Get Token
        api_response = api_instance.get_token(login_user_request)
        print("The response of AuthApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_user_request** | [**LoginUserRequest**](LoginUserRequest.md)|  | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[sudo_api_key_header](../README.md#sudo_api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user()

Get User

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.user_response import UserResponse
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
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
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)

    try:
        # Get User
        api_response = api_instance.get_user()
        print("The response of AuthApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

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

# **recover_password**
> Completed recover_password(email)

Recover Password

Password Recovery

### Example


```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.completed import Completed
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    email = 'email_example' # str | 

    try:
        # Recover Password
        api_response = api_instance.recover_password(email)
        print("The response of AuthApi->recover_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->recover_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **refresh_token**
> Token refresh_token(refresh_token_request)

Refresh Token

### Example


```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.refresh_token_request import RefreshTokenRequest
from flowhunt-python-sdk.models.token import Token
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    refresh_token_request = flowhunt-python-sdk.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh Token
        api_response = api_instance.refresh_token(refresh_token_request)
        print("The response of AuthApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> Completed register_user(register_user_request)

Register User

### Example


```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.completed import Completed
from flowhunt-python-sdk.models.register_user_request import RegisterUserRequest
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    register_user_request = flowhunt-python-sdk.RegisterUserRequest() # RegisterUserRequest | 

    try:
        # Register User
        api_response = api_instance.register_user(register_user_request)
        print("The response of AuthApi->register_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_request** | [**RegisterUserRequest**](RegisterUserRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> Completed reset_password(new_password_request)

Reset Password

Reset Password :param auth_controller: :param new_password: :return:

### Example


```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.completed import Completed
from flowhunt-python-sdk.models.new_password_request import NewPasswordRequest
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.AuthApi(api_client)
    new_password_request = flowhunt-python-sdk.NewPasswordRequest() # NewPasswordRequest | 

    try:
        # Reset Password
        api_response = api_instance.reset_password(new_password_request)
        print("The response of AuthApi->reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_password_request** | [**NewPasswordRequest**](NewPasswordRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

