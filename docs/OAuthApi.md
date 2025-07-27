# flowhunt.OAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_authorize**](OAuthApi.md#oauth_authorize) | **GET** /v2/auth/oauth/authorize | Oauth Authorize
[**oauth_authorize_post**](OAuthApi.md#oauth_authorize_post) | **POST** /v2/auth/oauth/authorize | Oauth Authorize Post
[**oauth_callback**](OAuthApi.md#oauth_callback) | **GET** /v2/auth/oauth/callback | Oauth Callback
[**oauth_login**](OAuthApi.md#oauth_login) | **GET** /v2/auth/oauth/login | Oauth Login
[**oauth_login_github**](OAuthApi.md#oauth_login_github) | **GET** /v2/auth/oauth/login/github | Oauth Login Github
[**oauth_login_google**](OAuthApi.md#oauth_login_google) | **GET** /v2/auth/oauth/login/google | Oauth Login Google
[**oauth_login_post**](OAuthApi.md#oauth_login_post) | **POST** /v2/auth/oauth/login | Oauth Login Post
[**oauth_login_shopify**](OAuthApi.md#oauth_login_shopify) | **GET** /v2/auth/oauth/login/shopify | Oauth Login Shopify
[**oauth_logout**](OAuthApi.md#oauth_logout) | **GET** /v2/auth/oauth/logout | Oauth Logout
[**oauth_revoke**](OAuthApi.md#oauth_revoke) | **POST** /v2/auth/oauth/revoke | Oauth Revoke
[**oauth_token**](OAuthApi.md#oauth_token) | **POST** /v2/auth/oauth/token | Oauth Token
[**oauth_userinfo**](OAuthApi.md#oauth_userinfo) | **GET** /v2/auth/oauth/userinfo | Oauth Userinfo
[**saml_callback**](OAuthApi.md#saml_callback) | **POST** /v2/auth/oauth/callback/saml/{random_id} | Saml Callback


# **oauth_authorize**
> object oauth_authorize()

Oauth Authorize

OAuth authorization endpoint

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Authorize
        api_response = api_instance.oauth_authorize()
        print("The response of OAuthApi->oauth_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_authorize: %s\n" % e)
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

# **oauth_authorize_post**
> object oauth_authorize_post()

Oauth Authorize Post

OAuth authorization endpoint (consent form submission)

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Authorize Post
        api_response = api_instance.oauth_authorize_post()
        print("The response of OAuthApi->oauth_authorize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_authorize_post: %s\n" % e)
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

# **oauth_callback**
> object oauth_callback()

Oauth Callback

OAuth callback endpoint for third-party providers

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Callback
        api_response = api_instance.oauth_callback()
        print("The response of OAuthApi->oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_callback: %s\n" % e)
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

# **oauth_login**
> object oauth_login()

Oauth Login

OAuth login page

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Login
        api_response = api_instance.oauth_login()
        print("The response of OAuthApi->oauth_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_login: %s\n" % e)
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

# **oauth_login_github**
> object oauth_login_github()

Oauth Login Github

OAuth login with GitHub

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Login Github
        api_response = api_instance.oauth_login_github()
        print("The response of OAuthApi->oauth_login_github:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_login_github: %s\n" % e)
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

# **oauth_login_google**
> object oauth_login_google()

Oauth Login Google

OAuth login with Google

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Login Google
        api_response = api_instance.oauth_login_google()
        print("The response of OAuthApi->oauth_login_google:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_login_google: %s\n" % e)
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

# **oauth_login_post**
> object oauth_login_post()

Oauth Login Post

OAuth login form submission

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Login Post
        api_response = api_instance.oauth_login_post()
        print("The response of OAuthApi->oauth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_login_post: %s\n" % e)
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

# **oauth_login_shopify**
> object oauth_login_shopify()

Oauth Login Shopify

OAuth login with Shopify for app installation

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Login Shopify
        api_response = api_instance.oauth_login_shopify()
        print("The response of OAuthApi->oauth_login_shopify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_login_shopify: %s\n" % e)
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

# **oauth_logout**
> object oauth_logout()

Oauth Logout

OAuth logout endpoint - revokes tokens, clears session and redirects to specified URL

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Logout
        api_response = api_instance.oauth_logout()
        print("The response of OAuthApi->oauth_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_logout: %s\n" % e)
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

# **oauth_revoke**
> object oauth_revoke()

Oauth Revoke

OAuth token revocation endpoint

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Revoke
        api_response = api_instance.oauth_revoke()
        print("The response of OAuthApi->oauth_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_revoke: %s\n" % e)
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

# **oauth_token**
> object oauth_token()

Oauth Token

OAuth token endpoint

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Token
        api_response = api_instance.oauth_token()
        print("The response of OAuthApi->oauth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_token: %s\n" % e)
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

# **oauth_userinfo**
> object oauth_userinfo()

Oauth Userinfo

OpenID Connect userinfo endpoint

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
    api_instance = flowhunt.OAuthApi(api_client)

    try:
        # Oauth Userinfo
        api_response = api_instance.oauth_userinfo()
        print("The response of OAuthApi->oauth_userinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->oauth_userinfo: %s\n" % e)
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

# **saml_callback**
> object saml_callback(random_id, workspace_id=workspace_id)

Saml Callback

SAML callback endpoint (Assertion Consumer Service)
Handles the SAML response from the Identity Provider after successful authentication

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
    api_instance = flowhunt.OAuthApi(api_client)
    random_id = 'random_id_example' # str | 
    workspace_id = 'workspace_id_example' # str |  (optional)

    try:
        # Saml Callback
        api_response = api_instance.saml_callback(random_id, workspace_id=workspace_id)
        print("The response of OAuthApi->saml_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->saml_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **random_id** | **str**|  | 
 **workspace_id** | **str**|  | [optional] 

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

