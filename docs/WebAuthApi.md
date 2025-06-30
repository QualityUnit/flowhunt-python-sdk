# flowhunt.WebAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_account**](WebAuthApi.md#activate_account) | **GET** /v2/auth/activate | Activate Account
[**get_user**](WebAuthApi.md#get_user) | **GET** /v2/auth/me | Get User
[**password_recovery_page**](WebAuthApi.md#password_recovery_page) | **GET** /v2/auth/recover-password | Password Recovery Page
[**password_recovery_submit**](WebAuthApi.md#password_recovery_submit) | **POST** /v2/auth/recover-password | Password Recovery Submit
[**register_page**](WebAuthApi.md#register_page) | **GET** /v2/auth/register | Register Page
[**register_submit**](WebAuthApi.md#register_submit) | **POST** /v2/auth/register | Register Submit
[**reset_password_page**](WebAuthApi.md#reset_password_page) | **GET** /v2/auth/reset-password | Reset Password Page
[**reset_password_submit**](WebAuthApi.md#reset_password_submit) | **POST** /v2/auth/reset-password | Reset Password Submit


# **activate_account**
> object activate_account(token)

Activate Account

Activate user account

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # Activate Account
        api_response = api_instance.activate_account(token)
        print("The response of WebAuthApi->activate_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->activate_account: %s\n" % e)
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

# **get_user**
> UserResponse get_user()

Get User

Get current authenticated user details.

This endpoint returns the current user's details including their product plans and API key workspace information.
It follows DDD principles by delegating the business logic to the application service layer.

Args:
    user: The current authenticated user (injected by dependency)
    request: The HTTP request object
    user_service: The user application service (injected by dependency)

Returns:
    UserResponse: The user details response

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.user_response import UserResponse
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
    api_instance = flowhunt.WebAuthApi(api_client)

    try:
        # Get User
        api_response = api_instance.get_user()
        print("The response of WebAuthApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->get_user: %s\n" % e)
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

# **password_recovery_page**
> object password_recovery_page()

Password Recovery Page

Password recovery page

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)

    try:
        # Password Recovery Page
        api_response = api_instance.password_recovery_page()
        print("The response of WebAuthApi->password_recovery_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->password_recovery_page: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_recovery_submit**
> object password_recovery_submit(email)

Password Recovery Submit

Handle password recovery form submission

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)
    email = 'email_example' # str | 

    try:
        # Password Recovery Submit
        api_response = api_instance.password_recovery_submit(email)
        print("The response of WebAuthApi->password_recovery_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->password_recovery_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_page**
> object register_page(next=next)

Register Page

Registration page

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)
    next = 'next_example' # str |  (optional)

    try:
        # Register Page
        api_response = api_instance.register_page(next=next)
        print("The response of WebAuthApi->register_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->register_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next** | **str**|  | [optional] 

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

# **register_submit**
> object register_submit(name, email, password, next=next)

Register Submit

Handle registration form submission

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)
    name = 'name_example' # str | 
    email = 'email_example' # str | 
    password = 'password_example' # str | 
    next = '/' # str |  (optional) (default to '/')

    try:
        # Register Submit
        api_response = api_instance.register_submit(name, email, password, next=next)
        print("The response of WebAuthApi->register_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->register_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **email** | **str**|  | 
 **password** | **str**|  | 
 **next** | **str**|  | [optional] [default to &#39;/&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_page**
> object reset_password_page(token)

Reset Password Page

Reset password page

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # Reset Password Page
        api_response = api_instance.reset_password_page(token)
        print("The response of WebAuthApi->reset_password_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->reset_password_page: %s\n" % e)
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

# **reset_password_submit**
> object reset_password_submit(token, password, confirm_password)

Reset Password Submit

Handle reset password form submission

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.WebAuthApi(api_client)
    token = 'token_example' # str | 
    password = 'password_example' # str | 
    confirm_password = 'confirm_password_example' # str | 

    try:
        # Reset Password Submit
        api_response = api_instance.reset_password_submit(token, password, confirm_password)
        print("The response of WebAuthApi->reset_password_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthApi->reset_password_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **password** | **str**|  | 
 **confirm_password** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

