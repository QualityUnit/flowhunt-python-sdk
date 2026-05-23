# flowhunt.AIProjectsLibraryApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_projects_template**](AIProjectsLibraryApi.md#get_ai_projects_template) | **GET** /v2/ai_projects_library/templates/{template_id} | Get Ai Projects Template
[**list_ai_projects_templates**](AIProjectsLibraryApi.md#list_ai_projects_templates) | **GET** /v2/ai_projects_library/templates | List Ai Projects Templates


# **get_ai_projects_template**
> AIProjectTemplateDetailResponse get_ai_projects_template(template_id, workspace_id)

Get Ai Projects Template

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.ai_project_template_detail_response import AIProjectTemplateDetailResponse
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
    api_instance = flowhunt.AIProjectsLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Ai Projects Template
        api_response = api_instance.get_ai_projects_template(template_id, workspace_id)
        print("The response of AIProjectsLibraryApi->get_ai_projects_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIProjectsLibraryApi->get_ai_projects_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**AIProjectTemplateDetailResponse**](AIProjectTemplateDetailResponse.md)

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

# **list_ai_projects_templates**
> List[AIProjectTemplateCardResponse] list_ai_projects_templates(workspace_id)

List Ai Projects Templates

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.ai_project_template_card_response import AIProjectTemplateCardResponse
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
    api_instance = flowhunt.AIProjectsLibraryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Ai Projects Templates
        api_response = api_instance.list_ai_projects_templates(workspace_id)
        print("The response of AIProjectsLibraryApi->list_ai_projects_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIProjectsLibraryApi->list_ai_projects_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[AIProjectTemplateCardResponse]**](AIProjectTemplateCardResponse.md)

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

