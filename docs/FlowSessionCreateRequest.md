# FlowSessionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL | [optional] 
**lang** | **str** | Session language attribute | [optional] [default to 'en']
**access_token** | **str** | The access token | [optional] 
**refresh_token** | **str** | The refresh token | [optional] 
**username** | **str** | The username | [optional] 
**password** | **str** | The password | [optional] 
**variables** | **Dict[str, str]** | Agent input variables | [optional] 
**chatbot_id** | **str** | The chatbot ID | 
**on_chat_opened_postback_url** | **str** | The on chat opened postback URL | [optional] 

## Example

```python
from flowhunt.models.flow_session_create_request import FlowSessionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionCreateRequest from a JSON string
flow_session_create_request_instance = FlowSessionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionCreateRequest.to_json())

# convert the object into a dict
flow_session_create_request_dict = flow_session_create_request_instance.to_dict()
# create an instance of FlowSessionCreateRequest from a dict
flow_session_create_request_from_dict = FlowSessionCreateRequest.from_dict(flow_session_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


