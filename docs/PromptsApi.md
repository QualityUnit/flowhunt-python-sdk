# flowhunt-python-sdk.PromptsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_prompt**](PromptsApi.md#create_prompt) | **POST** /v2/prompts/create | Create Prompt
[**create_prompt_category**](PromptsApi.md#create_prompt_category) | **POST** /v2/prompts/categories/create | Create Prompt Category
[**delete_prompt**](PromptsApi.md#delete_prompt) | **DELETE** /v2/prompts/{prompt_id} | Delete Prompt
[**delete_prompt_category**](PromptsApi.md#delete_prompt_category) | **DELETE** /v2/prompts/categories/{cat_id} | Delete Prompt Category
[**search_prompt_categories**](PromptsApi.md#search_prompt_categories) | **POST** /v2/prompts/categories/search | Search Prompt Categories
[**search_prompts**](PromptsApi.md#search_prompts) | **POST** /v2/prompts/search | Search Prompts
[**update_prompt**](PromptsApi.md#update_prompt) | **PUT** /v2/prompts/{prompt_id} | Update Prompt
[**update_prompt_category**](PromptsApi.md#update_prompt_category) | **PUT** /v2/prompts/categories/{cat_id} | Update Prompt Category


# **create_prompt**
> PromptResponse create_prompt(workspace_id, prompt_create_request)

Create Prompt

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.prompt_create_request import PromptCreateRequest
from flowhunt-python-sdk.models.prompt_response import PromptResponse
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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    prompt_create_request = flowhunt-python-sdk.PromptCreateRequest() # PromptCreateRequest | 

    try:
        # Create Prompt
        api_response = api_instance.create_prompt(workspace_id, prompt_create_request)
        print("The response of PromptsApi->create_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->create_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **prompt_create_request** | [**PromptCreateRequest**](PromptCreateRequest.md)|  | 

### Return type

[**PromptResponse**](PromptResponse.md)

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

# **create_prompt_category**
> PromptCategoryResponse create_prompt_category(workspace_id, prompt_category_create_request)

Create Prompt Category

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.prompt_category_create_request import PromptCategoryCreateRequest
from flowhunt-python-sdk.models.prompt_category_response import PromptCategoryResponse
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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    prompt_category_create_request = flowhunt-python-sdk.PromptCategoryCreateRequest() # PromptCategoryCreateRequest | 

    try:
        # Create Prompt Category
        api_response = api_instance.create_prompt_category(workspace_id, prompt_category_create_request)
        print("The response of PromptsApi->create_prompt_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->create_prompt_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **prompt_category_create_request** | [**PromptCategoryCreateRequest**](PromptCategoryCreateRequest.md)|  | 

### Return type

[**PromptCategoryResponse**](PromptCategoryResponse.md)

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

# **delete_prompt**
> Completed delete_prompt(prompt_id, workspace_id)

Delete Prompt

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Prompt
        api_response = api_instance.delete_prompt(prompt_id, workspace_id)
        print("The response of PromptsApi->delete_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->delete_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **delete_prompt_category**
> Completed delete_prompt_category(cat_id, workspace_id)

Delete Prompt Category

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    cat_id = 'cat_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Prompt Category
        api_response = api_instance.delete_prompt_category(cat_id, workspace_id)
        print("The response of PromptsApi->delete_prompt_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->delete_prompt_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **search_prompt_categories**
> List[PromptCategoryResponse] search_prompt_categories(workspace_id, prompt_category_search_request)

Search Prompt Categories

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.prompt_category_response import PromptCategoryResponse
from flowhunt-python-sdk.models.prompt_category_search_request import PromptCategorySearchRequest
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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    prompt_category_search_request = flowhunt-python-sdk.PromptCategorySearchRequest() # PromptCategorySearchRequest | 

    try:
        # Search Prompt Categories
        api_response = api_instance.search_prompt_categories(workspace_id, prompt_category_search_request)
        print("The response of PromptsApi->search_prompt_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->search_prompt_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **prompt_category_search_request** | [**PromptCategorySearchRequest**](PromptCategorySearchRequest.md)|  | 

### Return type

[**List[PromptCategoryResponse]**](PromptCategoryResponse.md)

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

# **search_prompts**
> List[PromptResponse] search_prompts(workspace_id, prompt_search_request)

Search Prompts

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.prompt_response import PromptResponse
from flowhunt-python-sdk.models.prompt_search_request import PromptSearchRequest
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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    prompt_search_request = flowhunt-python-sdk.PromptSearchRequest() # PromptSearchRequest | 

    try:
        # Search Prompts
        api_response = api_instance.search_prompts(workspace_id, prompt_search_request)
        print("The response of PromptsApi->search_prompts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->search_prompts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **prompt_search_request** | [**PromptSearchRequest**](PromptSearchRequest.md)|  | 

### Return type

[**List[PromptResponse]**](PromptResponse.md)

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

# **update_prompt**
> PromptResponse update_prompt(prompt_id, workspace_id, prompt_update_request)

Update Prompt

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.prompt_response import PromptResponse
from flowhunt-python-sdk.models.prompt_update_request import PromptUpdateRequest
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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    prompt_update_request = flowhunt-python-sdk.PromptUpdateRequest() # PromptUpdateRequest | 

    try:
        # Update Prompt
        api_response = api_instance.update_prompt(prompt_id, workspace_id, prompt_update_request)
        print("The response of PromptsApi->update_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->update_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **prompt_update_request** | [**PromptUpdateRequest**](PromptUpdateRequest.md)|  | 

### Return type

[**PromptResponse**](PromptResponse.md)

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

# **update_prompt_category**
> PromptCategoryResponse update_prompt_category(cat_id, workspace_id, prompt_category_update_request)

Update Prompt Category

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.prompt_category_response import PromptCategoryResponse
from flowhunt-python-sdk.models.prompt_category_update_request import PromptCategoryUpdateRequest
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
    api_instance = flowhunt-python-sdk.PromptsApi(api_client)
    cat_id = 'cat_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    prompt_category_update_request = flowhunt-python-sdk.PromptCategoryUpdateRequest() # PromptCategoryUpdateRequest | 

    try:
        # Update Prompt Category
        api_response = api_instance.update_prompt_category(cat_id, workspace_id, prompt_category_update_request)
        print("The response of PromptsApi->update_prompt_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->update_prompt_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cat_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **prompt_category_update_request** | [**PromptCategoryUpdateRequest**](PromptCategoryUpdateRequest.md)|  | 

### Return type

[**PromptCategoryResponse**](PromptCategoryResponse.md)

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

