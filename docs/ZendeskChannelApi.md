# flowhunt.ZendeskChannelApi

All URIs are relative to *https://api.flowhunt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_ui**](ZendeskChannelApi.md#admin_ui) | **POST** /v2/integrations/zendesk_channel/admin_ui | Admin Ui
[**channelback**](ZendeskChannelApi.md#channelback) | **POST** /v2/integrations/zendesk_channel/channelback | Channelback
[**events_callback**](ZendeskChannelApi.md#events_callback) | **POST** /v2/integrations/zendesk_channel/events | Events Callback
[**manifest**](ZendeskChannelApi.md#manifest) | **GET** /v2/integrations/zendesk_channel/manifest.json | Manifest
[**messaging_webhook**](ZendeskChannelApi.md#messaging_webhook) | **POST** /v2/integrations/zendesk_channel/messaging_webhook | Messaging Webhook
[**messaging_webhook_head**](ZendeskChannelApi.md#messaging_webhook_head) | **HEAD** /v2/integrations/zendesk_channel/messaging_webhook | Messaging Webhook Head


# **admin_ui**
> str admin_ui()

Admin Ui

Zendesk Channel Framework admin UI callback.

Zendesk sends a URL-encoded form POST with account information.  We
persist the push credentials on the matching integration record and
return a small HTML page that auto-submits back to Zendesk's
``return_url``.

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ZendeskChannelApi(api_client)

    try:
        # Admin Ui
        api_response = api_instance.admin_ui()
        print("The response of ZendeskChannelApi->admin_ui:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskChannelApi->admin_ui: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channelback**
> object channelback()

Channelback

Zendesk Channel Framework channelback endpoint.

Called by Zendesk when an agent replies to a ticket that was created
via the Channel Framework push API.  The agent's message is routed
back to the originating chat session.

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ZendeskChannelApi(api_client)

    try:
        # Channelback
        api_response = api_instance.channelback()
        print("The response of ZendeskChannelApi->channelback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskChannelApi->channelback: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_callback**
> object events_callback()

Events Callback

Zendesk Channel Framework event callback.

Receives event notifications from Zendesk (e.g. resource lifecycle
events).  Logged for debugging and acknowledged with 200 OK.

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ZendeskChannelApi(api_client)

    try:
        # Events Callback
        api_response = api_instance.events_callback()
        print("The response of ZendeskChannelApi->events_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskChannelApi->events_callback: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manifest**
> object manifest()

Manifest

Return the Zendesk Channel Framework manifest.

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ZendeskChannelApi(api_client)

    try:
        # Manifest
        api_response = api_instance.manifest()
        print("The response of ZendeskChannelApi->manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskChannelApi->manifest: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messaging_webhook**
> object messaging_webhook()

Messaging Webhook

Zendesk Sunshine Conversations (Messaging API) webhook endpoint.

Receives webhook events from the Sunshine Conversations API:
- conversation:message -- agent replies to escalated conversations
- switchboard:passControl -- control handed back to our bot
- switchboard:releaseControl -- agent releases control

Agent messages are routed back to the originating FlowHunt session
via the ZendeskAgentReply trigger.

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ZendeskChannelApi(api_client)

    try:
        # Messaging Webhook
        api_response = api_instance.messaging_webhook()
        print("The response of ZendeskChannelApi->messaging_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskChannelApi->messaging_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messaging_webhook_head**
> object messaging_webhook_head()

Messaging Webhook Head

Health check endpoint for Zendesk webhook registration.

### Example


```python
import flowhunt
from flowhunt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.flowhunt.io
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt.Configuration(
    host = "https://api.flowhunt.io"
)


# Enter a context with an instance of the API client
with flowhunt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt.ZendeskChannelApi(api_client)

    try:
        # Messaging Webhook Head
        api_response = api_instance.messaging_webhook_head()
        print("The response of ZendeskChannelApi->messaging_webhook_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskChannelApi->messaging_webhook_head: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

