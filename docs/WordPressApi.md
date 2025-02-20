# flowhunt.WordPressApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wordpress_post_categories_0**](WordPressApi.md#get_wordpress_post_categories_0) | **GET** /v2/integrations/wordpress/{integration_id}/categories | Get Wordpress Post Categories
[**get_wordpress_post_tags_0**](WordPressApi.md#get_wordpress_post_tags_0) | **GET** /v2/integrations/wordpress/{integration_id}/tags | Get Wordpress Post Tags
[**get_wordpress_sites_0**](WordPressApi.md#get_wordpress_sites_0) | **GET** /v2/integrations/wordpress/sites | Get Wordpress Sites


# **get_wordpress_post_categories_0**
> List[WordPressCategoryResponse] get_wordpress_post_categories_0(integration_id, workspace_id)

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
    api_instance = flowhunt.WordPressApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Post Categories
        api_response = api_instance.get_wordpress_post_categories_0(integration_id, workspace_id)
        print("The response of WordPressApi->get_wordpress_post_categories_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressApi->get_wordpress_post_categories_0: %s\n" % e)
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

# **get_wordpress_post_tags_0**
> List[WordPressTagsResponse] get_wordpress_post_tags_0(integration_id, workspace_id)

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
    api_instance = flowhunt.WordPressApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Post Tags
        api_response = api_instance.get_wordpress_post_tags_0(integration_id, workspace_id)
        print("The response of WordPressApi->get_wordpress_post_tags_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressApi->get_wordpress_post_tags_0: %s\n" % e)
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

# **get_wordpress_sites_0**
> List[WordPressSiteResponse] get_wordpress_sites_0(workspace_id)

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
    api_instance = flowhunt.WordPressApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Sites
        api_response = api_instance.get_wordpress_sites_0(workspace_id)
        print("The response of WordPressApi->get_wordpress_sites_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressApi->get_wordpress_sites_0: %s\n" % e)
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

