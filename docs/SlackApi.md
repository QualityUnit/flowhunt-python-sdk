# flowhunt.SlackApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_slack_channels**](SlackApi.md#get_slack_channels) | **GET** /v2/integrations/slack/{slack_team_id}/channels | Get Slack Channels
[**get_slack_workspaces**](SlackApi.md#get_slack_workspaces) | **GET** /v2/integrations/slack/ | Get Slack Workspaces


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

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
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
    api_instance = flowhunt.SlackApi(api_client)
    slack_team_id = 'slack_team_id_example' # str | 
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Slack Channels
        api_response = api_instance.get_slack_channels(slack_team_id, workspace_id)
        print("The response of SlackApi->get_slack_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->get_slack_channels: %s\n" % e)
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

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
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
    api_instance = flowhunt.SlackApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Slack Workspaces
        api_response = api_instance.get_slack_workspaces(workspace_id)
        print("The response of SlackApi->get_slack_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlackApi->get_slack_workspaces: %s\n" % e)
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

