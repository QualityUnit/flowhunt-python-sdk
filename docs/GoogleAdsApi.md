# flowhunt.GoogleAdsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_not_assigned_keywords**](GoogleAdsApi.md#analyze_not_assigned_keywords) | **POST** /v2/integrations/google_ads/analyze_not_assigned_keywords | Analyze Not Assigned Keywords
[**get_google_ads_campaigns**](GoogleAdsApi.md#get_google_ads_campaigns) | **POST** /v2/integrations/google_ads/{customer_id}/campaigns | Get Google Ads Campaigns
[**get_google_ads_customers**](GoogleAdsApi.md#get_google_ads_customers) | **POST** /v2/integrations/google_ads/customers | Get Google Ads Customers
[**get_google_ads_groups**](GoogleAdsApi.md#get_google_ads_groups) | **POST** /v2/integrations/google_ads/{customer_id}/campaigns/{campaign_id}/groups | Get Google Ads Groups
[**import_all_google_ads_groups**](GoogleAdsApi.md#import_all_google_ads_groups) | **POST** /v2/integrations/google_ads/{customer_id}/campaigns/import_all_groups | Import All Google Ads Groups
[**import_google_ads_campaigns**](GoogleAdsApi.md#import_google_ads_campaigns) | **POST** /v2/integrations/google_ads/{customer_id}/campaigns/import | Import Google Ads Campaigns
[**import_google_ads_customers**](GoogleAdsApi.md#import_google_ads_customers) | **POST** /v2/integrations/google_ads/customers/import | Import Google Ads Customers
[**import_google_ads_groups**](GoogleAdsApi.md#import_google_ads_groups) | **POST** /v2/integrations/google_ads/{customer_id}/campaigns/{campaign_id}/groups/import | Import Google Ads Groups
[**update_google_ads_campaign**](GoogleAdsApi.md#update_google_ads_campaign) | **PUT** /v2/integrations/google_ads/{customer_id}/campaigns/{campaign_id} | Update Google Ads Campaign
[**update_google_ads_customer_update**](GoogleAdsApi.md#update_google_ads_customer_update) | **PUT** /v2/integrations/google_ads/customers/{customer_id} | Update Google Ads Customer Update
[**update_google_ads_group**](GoogleAdsApi.md#update_google_ads_group) | **PUT** /v2/integrations/google_ads/{customer_id}/campaigns/{campaign_id}/groups/{group_id} | Update Google Ads Group


# **analyze_not_assigned_keywords**
> Completed analyze_not_assigned_keywords(workspace_id)

Analyze Not Assigned Keywords

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
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
        # Analyze Not Assigned Keywords
        api_response = api_instance.analyze_not_assigned_keywords(workspace_id)
        print("The response of GoogleAdsApi->analyze_not_assigned_keywords:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->analyze_not_assigned_keywords: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_google_ads_campaigns**
> GoogleAdsCampaignsResponse get_google_ads_campaigns(customer_id, workspace_id)

Get Google Ads Campaigns

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_campaigns_response import GoogleAdsCampaignsResponse
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
    customer_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Google Ads Campaigns
        api_response = api_instance.get_google_ads_campaigns(customer_id, workspace_id)
        print("The response of GoogleAdsApi->get_google_ads_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_google_ads_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsCampaignsResponse**](GoogleAdsCampaignsResponse.md)

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

# **get_google_ads_customers**
> GoogleAdsCustomersResponse get_google_ads_customers(workspace_id)

Get Google Ads Customers

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
        # Get Google Ads Customers
        api_response = api_instance.get_google_ads_customers(workspace_id)
        print("The response of GoogleAdsApi->get_google_ads_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_google_ads_customers: %s\n" % e)
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

# **get_google_ads_groups**
> GoogleAdsGroupsResponse get_google_ads_groups(customer_id, campaign_id, workspace_id)

Get Google Ads Groups

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_groups_response import GoogleAdsGroupsResponse
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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Google Ads Groups
        api_response = api_instance.get_google_ads_groups(customer_id, campaign_id, workspace_id)
        print("The response of GoogleAdsApi->get_google_ads_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->get_google_ads_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsGroupsResponse**](GoogleAdsGroupsResponse.md)

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

# **import_all_google_ads_groups**
> GoogleAdsGroupsResponse import_all_google_ads_groups(customer_id, workspace_id)

Import All Google Ads Groups

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_groups_response import GoogleAdsGroupsResponse
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
    customer_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Import All Google Ads Groups
        api_response = api_instance.import_all_google_ads_groups(customer_id, workspace_id)
        print("The response of GoogleAdsApi->import_all_google_ads_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->import_all_google_ads_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsGroupsResponse**](GoogleAdsGroupsResponse.md)

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
> GoogleAdsCampaignsResponse import_google_ads_campaigns(customer_id, workspace_id)

Import Google Ads Campaigns

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_campaigns_response import GoogleAdsCampaignsResponse
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
    customer_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Import Google Ads Campaigns
        api_response = api_instance.import_google_ads_campaigns(customer_id, workspace_id)
        print("The response of GoogleAdsApi->import_google_ads_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->import_google_ads_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsCampaignsResponse**](GoogleAdsCampaignsResponse.md)

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
> GoogleAdsGroupsResponse import_google_ads_groups(customer_id, campaign_id, workspace_id)

Import Google Ads Groups

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_ads_groups_response import GoogleAdsGroupsResponse
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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Import Google Ads Groups
        api_response = api_instance.import_google_ads_groups(customer_id, campaign_id, workspace_id)
        print("The response of GoogleAdsApi->import_google_ads_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleAdsApi->import_google_ads_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleAdsGroupsResponse**](GoogleAdsGroupsResponse.md)

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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
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
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
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
    customer_id = 56 # int | 
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
 **customer_id** | **int**|  | 
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
    customer_id = 56 # int | 
    campaign_id = 56 # int | 
    group_id = 56 # int | 
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
 **customer_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **group_id** | **int**|  | 
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

