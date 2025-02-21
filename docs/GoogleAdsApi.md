# flowhunt.GoogleAdsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_not_assigned_keywords**](GoogleAdsApi.md#analyze_not_assigned_keywords) | **POST** /v2/integrations/google_ads/analyze_not_assigned_keywords | Analyze Not Assigned Keywords
[**get_conversion_tracking_code_examples**](GoogleAdsApi.md#get_conversion_tracking_code_examples) | **POST** /v2/integrations/google_ads/conversion-tracking-code/{customer_id} | Get Conversion Tracking Code Examples
[**get_conversion_tracking_settings**](GoogleAdsApi.md#get_conversion_tracking_settings) | **POST** /v2/integrations/google_ads/conversion-tracking-settings/{customer_id} | Get Conversion Tracking Settings
[**get_google_ads_campaigns**](GoogleAdsApi.md#get_google_ads_campaigns) | **POST** /v2/integrations/google_ads/campaigns | Get Google Ads Campaigns
[**get_google_ads_customers**](GoogleAdsApi.md#get_google_ads_customers) | **POST** /v2/integrations/google_ads/customers | Get Google Ads Customers
[**get_google_ads_groups**](GoogleAdsApi.md#get_google_ads_groups) | **POST** /v2/integrations/google_ads/groups | Get Google Ads Groups
[**get_source_tracking_code_examples**](GoogleAdsApi.md#get_source_tracking_code_examples) | **POST** /v2/integrations/google_ads/source-tracking-code | Get Source Tracking Code Examples
[**import_google_ads_campaigns**](GoogleAdsApi.md#import_google_ads_campaigns) | **POST** /v2/integrations/google_ads/campaigns/import | Import Google Ads Campaigns
[**import_google_ads_customers**](GoogleAdsApi.md#import_google_ads_customers) | **POST** /v2/integrations/google_ads/customers/import | Import Google Ads Customers
[**import_google_ads_groups**](GoogleAdsApi.md#import_google_ads_groups) | **POST** /v2/integrations/google_ads/groups/import | Import Google Ads Groups
[**list_conversion_actions**](GoogleAdsApi.md#list_conversion_actions) | **POST** /v2/integrations/google_ads/conversion-actions/{customer_id} | List Conversion Actions
[**update_google_ads_campaign**](GoogleAdsApi.md#update_google_ads_campaign) | **PUT** /v2/integrations/google_ads/campaigns/{customer_id}/{campaign_id} | Update Google Ads Campaign
[**update_google_ads_customer_update**](GoogleAdsApi.md#update_google_ads_customer_update) | **PUT** /v2/integrations/google_ads/customers/{customer_id} | Update Google Ads Customer Update
[**update_google_ads_group**](GoogleAdsApi.md#update_google_ads_group) | **PUT** /v2/integrations/google_ads/groups/{customer_id}/{campaign_id}/{group_id} | Update Google Ads Group


# **analyze_not_assigned_keywords**
> Completed analyze_not_assigned_keywords(workspace_id, google_ads_analyze_keywords_request)

Analyze Not Assigned Keywords

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
from flowhunt.models.google_ads_analyze_keywords_request import GoogleAdsAnalyzeKeywordsRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    google_ads_analyze_keywords_request = flowhunt.GoogleAdsAnalyzeKeywordsRequest() # GoogleAdsAnalyzeKeywordsRequest | 

    try:
        # Analyze Not Assigned Keywords
        api_response = api_instance.analyze_not_assigned_keywords(workspace_id, google_ads_analyze_keywords_request)
        print("The response of GoogleAdsApi->analyze_not_assigned_keywords:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->analyze_not_assigned_keywords: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **google_ads_analyze_keywords_request** | [**GoogleAdsAnalyzeKeywordsRequest**](GoogleAdsAnalyzeKeywordsRequest.md)|  | 

### Return type

[**Completed**](Completed.md)

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

# **get_conversion_tracking_code_examples**
> GoogleAdsConversionTrackingCodeExamplesResponse get_conversion_tracking_code_examples(customer_id, workspace_id)

Get Conversion Tracking Code Examples

Get example tracking code for each conversion action in the Google Ads account.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_conversion_tracking_code_examples_response import GoogleAdsConversionTrackingCodeExamplesResponse
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Conversion Tracking Code Examples
        api_response = api_instance.get_conversion_tracking_code_examples(customer_id, workspace_id)
        print("The response of GoogleAdsApi->get_conversion_tracking_code_examples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_conversion_tracking_code_examples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsConversionTrackingCodeExamplesResponse**](GoogleAdsConversionTrackingCodeExamplesResponse.md)

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

# **get_conversion_tracking_settings**
> List[GoogleAdsConversionTrackingSettingsResponse] get_conversion_tracking_settings(customer_id, workspace_id)

Get Conversion Tracking Settings

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_conversion_tracking_settings_response import GoogleAdsConversionTrackingSettingsResponse
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Conversion Tracking Settings
        api_response = api_instance.get_conversion_tracking_settings(customer_id, workspace_id)
        print("The response of GoogleAdsApi->get_conversion_tracking_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_conversion_tracking_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[GoogleAdsConversionTrackingSettingsResponse]**](GoogleAdsConversionTrackingSettingsResponse.md)

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

# **get_google_ads_campaigns**
> GoogleAdsCampaignsResponse get_google_ads_campaigns(workspace_id, google_ads_campaigns_search_request)

Get Google Ads Campaigns

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_campaigns_response import GoogleAdsCampaignsResponse
from flowhunt.models.google_ads_campaigns_search_request import GoogleAdsCampaignsSearchRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    google_ads_campaigns_search_request = flowhunt.GoogleAdsCampaignsSearchRequest() # GoogleAdsCampaignsSearchRequest | 

    try:
        # Get Google Ads Campaigns
        api_response = api_instance.get_google_ads_campaigns(workspace_id, google_ads_campaigns_search_request)
        print("The response of GoogleAdsApi->get_google_ads_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_google_ads_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **google_ads_campaigns_search_request** | [**GoogleAdsCampaignsSearchRequest**](GoogleAdsCampaignsSearchRequest.md)|  | 

### Return type

[**GoogleAdsCampaignsResponse**](GoogleAdsCampaignsResponse.md)

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

# **get_google_ads_customers**
> GoogleAdsCustomersResponse get_google_ads_customers(workspace_id, google_ads_customers_search_request)

Get Google Ads Customers

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_customers_response import GoogleAdsCustomersResponse
from flowhunt.models.google_ads_customers_search_request import GoogleAdsCustomersSearchRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    google_ads_customers_search_request = flowhunt.GoogleAdsCustomersSearchRequest() # GoogleAdsCustomersSearchRequest | 

    try:
        # Get Google Ads Customers
        api_response = api_instance.get_google_ads_customers(workspace_id, google_ads_customers_search_request)
        print("The response of GoogleAdsApi->get_google_ads_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_google_ads_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **google_ads_customers_search_request** | [**GoogleAdsCustomersSearchRequest**](GoogleAdsCustomersSearchRequest.md)|  | 

### Return type

[**GoogleAdsCustomersResponse**](GoogleAdsCustomersResponse.md)

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

# **get_google_ads_groups**
> GoogleAdsGroupsResponse get_google_ads_groups(workspace_id, google_ads_groups_search_request)

Get Google Ads Groups

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_groups_response import GoogleAdsGroupsResponse
from flowhunt.models.google_ads_groups_search_request import GoogleAdsGroupsSearchRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    google_ads_groups_search_request = flowhunt.GoogleAdsGroupsSearchRequest() # GoogleAdsGroupsSearchRequest | 

    try:
        # Get Google Ads Groups
        api_response = api_instance.get_google_ads_groups(workspace_id, google_ads_groups_search_request)
        print("The response of GoogleAdsApi->get_google_ads_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_google_ads_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **google_ads_groups_search_request** | [**GoogleAdsGroupsSearchRequest**](GoogleAdsGroupsSearchRequest.md)|  | 

### Return type

[**GoogleAdsGroupsResponse**](GoogleAdsGroupsResponse.md)

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

# **get_source_tracking_code_examples**
> GoogleAdsSourceTrackingCodeExamplesResponse get_source_tracking_code_examples(workspace_id)

Get Source Tracking Code Examples

Get example tracking code for each customer in the workspace.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_source_tracking_code_examples_response import GoogleAdsSourceTrackingCodeExamplesResponse
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Source Tracking Code Examples
        api_response = api_instance.get_source_tracking_code_examples(workspace_id)
        print("The response of GoogleAdsApi->get_source_tracking_code_examples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_source_tracking_code_examples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsSourceTrackingCodeExamplesResponse**](GoogleAdsSourceTrackingCodeExamplesResponse.md)

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

# **import_google_ads_campaigns**
> GoogleAdsCampaignsResponse import_google_ads_campaigns(workspace_id, google_ads_campaigns_search_request)

Import Google Ads Campaigns

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_campaigns_response import GoogleAdsCampaignsResponse
from flowhunt.models.google_ads_campaigns_search_request import GoogleAdsCampaignsSearchRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    google_ads_campaigns_search_request = flowhunt.GoogleAdsCampaignsSearchRequest() # GoogleAdsCampaignsSearchRequest | 

    try:
        # Import Google Ads Campaigns
        api_response = api_instance.import_google_ads_campaigns(workspace_id, google_ads_campaigns_search_request)
        print("The response of GoogleAdsApi->import_google_ads_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->import_google_ads_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **google_ads_campaigns_search_request** | [**GoogleAdsCampaignsSearchRequest**](GoogleAdsCampaignsSearchRequest.md)|  | 

### Return type

[**GoogleAdsCampaignsResponse**](GoogleAdsCampaignsResponse.md)

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

# **import_google_ads_customers**
> GoogleAdsCustomersResponse import_google_ads_customers(workspace_id)

Import Google Ads Customers

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_customers_response import GoogleAdsCustomersResponse
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Import Google Ads Customers
        api_response = api_instance.import_google_ads_customers(workspace_id)
        print("The response of GoogleAdsApi->import_google_ads_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->import_google_ads_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsCustomersResponse**](GoogleAdsCustomersResponse.md)

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

# **import_google_ads_groups**
> GoogleAdsGroupsResponse import_google_ads_groups(workspace_id, google_ads_groups_search_request)

Import Google Ads Groups

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_groups_response import GoogleAdsGroupsResponse
from flowhunt.models.google_ads_groups_search_request import GoogleAdsGroupsSearchRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    google_ads_groups_search_request = flowhunt.GoogleAdsGroupsSearchRequest() # GoogleAdsGroupsSearchRequest | 

    try:
        # Import Google Ads Groups
        api_response = api_instance.import_google_ads_groups(workspace_id, google_ads_groups_search_request)
        print("The response of GoogleAdsApi->import_google_ads_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->import_google_ads_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **google_ads_groups_search_request** | [**GoogleAdsGroupsSearchRequest**](GoogleAdsGroupsSearchRequest.md)|  | 

### Return type

[**GoogleAdsGroupsResponse**](GoogleAdsGroupsResponse.md)

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

# **list_conversion_actions**
> GoogleAdsConversionActionsResponse list_conversion_actions(customer_id, workspace_id)

List Conversion Actions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_conversion_actions_response import GoogleAdsConversionActionsResponse
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Conversion Actions
        api_response = api_instance.list_conversion_actions(customer_id, workspace_id)
        print("The response of GoogleAdsApi->list_conversion_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->list_conversion_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsConversionActionsResponse**](GoogleAdsConversionActionsResponse.md)

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

# **update_google_ads_campaign**
> GoogleAdsCampaignResponse update_google_ads_campaign(customer_id, campaign_id, workspace_id, google_ads_campaign_update_request)

Update Google Ads Campaign

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_campaign_response import GoogleAdsCampaignResponse
from flowhunt.models.google_ads_campaign_update_request import GoogleAdsCampaignUpdateRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    campaign_id = 'campaign_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    google_ads_campaign_update_request = flowhunt.GoogleAdsCampaignUpdateRequest() # GoogleAdsCampaignUpdateRequest | 

    try:
        # Update Google Ads Campaign
        api_response = api_instance.update_google_ads_campaign(customer_id, campaign_id, workspace_id, google_ads_campaign_update_request)
        print("The response of GoogleAdsApi->update_google_ads_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->update_google_ads_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **campaign_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **google_ads_campaign_update_request** | [**GoogleAdsCampaignUpdateRequest**](GoogleAdsCampaignUpdateRequest.md)|  | 

### Return type

[**GoogleAdsCampaignResponse**](GoogleAdsCampaignResponse.md)

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

# **update_google_ads_customer_update**
> GoogleAdsCustomerResponse update_google_ads_customer_update(customer_id, workspace_id, google_ads_customer_update_request)

Update Google Ads Customer Update

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_customer_response import GoogleAdsCustomerResponse
from flowhunt.models.google_ads_customer_update_request import GoogleAdsCustomerUpdateRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    google_ads_customer_update_request = flowhunt.GoogleAdsCustomerUpdateRequest() # GoogleAdsCustomerUpdateRequest | 

    try:
        # Update Google Ads Customer Update
        api_response = api_instance.update_google_ads_customer_update(customer_id, workspace_id, google_ads_customer_update_request)
        print("The response of GoogleAdsApi->update_google_ads_customer_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->update_google_ads_customer_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **google_ads_customer_update_request** | [**GoogleAdsCustomerUpdateRequest**](GoogleAdsCustomerUpdateRequest.md)|  | 

### Return type

[**GoogleAdsCustomerResponse**](GoogleAdsCustomerResponse.md)

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

# **update_google_ads_group**
> GoogleAdsGroupResponse update_google_ads_group(customer_id, campaign_id, group_id, workspace_id, google_ads_group_update_request)

Update Google Ads Group

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_group_response import GoogleAdsGroupResponse
from flowhunt.models.google_ads_group_update_request import GoogleAdsGroupUpdateRequest
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
    api_instance = flowhunt.GoogleAdsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    campaign_id = 'campaign_id_example' # str | 
    group_id = 'group_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 
    google_ads_group_update_request = flowhunt.GoogleAdsGroupUpdateRequest() # GoogleAdsGroupUpdateRequest | 

    try:
        # Update Google Ads Group
        api_response = api_instance.update_google_ads_group(customer_id, campaign_id, group_id, workspace_id, google_ads_group_update_request)
        print("The response of GoogleAdsApi->update_google_ads_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->update_google_ads_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **campaign_id** | **str**|  | 
 **group_id** | **str**|  | 
 **workspace_id** | **str**|  | 
 **google_ads_group_update_request** | [**GoogleAdsGroupUpdateRequest**](GoogleAdsGroupUpdateRequest.md)|  | 

### Return type

[**GoogleAdsGroupResponse**](GoogleAdsGroupResponse.md)

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

