# flowhunt.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration**](IntegrationsApi.md#create_integration) | **POST** /v2/integrations/{slug}/integrate | Create Integration
[**customer_data_request**](IntegrationsApi.md#customer_data_request) | **POST** /v2/integrations/shopify/webhooks/customers/data_request | Customer Data Request
[**customer_redact**](IntegrationsApi.md#customer_redact) | **POST** /v2/integrations/shopify/webhooks/customers/redact | Customer Redact
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /v2/integrations/{slug}/{integration_id} | Delete Integration
[**get_actors**](IntegrationsApi.md#get_actors) | **GET** /v2/integrations/hubspot/actors/ | Get Actors
[**get_all_integrations**](IntegrationsApi.md#get_all_integrations) | **GET** /v2/integrations/all | Get All Integrations
[**get_calendars**](IntegrationsApi.md#get_calendars) | **GET** /v2/integrations/google/calendar | Get Calendars
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /v2/integrations/{slug}/{integration_id} | Get Integration
[**get_picker_token**](IntegrationsApi.md#get_picker_token) | **GET** /v2/integrations/google/picker_token | Get Picker Token
[**get_profile_information**](IntegrationsApi.md#get_profile_information) | **GET** /v2/integrations/instagram/profile_information | Get Profile Information
[**get_sheets**](IntegrationsApi.md#get_sheets) | **GET** /v2/integrations/google/sheets/{document_id} | Get Sheets
[**get_slack_channels**](IntegrationsApi.md#get_slack_channels) | **GET** /v2/integrations/slack/{slack_team_id}/channels | Get Slack Channels
[**get_slack_workspaces**](IntegrationsApi.md#get_slack_workspaces) | **GET** /v2/integrations/slack/ | Get Slack Workspaces
[**get_wordpress_post_categories**](IntegrationsApi.md#get_wordpress_post_categories) | **GET** /v2/integrations/wordpress/{integration_id}/categories | Get Wordpress Post Categories
[**get_wordpress_post_tags**](IntegrationsApi.md#get_wordpress_post_tags) | **GET** /v2/integrations/wordpress/{integration_id}/tags | Get Wordpress Post Tags
[**get_wordpress_sites**](IntegrationsApi.md#get_wordpress_sites) | **GET** /v2/integrations/wordpress/sites | Get Wordpress Sites
[**integration_callback**](IntegrationsApi.md#integration_callback) | **GET** /v2/integrations/{slug}/callback | Integration Callback
[**search_integrations**](IntegrationsApi.md#search_integrations) | **POST** /v2/integrations/{slug} | Search Integrations
[**shop_redact**](IntegrationsApi.md#shop_redact) | **POST** /v2/integrations/shopify/webhooks/shop/redact | Shop Redact
[**update_admin_consent**](IntegrationsApi.md#update_admin_consent) | **POST** /v2/integrations/microsoft_entra_id/admin_consent | Update Admin Consent


# **create_integration**
> IntegrationFlowResponse create_integration(slug, workspace_id)

Create Integration

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_flow_response import IntegrationFlowResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Create Integration
        api_response = api_instance.create_integration(slug, workspace_id)
        print("The response of IntegrationsApi->create_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **workspace_id** | **str**|  | 

### Return type

[**IntegrationFlowResponse**](IntegrationFlowResponse.md)

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

# **customer_data_request**
> object customer_data_request(customer_data_request_payload)

Customer Data Request

Handle customer data request webhooks from Shopify.

This endpoint is called when a customer requests their data from a Shopify store.

Args:
    request: The FastAPI request object
    payload: The webhook payload

Returns:
    A 200 OK response if the webhook is valid and processed successfully

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.customer_data_request_payload import CustomerDataRequestPayload
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    customer_data_request_payload = flowhunt.CustomerDataRequestPayload() # CustomerDataRequestPayload | 

    try:
        # Customer Data Request
        api_response = api_instance.customer_data_request(customer_data_request_payload)
        print("The response of IntegrationsApi->customer_data_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->customer_data_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_data_request_payload** | [**CustomerDataRequestPayload**](CustomerDataRequestPayload.md)|  | 

### Return type

**object**

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

# **customer_redact**
> object customer_redact(customer_redact_payload)

Customer Redact

Handle customer redact webhooks from Shopify.

This endpoint is called when a customer requests their data to be deleted from a Shopify store.

Args:
    request: The FastAPI request object
    payload: The webhook payload

Returns:
    A 200 OK response if the webhook is valid and processed successfully

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.customer_redact_payload import CustomerRedactPayload
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    customer_redact_payload = flowhunt.CustomerRedactPayload() # CustomerRedactPayload | 

    try:
        # Customer Redact
        api_response = api_instance.customer_redact(customer_redact_payload)
        print("The response of IntegrationsApi->customer_redact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->customer_redact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_redact_payload** | [**CustomerRedactPayload**](CustomerRedactPayload.md)|  | 

### Return type

**object**

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

# **delete_integration**
> Completed delete_integration(slug, integration_id, workspace_id)

Delete Integration

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.completed import Completed
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Integration
        api_response = api_instance.delete_integration(slug, integration_id, workspace_id)
        print("The response of IntegrationsApi->delete_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->delete_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**Completed**](Completed.md)

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

# **get_actors**
> HubSpotActorsResponse get_actors(workspace_id)

Get Actors

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.hub_spot_actors_response import HubSpotActorsResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Actors
        api_response = api_instance.get_actors(workspace_id)
        print("The response of IntegrationsApi->get_actors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_actors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**HubSpotActorsResponse**](HubSpotActorsResponse.md)

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

# **get_all_integrations**
> List[IntegrationResponse] get_all_integrations(workspace_id)

Get All Integrations

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_response import IntegrationResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get All Integrations
        api_response = api_instance.get_all_integrations(workspace_id)
        print("The response of IntegrationsApi->get_all_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_all_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[IntegrationResponse]**](IntegrationResponse.md)

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

# **get_calendars**
> GoogleCalendarsResponse get_calendars(workspace_id)

Get Calendars

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_calendars_response import GoogleCalendarsResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Calendars
        api_response = api_instance.get_calendars(workspace_id)
        print("The response of IntegrationsApi->get_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_calendars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GoogleCalendarsResponse**](GoogleCalendarsResponse.md)

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

# **get_integration**
> IntegrationDetailResponse get_integration(slug, integration_id, workspace_id)

Get Integration

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_detail_response import IntegrationDetailResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Integration
        api_response = api_instance.get_integration(slug, integration_id, workspace_id)
        print("The response of IntegrationsApi->get_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **integration_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**IntegrationDetailResponse**](IntegrationDetailResponse.md)

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

# **get_picker_token**
> GooglePickerTokenResponse get_picker_token(workspace_id)

Get Picker Token

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_picker_token_response import GooglePickerTokenResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Picker Token
        api_response = api_instance.get_picker_token(workspace_id)
        print("The response of IntegrationsApi->get_picker_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_picker_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**GooglePickerTokenResponse**](GooglePickerTokenResponse.md)

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

# **get_profile_information**
> InstagramProfileInformationResponse get_profile_information(workspace_id)

Get Profile Information

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.instagram_profile_information_response import InstagramProfileInformationResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Profile Information
        api_response = api_instance.get_profile_information(workspace_id)
        print("The response of IntegrationsApi->get_profile_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_profile_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**InstagramProfileInformationResponse**](InstagramProfileInformationResponse.md)

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

# **get_sheets**
> GoogleSheetsResponse get_sheets(document_id, workspace_id)

Get Sheets

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.google_sheets_response import GoogleSheetsResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    document_id = 'document_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Sheets
        api_response = api_instance.get_sheets(document_id, workspace_id)
        print("The response of IntegrationsApi->get_sheets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_sheets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**GoogleSheetsResponse**](GoogleSheetsResponse.md)

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

# **get_slack_channels**
> List[SlackChannelResponse] get_slack_channels(slack_team_id, workspace_id)

Get Slack Channels

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.slack_channel_response import SlackChannelResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slack_team_id = 'slack_team_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Slack Channels
        api_response = api_instance.get_slack_channels(slack_team_id, workspace_id)
        print("The response of IntegrationsApi->get_slack_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_slack_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slack_team_id** | **str**|  | 
 **workspace_id** | **str**|  | 

### Return type

[**List[SlackChannelResponse]**](SlackChannelResponse.md)

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

# **get_slack_workspaces**
> List[SlackWorkspaceResponse] get_slack_workspaces(workspace_id)

Get Slack Workspaces

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.slack_workspace_response import SlackWorkspaceResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Slack Workspaces
        api_response = api_instance.get_slack_workspaces(workspace_id)
        print("The response of IntegrationsApi->get_slack_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_slack_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[SlackWorkspaceResponse]**](SlackWorkspaceResponse.md)

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

# **get_wordpress_post_categories**
> List[WordPressCategoryResponse] get_wordpress_post_categories(integration_id, workspace_id)

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
    api_instance = flowhunt.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Post Categories
        api_response = api_instance.get_wordpress_post_categories(integration_id, workspace_id)
        print("The response of IntegrationsApi->get_wordpress_post_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_wordpress_post_categories: %s\n" % e)
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

# **get_wordpress_post_tags**
> List[WordPressTagsResponse] get_wordpress_post_tags(integration_id, workspace_id)

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
    api_instance = flowhunt.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Post Tags
        api_response = api_instance.get_wordpress_post_tags(integration_id, workspace_id)
        print("The response of IntegrationsApi->get_wordpress_post_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_wordpress_post_tags: %s\n" % e)
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

# **get_wordpress_sites**
> List[WordPressSiteResponse] get_wordpress_sites(workspace_id)

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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Wordpress Sites
        api_response = api_instance.get_wordpress_sites(workspace_id)
        print("The response of IntegrationsApi->get_wordpress_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_wordpress_sites: %s\n" % e)
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

# **integration_callback**
> object integration_callback(slug)

Integration Callback

### Example


```python
import flowhunt
from flowhunt.models.integration_slug import IntegrationSlug
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 

    try:
        # Integration Callback
        api_response = api_instance.integration_callback(slug)
        print("The response of IntegrationsApi->integration_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->integration_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_integrations**
> List[IntegrationDetailResponse] search_integrations(slug, workspace_id, integration_search_request)

Search Integrations

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_detail_response import IntegrationDetailResponse
from flowhunt.models.integration_search_request import IntegrationSearchRequest
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    slug = flowhunt.IntegrationSlug() # IntegrationSlug | 
    workspace_id = 'workspace_id_example' # str | 
    integration_search_request = flowhunt.IntegrationSearchRequest() # IntegrationSearchRequest | 

    try:
        # Search Integrations
        api_response = api_instance.search_integrations(slug, workspace_id, integration_search_request)
        print("The response of IntegrationsApi->search_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->search_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**IntegrationSlug**](.md)|  | 
 **workspace_id** | **str**|  | 
 **integration_search_request** | [**IntegrationSearchRequest**](IntegrationSearchRequest.md)|  | 

### Return type

[**List[IntegrationDetailResponse]**](IntegrationDetailResponse.md)

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

# **shop_redact**
> object shop_redact(shop_redact_payload)

Shop Redact

Handle shop redact webhooks from Shopify.

This endpoint is called 48 hours after a store owner uninstalls the app.

Args:
    request: The FastAPI request object
    payload: The webhook payload

Returns:
    A 200 OK response if the webhook is valid and processed successfully

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.shop_redact_payload import ShopRedactPayload
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    shop_redact_payload = flowhunt.ShopRedactPayload() # ShopRedactPayload | 

    try:
        # Shop Redact
        api_response = api_instance.shop_redact(shop_redact_payload)
        print("The response of IntegrationsApi->shop_redact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->shop_redact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_redact_payload** | [**ShopRedactPayload**](ShopRedactPayload.md)|  | 

### Return type

**object**

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

# **update_admin_consent**
> IntegrationDetailResponse update_admin_consent(workspace_id, integration_id)

Update Admin Consent

### Example

* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.integration_detail_response import IntegrationDetailResponse
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
    api_instance = flowhunt.IntegrationsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    integration_id = 'integration_id_example' # str | 

    try:
        # Update Admin Consent
        api_response = api_instance.update_admin_consent(workspace_id, integration_id)
        print("The response of IntegrationsApi->update_admin_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->update_admin_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **integration_id** | **str**|  | 

### Return type

[**IntegrationDetailResponse**](IntegrationDetailResponse.md)

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

