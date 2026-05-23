# flowhunt.AIStudioLibraryApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_studio_template**](AIStudioLibraryApi.md#get_ai_studio_template) | **GET** /v2/ai_studio_library/templates/{template_id} | Get Ai Studio Template
[**list_ai_studio_templates**](AIStudioLibraryApi.md#list_ai_studio_templates) | **GET** /v2/ai_studio_library/templates | List Ai Studio Templates


# **get_ai_studio_template**
> AIStudioFlowTemplateResponse get_ai_studio_template(template_id, workspace_id)

Get Ai Studio Template

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.ai_studio_flow_template_response import AIStudioFlowTemplateResponse
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
    api_instance = flowhunt.AIStudioLibraryApi(api_client)
    template_id = 'template_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Ai Studio Template
        api_response = api_instance.get_ai_studio_template(template_id, workspace_id)
        print("The response of AIStudioLibraryApi->get_ai_studio_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIStudioLibraryApi->get_ai_studio_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**AIStudioFlowTemplateResponse**](AIStudioFlowTemplateResponse.md)

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

# **list_ai_studio_templates**
> List[AIStudioFlowTemplateResponse] list_ai_studio_templates(workspace_id)

List Ai Studio Templates

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.ai_studio_flow_template_response import AIStudioFlowTemplateResponse
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
    api_instance = flowhunt.AIStudioLibraryApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Ai Studio Templates
        api_response = api_instance.list_ai_studio_templates(workspace_id)
        print("The response of AIStudioLibraryApi->list_ai_studio_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIStudioLibraryApi->list_ai_studio_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[AIStudioFlowTemplateResponse]**](AIStudioFlowTemplateResponse.md)

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

