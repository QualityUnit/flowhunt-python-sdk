# flowhunt.WorkspacesSSODomainVerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain_verification**](WorkspacesSSODomainVerificationApi.md#create_domain_verification) | **POST** /v2/workspaces/{workspace_id}/sso/domain-verification | Create Domain Verification
[**delete_domain_verification**](WorkspacesSSODomainVerificationApi.md#delete_domain_verification) | **DELETE** /v2/workspaces/{workspace_id}/sso/domain-verification | Delete Domain Verification
[**list_domain_verifications**](WorkspacesSSODomainVerificationApi.md#list_domain_verifications) | **GET** /v2/workspaces/{workspace_id}/sso/domain-verification | List Domain Verifications
[**verify_domain**](WorkspacesSSODomainVerificationApi.md#verify_domain) | **POST** /v2/workspaces/{workspace_id}/sso/domain-verification/verify | Verify Domain


# **create_domain_verification**
> WorkspaceSSODomainVerificationResponse create_domain_verification(workspace_id, workspace_sso_domain_verification_create_request)

Create Domain Verification

Create a new domain verification record.
Admin endpoint - requires workspace admin permissions.
Enterprise feature - requires enterprise subscription.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_domain_verification_create_request import WorkspaceSSODomainVerificationCreateRequest
from flowhunt.models.workspace_sso_domain_verification_response import WorkspaceSSODomainVerificationResponse
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
    api_instance = flowhunt.WorkspacesSSODomainVerificationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_sso_domain_verification_create_request = flowhunt.WorkspaceSSODomainVerificationCreateRequest() # WorkspaceSSODomainVerificationCreateRequest | 

    try:
        # Create Domain Verification
        api_response = api_instance.create_domain_verification(workspace_id, workspace_sso_domain_verification_create_request)
        print("The response of WorkspacesSSODomainVerificationApi->create_domain_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSODomainVerificationApi->create_domain_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_sso_domain_verification_create_request** | [**WorkspaceSSODomainVerificationCreateRequest**](WorkspaceSSODomainVerificationCreateRequest.md)|  | 

### Return type

[**WorkspaceSSODomainVerificationResponse**](WorkspaceSSODomainVerificationResponse.md)

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

# **delete_domain_verification**
> Completed delete_domain_verification(workspace_id)

Delete Domain Verification

Delete a domain verification record.
Admin endpoint - requires workspace admin permissions.
Enterprise feature - requires enterprise subscription.

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
    api_instance = flowhunt.WorkspacesSSODomainVerificationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Domain Verification
        api_response = api_instance.delete_domain_verification(workspace_id)
        print("The response of WorkspacesSSODomainVerificationApi->delete_domain_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSODomainVerificationApi->delete_domain_verification: %s\n" % e)
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

# **list_domain_verifications**
> List[WorkspaceSSODomainVerificationResponse] list_domain_verifications(workspace_id)

List Domain Verifications

List all domain verifications for a workspace.
Admin endpoint - requires workspace admin permissions.
Enterprise feature - requires enterprise subscription.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_domain_verification_response import WorkspaceSSODomainVerificationResponse
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
    api_instance = flowhunt.WorkspacesSSODomainVerificationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List Domain Verifications
        api_response = api_instance.list_domain_verifications(workspace_id)
        print("The response of WorkspacesSSODomainVerificationApi->list_domain_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSODomainVerificationApi->list_domain_verifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[WorkspaceSSODomainVerificationResponse]**](WorkspaceSSODomainVerificationResponse.md)

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

# **verify_domain**
> WorkspaceSSODomainVerificationResponse verify_domain(workspace_id)

Verify Domain

Verify a domain by checking DNS TXT records.
Admin endpoint - requires workspace admin permissions.
Enterprise feature - requires enterprise subscription.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

```python
import flowhunt
from flowhunt.models.workspace_sso_domain_verification_response import WorkspaceSSODomainVerificationResponse
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
    api_instance = flowhunt.WorkspacesSSODomainVerificationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Verify Domain
        api_response = api_instance.verify_domain(workspace_id)
        print("The response of WorkspacesSSODomainVerificationApi->verify_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesSSODomainVerificationApi->verify_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceSSODomainVerificationResponse**](WorkspaceSSODomainVerificationResponse.md)

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

