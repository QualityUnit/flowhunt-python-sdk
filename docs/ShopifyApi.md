# flowhunt.ShopifyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_data_request**](ShopifyApi.md#customer_data_request) | **POST** /v2/integrations/shopify/webhooks/customers/data_request | Customer Data Request
[**customer_redact**](ShopifyApi.md#customer_redact) | **POST** /v2/integrations/shopify/webhooks/customers/redact | Customer Redact
[**shop_redact**](ShopifyApi.md#shop_redact) | **POST** /v2/integrations/shopify/webhooks/shop/redact | Shop Redact


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
    api_instance = flowhunt.ShopifyApi(api_client)
    customer_data_request_payload = flowhunt.CustomerDataRequestPayload() # CustomerDataRequestPayload | 

    try:
        # Customer Data Request
        api_response = api_instance.customer_data_request(customer_data_request_payload)
        print("The response of ShopifyApi->customer_data_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopifyApi->customer_data_request: %s\n" % e)
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
    api_instance = flowhunt.ShopifyApi(api_client)
    customer_redact_payload = flowhunt.CustomerRedactPayload() # CustomerRedactPayload | 

    try:
        # Customer Redact
        api_response = api_instance.customer_redact(customer_redact_payload)
        print("The response of ShopifyApi->customer_redact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopifyApi->customer_redact: %s\n" % e)
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
    api_instance = flowhunt.ShopifyApi(api_client)
    shop_redact_payload = flowhunt.ShopRedactPayload() # ShopRedactPayload | 

    try:
        # Shop Redact
        api_response = api_instance.shop_redact(shop_redact_payload)
        print("The response of ShopifyApi->shop_redact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopifyApi->shop_redact: %s\n" % e)
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

