# flowhunt.PhotoAIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explore**](PhotoAIApi.md#explore) | **GET** /v2/photo_ai/public/explore | Explore
[**get_effects**](PhotoAIApi.md#get_effects) | **GET** /v2/photo_ai/public/effects | Get Effects
[**get_styles**](PhotoAIApi.md#get_styles) | **GET** /v2/photo_ai/public/styles | Get Styles
[**get_templates**](PhotoAIApi.md#get_templates) | **GET** /v2/photo_ai/public/templates | Get Templates


# **explore**
> List[CommunityImageGenerationsResponse] explore()

Explore

### Example


```python
import flowhunt
from flowhunt.models.community_image_generations_response import CommunityImageGenerationsResponse
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
    api_instance = flowhunt.PhotoAIApi(api_client)

    try:
        # Explore
        api_response = api_instance.explore()
        print("The response of PhotoAIApi->explore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotoAIApi->explore: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CommunityImageGenerationsResponse]**](CommunityImageGenerationsResponse.md)

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

# **get_effects**
> List[PhotoAIEffectResponse] get_effects()

Get Effects

### Example


```python
import flowhunt
from flowhunt.models.photo_ai_effect_response import PhotoAIEffectResponse
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
    api_instance = flowhunt.PhotoAIApi(api_client)

    try:
        # Get Effects
        api_response = api_instance.get_effects()
        print("The response of PhotoAIApi->get_effects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotoAIApi->get_effects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PhotoAIEffectResponse]**](PhotoAIEffectResponse.md)

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

# **get_styles**
> List[PhotoAIStyleResponse] get_styles()

Get Styles

### Example


```python
import flowhunt
from flowhunt.models.photo_ai_style_response import PhotoAIStyleResponse
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
    api_instance = flowhunt.PhotoAIApi(api_client)

    try:
        # Get Styles
        api_response = api_instance.get_styles()
        print("The response of PhotoAIApi->get_styles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotoAIApi->get_styles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PhotoAIStyleResponse]**](PhotoAIStyleResponse.md)

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

# **get_templates**
> List[PhotoAITemplateResponse] get_templates()

Get Templates

### Example


```python
import flowhunt
from flowhunt.models.photo_ai_template_response import PhotoAITemplateResponse
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
    api_instance = flowhunt.PhotoAIApi(api_client)

    try:
        # Get Templates
        api_response = api_instance.get_templates()
        print("The response of PhotoAIApi->get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotoAIApi->get_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PhotoAITemplateResponse]**](PhotoAITemplateResponse.md)

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

