# flowhunt.ZendeskApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_zendesk_kb_categories**](ZendeskApi.md#list_zendesk_kb_categories) | **GET** /v2/integrations/zendesk/kb/categories | List Zendesk Kb Categories
[**list_zendesk_kb_labels**](ZendeskApi.md#list_zendesk_kb_labels) | **GET** /v2/integrations/zendesk/kb/labels | List Zendesk Kb Labels
[**list_zendesk_kb_sections**](ZendeskApi.md#list_zendesk_kb_sections) | **GET** /v2/integrations/zendesk/kb/sections | List Zendesk Kb Sections


# **list_zendesk_kb_categories**
> List[ZendeskKBCategoryResponse] list_zendesk_kb_categories(workspace_id, locale=locale)

List Zendesk Kb Categories

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.zendesk_kb_category_response import ZendeskKBCategoryResponse
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
    api_instance = flowhunt.ZendeskApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    locale = 'locale_example' # str | Locale filter (e.g. en-us) (optional)

    try:
        # List Zendesk Kb Categories
        api_response = api_instance.list_zendesk_kb_categories(workspace_id, locale=locale)
        print("The response of ZendeskApi->list_zendesk_kb_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskApi->list_zendesk_kb_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **locale** | **str**| Locale filter (e.g. en-us) | [optional] 

### Return type

[**List[ZendeskKBCategoryResponse]**](ZendeskKBCategoryResponse.md)

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

# **list_zendesk_kb_labels**
> List[ZendeskKBLabelResponse] list_zendesk_kb_labels(workspace_id)

List Zendesk Kb Labels

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.zendesk_kb_label_response import ZendeskKBLabelResponse
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
    api_instance = flowhunt.ZendeskApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Zendesk Kb Labels
        api_response = api_instance.list_zendesk_kb_labels(workspace_id)
        print("The response of ZendeskApi->list_zendesk_kb_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskApi->list_zendesk_kb_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[ZendeskKBLabelResponse]**](ZendeskKBLabelResponse.md)

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

# **list_zendesk_kb_sections**
> List[ZendeskKBSectionResponse] list_zendesk_kb_sections(workspace_id, category_id=category_id)

List Zendesk Kb Sections

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.zendesk_kb_section_response import ZendeskKBSectionResponse
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
    api_instance = flowhunt.ZendeskApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    category_id = 56 # int | Category ID to filter sections (optional)

    try:
        # List Zendesk Kb Sections
        api_response = api_instance.list_zendesk_kb_sections(workspace_id, category_id=category_id)
        print("The response of ZendeskApi->list_zendesk_kb_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskApi->list_zendesk_kb_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **category_id** | **int**| Category ID to filter sections | [optional] 

### Return type

[**List[ZendeskKBSectionResponse]**](ZendeskKBSectionResponse.md)

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

