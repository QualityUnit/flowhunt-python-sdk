# flowhunt.CreditsApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credit_balance**](CreditsApi.md#get_credit_balance) | **GET** /v2/credits/balance | Get Credit Balance
[**get_daily_chart_data**](CreditsApi.md#get_daily_chart_data) | **POST** /v2/credits/daily/chart | Get Daily Chart Data
[**get_workspace_credit_balance**](CreditsApi.md#get_workspace_credit_balance) | **GET** /v2/credits/workspace_balance | Get Workspace Credit Balance
[**search_credit_transactions**](CreditsApi.md#search_credit_transactions) | **POST** /v2/credits/search | Search Credit Transactions
[**search_daily_credit_transactions**](CreditsApi.md#search_daily_credit_transactions) | **POST** /v2/credits/search_daily | Search Daily Credit Transactions


# **get_credit_balance**
> CreditBalanceResponse get_credit_balance()

Get Credit Balance

Get the credit balance for the current user.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.credit_balance_response import CreditBalanceResponse
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
    api_instance = flowhunt.CreditsApi(api_client)

    try:
        # Get Credit Balance
        api_response = api_instance.get_credit_balance()
        print("The response of CreditsApi->get_credit_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_credit_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreditBalanceResponse**](CreditBalanceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_daily_chart_data**
> CreditDailyChartResponse get_daily_chart_data(workspace_id, credit_daily_chart_request)

Get Daily Chart Data

Get daily credit transactions aggregated for chart display.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.credit_daily_chart_request import CreditDailyChartRequest
from flowhunt.models.credit_daily_chart_response import CreditDailyChartResponse
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
    api_instance = flowhunt.CreditsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    credit_daily_chart_request = flowhunt.CreditDailyChartRequest() # CreditDailyChartRequest | 

    try:
        # Get Daily Chart Data
        api_response = api_instance.get_daily_chart_data(workspace_id, credit_daily_chart_request)
        print("The response of CreditsApi->get_daily_chart_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_daily_chart_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **credit_daily_chart_request** | [**CreditDailyChartRequest**](CreditDailyChartRequest.md)|  | 

### Return type

[**CreditDailyChartResponse**](CreditDailyChartResponse.md)

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

# **get_workspace_credit_balance**
> CreditBalanceResponse get_workspace_credit_balance(workspace_id)

Get Workspace Credit Balance

Get the credit balance for a workspace.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.credit_balance_response import CreditBalanceResponse
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
    api_instance = flowhunt.CreditsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Workspace Credit Balance
        api_response = api_instance.get_workspace_credit_balance(workspace_id)
        print("The response of CreditsApi->get_workspace_credit_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_workspace_credit_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**CreditBalanceResponse**](CreditBalanceResponse.md)

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

# **search_credit_transactions**
> List[CreditTransactionResponse] search_credit_transactions(workspace_id, credit_transaction_search_request)

Search Credit Transactions

Search for credit transactions based on criteria.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.credit_transaction_response import CreditTransactionResponse
from flowhunt.models.credit_transaction_search_request import CreditTransactionSearchRequest
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
    api_instance = flowhunt.CreditsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    credit_transaction_search_request = flowhunt.CreditTransactionSearchRequest() # CreditTransactionSearchRequest | 

    try:
        # Search Credit Transactions
        api_response = api_instance.search_credit_transactions(workspace_id, credit_transaction_search_request)
        print("The response of CreditsApi->search_credit_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->search_credit_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **credit_transaction_search_request** | [**CreditTransactionSearchRequest**](CreditTransactionSearchRequest.md)|  | 

### Return type

[**List[CreditTransactionResponse]**](CreditTransactionResponse.md)

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

# **search_daily_credit_transactions**
> List[CreditDailyTransactionResponse] search_daily_credit_transactions(workspace_id, credit_daily_transaction_search_request)

Search Daily Credit Transactions

Search for daily credit transactions based on criteria.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.credit_daily_transaction_response import CreditDailyTransactionResponse
from flowhunt.models.credit_daily_transaction_search_request import CreditDailyTransactionSearchRequest
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
    api_instance = flowhunt.CreditsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    credit_daily_transaction_search_request = flowhunt.CreditDailyTransactionSearchRequest() # CreditDailyTransactionSearchRequest | 

    try:
        # Search Daily Credit Transactions
        api_response = api_instance.search_daily_credit_transactions(workspace_id, credit_daily_transaction_search_request)
        print("The response of CreditsApi->search_daily_credit_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->search_daily_credit_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **credit_daily_transaction_search_request** | [**CreditDailyTransactionSearchRequest**](CreditDailyTransactionSearchRequest.md)|  | 

### Return type

[**List[CreditDailyTransactionResponse]**](CreditDailyTransactionResponse.md)

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

