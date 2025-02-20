# flowhunt.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration**](IntegrationsApi.md#create_integration) | **POST** /v2/integrations/{slug}/integrate | Create Integration
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /v2/integrations/{slug}/{integration_id} | Delete Integration
[**get_all_integrations**](IntegrationsApi.md#get_all_integrations) | **GET** /v2/integrations/all | Get All Integrations
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /v2/integrations/{slug}/{integration_id} | Get Integration
[**get_picker_token**](IntegrationsApi.md#get_picker_token) | **GET** /v2/integrations/google/picker_token | Get Picker Token
[**get_slack_channels**](IntegrationsApi.md#get_slack_channels) | **GET** /v2/integrations/slack/{slack_team_id}/channels | Get Slack Channels
[**get_slack_workspaces**](IntegrationsApi.md#get_slack_workspaces) | **GET** /v2/integrations/slack/ | Get Slack Workspaces
[**get_wordpress_post_categories**](IntegrationsApi.md#get_wordpress_post_categories) | **GET** /v2/integrations/wordpress/{integration_id}/categories | Get Wordpress Post Categories
[**get_wordpress_post_tags**](IntegrationsApi.md#get_wordpress_post_tags) | **GET** /v2/integrations/wordpress/{integration_id}/tags | Get Wordpress Post Tags
[**get_wordpress_sites**](IntegrationsApi.md#get_wordpress_sites) | **GET** /v2/integrations/wordpress/sites | Get Wordpress Sites
[**integration_callback**](IntegrationsApi.md#integration_callback) | **GET** /v2/integrations/{slug}/callback | Integration Callback
[**search_integrations**](IntegrationsApi.md#search_integrations) | **POST** /v2/integrations/{slug} | Search Integrations


# **create_integration**
> IntegrationFlowResponse create_integration(slug, workspace_id)

Create Integration

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_flow_response import IntegrationFlowResponse
from flowhunt.models.integration_slug import IntegrationSlug
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Create Integration
        api_response = api_instance.create_integration(slug, workspace_id)
        print("The response of IntegrationsApi->create_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **workspace_id** | **str**|  | 

### Return type

[**IntegrationFlowResponse**](IntegrationFlowResponse.md)

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

# **delete_integration**
> Completed delete_integration(slug, integration_id, workspace_id)

Delete Integration

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.integration_slug import IntegrationSlug
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Integration
        api_response = api_instance.delete_integration(slug, integration_id, workspace_id)
        print("The response of IntegrationsApi->delete_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->delete_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **get_all_integrations**
> List[IntegrationResponse] get_all_integrations(workspace_id)

Get All Integrations

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_response import IntegrationResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get All Integrations
        api_response = api_instance.get_all_integrations(workspace_id)
        print("The response of IntegrationsApi->get_all_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_all_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[IntegrationResponse]**](IntegrationResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> IntegrationDetailResponse get_integration(slug, integration_id, workspace_id)

Get Integration

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_detail_response import IntegrationDetailResponse
from flowhunt.models.integration_slug import IntegrationSlug
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Integration
        api_response = api_instance.get_integration(slug, integration_id, workspace_id)
        print("The response of IntegrationsApi->get_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Picker Token
        api_response = api_instance.get_picker_token(workspace_id)
        print("The response of IntegrationsApi->get_picker_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_picker_token: %s\n" % e)
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

# **get_slack_channels**
> List[SlackChannelResponse] get_slack_channels(slack_team_id, workspace_id)

Get Slack Channels

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.slack_channel_response import SlackChannelResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slack_team_id = 'slack_team_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Slack Channels
        api_response = api_instance.get_slack_channels(slack_team_id, workspace_id)
        print("The response of IntegrationsApi->get_slack_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_slack_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slack_team_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[SlackChannelResponse]**](SlackChannelResponse.md)

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

# **get_slack_workspaces**
> List[SlackWorkspaceResponse] get_slack_workspaces(workspace_id)

Get Slack Workspaces

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.slack_workspace_response import SlackWorkspaceResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Slack Workspaces
        api_response = api_instance.get_slack_workspaces(workspace_id)
        print("The response of IntegrationsApi->get_slack_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_slack_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[SlackWorkspaceResponse]**](SlackWorkspaceResponse.md)

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

# **get_wordpress_post_categories**
> List[WordPressCategoryResponse] get_wordpress_post_categories(integration_id, workspace_id)

Get Wordpress Post Categories

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.word_press_category_response import WordPressCategoryResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Post Categories
        api_response = api_instance.get_wordpress_post_categories(integration_id, workspace_id)
        print("The response of IntegrationsApi->get_wordpress_post_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_wordpress_post_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[WordPressCategoryResponse]**](WordPressCategoryResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wordpress_post_tags**
> List[WordPressTagsResponse] get_wordpress_post_tags(integration_id, workspace_id)

Get Wordpress Post Tags

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.word_press_tags_response import WordPressTagsResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Post Tags
        api_response = api_instance.get_wordpress_post_tags(integration_id, workspace_id)
        print("The response of IntegrationsApi->get_wordpress_post_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_wordpress_post_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[WordPressTagsResponse]**](WordPressTagsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wordpress_sites**
> List[WordPressSiteResponse] get_wordpress_sites(workspace_id)

Get Wordpress Sites

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.word_press_site_response import WordPressSiteResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Sites
        api_response = api_instance.get_wordpress_sites(workspace_id)
        print("The response of IntegrationsApi->get_wordpress_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_wordpress_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[WordPressSiteResponse]**](WordPressSiteResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_callback**
> object integration_callback(slug)

Integration Callback

### Example


```python
import flowhunt
from flowhunt.models.integration_slug import IntegrationSlug
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 

    try:
        # Integration Callback
        api_response = api_instance.integration_callback(slug)
        print("The response of IntegrationsApi->integration_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->integration_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 

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

# **search_integrations**
> List[IntegrationDetailResponse] search_integrations(slug, workspace_id, integration_search_request)

Search Integrations

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_detail_response import IntegrationDetailResponse
from flowhunt.models.integration_search_request import IntegrationSearchRequest
from flowhunt.models.integration_slug import IntegrationSlug
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    workspace_id = 'workspace_id_example' # str | 
    integration_search_request = flowhunt.IntegrationSearchRequest() # IntegrationSearchRequest | 

    try:
        # Search Integrations
        api_response = api_instance.search_integrations(slug, workspace_id, integration_search_request)
        print("The response of IntegrationsApi->search_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->search_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **workspace_id** | **str**|  | 
 **integration_search_request** | [**IntegrationSearchRequest**](IntegrationSearchRequest.md)|  | 

### Return type

[**List[IntegrationDetailResponse]**](IntegrationDetailResponse.md)

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

