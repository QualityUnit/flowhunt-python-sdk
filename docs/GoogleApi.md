# flowhunt.GoogleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drive_document_detail_0**](GoogleApi.md#get_drive_document_detail_0) | **POST** /v2/integrations/google/drive/files/{document_id} | Get Drive Document Detail
[**get_drive_documents_0**](GoogleApi.md#get_drive_documents_0) | **POST** /v2/integrations/google/{integration_slug}/drive/files | Get Drive Documents


# **get_drive_document_detail_0**
> GoogleDriveFileResponse get_drive_document_detail_0(document_id, workspace_id)

Get Drive Document Detail

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_drive_file_response import GoogleDriveFileResponse
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
    api_instance = flowhunt.GoogleApi(api_client)
    document_id = 'document_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Drive Document Detail
        api_response = api_instance.get_drive_document_detail_0(document_id, workspace_id)
        print("The response of GoogleApi->get_drive_document_detail_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->get_drive_document_detail_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleDriveFileResponse**](GoogleDriveFileResponse.md)

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

# **get_drive_documents_0**
> GoogleDriveSearchResponse get_drive_documents_0(integration_slug, workspace_id, google_drive_search_query)

Get Drive Documents

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_drive_search_query import GoogleDriveSearchQuery
from flowhunt.models.google_drive_search_response import GoogleDriveSearchResponse
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
    api_instance = flowhunt.GoogleApi(api_client)
    integration_slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    workspace_id = 'workspace_id_example' # str | 
    google_drive_search_query = flowhunt.GoogleDriveSearchQuery() # GoogleDriveSearchQuery | 

    try:
        # Get Drive Documents
        api_response = api_instance.get_drive_documents_0(integration_slug, workspace_id, google_drive_search_query)
        print("The response of GoogleApi->get_drive_documents_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleApi->get_drive_documents_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_slug** | [**IntegrationSlug**](.md)|  | 
 **workspace_id** | **str**|  | 
 **google_drive_search_query** | [**GoogleDriveSearchQuery**](GoogleDriveSearchQuery.md)|  | 

### Return type

[**GoogleDriveSearchResponse**](GoogleDriveSearchResponse.md)

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

