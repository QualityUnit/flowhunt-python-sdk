# flowhunt-python-sdk.MediaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transcript**](MediaApi.md#get_transcript) | **POST** /v2/media/transcript | Get Transcript
[**get_transcript_result**](MediaApi.md#get_transcript_result) | **POST** /v2/media/transcript_status | Get Transcript Result
[**get_youtube_transcript**](MediaApi.md#get_youtube_transcript) | **POST** /v2/media/youtube/transcript | Get Youtube Transcript


# **get_transcript**
> DocumentContentResponse get_transcript(workspace_id, file, postback_url=postback_url)

Get Transcript

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.document_content_response import DocumentContentResponse
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
    api_instance = flowhunt-python-sdk.MediaApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    file = None # bytearray | 
    postback_url = 'postback_url_example' # str | The post back URL where to send the response in body (optional)

    try:
        # Get Transcript
        api_response = api_instance.get_transcript(workspace_id, file, postback_url=postback_url)
        print("The response of MediaApi->get_transcript:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_transcript: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **file** | **bytearray**|  | 
 **postback_url** | **str**| The post back URL where to send the response in body | [optional] 

### Return type

[**DocumentContentResponse**](DocumentContentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcript_result**
> DocumentContentResponse get_transcript_result(workspace_id, transcript_task_request)

Get Transcript Result

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.document_content_response import DocumentContentResponse
from flowhunt-python-sdk.models.transcript_task_request import TranscriptTaskRequest
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
    api_instance = flowhunt-python-sdk.MediaApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    transcript_task_request = flowhunt-python-sdk.TranscriptTaskRequest() # TranscriptTaskRequest | 

    try:
        # Get Transcript Result
        api_response = api_instance.get_transcript_result(workspace_id, transcript_task_request)
        print("The response of MediaApi->get_transcript_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_transcript_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **transcript_task_request** | [**TranscriptTaskRequest**](TranscriptTaskRequest.md)|  | 

### Return type

[**DocumentContentResponse**](DocumentContentResponse.md)

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

# **get_youtube_transcript**
> YoutubeTranscriptResponse get_youtube_transcript(workspace_id, youtube_transcript_request)

Get Youtube Transcript

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt-python-sdk
from flowhunt-python-sdk.models.youtube_transcript_request import YoutubeTranscriptRequest
from flowhunt-python-sdk.models.youtube_transcript_response import YoutubeTranscriptResponse
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
    api_instance = flowhunt-python-sdk.MediaApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    youtube_transcript_request = flowhunt-python-sdk.YoutubeTranscriptRequest() # YoutubeTranscriptRequest | 

    try:
        # Get Youtube Transcript
        api_response = api_instance.get_youtube_transcript(workspace_id, youtube_transcript_request)
        print("The response of MediaApi->get_youtube_transcript:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_youtube_transcript: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **youtube_transcript_request** | [**YoutubeTranscriptRequest**](YoutubeTranscriptRequest.md)|  | 

### Return type

[**YoutubeTranscriptResponse**](YoutubeTranscriptResponse.md)

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

