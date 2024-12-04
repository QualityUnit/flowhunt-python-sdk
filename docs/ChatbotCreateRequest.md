# ChatbotCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**flow_id** | **str** | Chatbot Flow ID | [optional] 
**status** | [**ChatbotStatus**](ChatbotStatus.md) |  | 
**url_suffix** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**max_window_size** | **str** |  | [optional] 
**msg_rpm** | **int** |  | [optional] 
**msg_ip_rpm** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.chatbot_create_request import ChatbotCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotCreateRequest from a JSON string
chatbot_create_request_instance = ChatbotCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ChatbotCreateRequest.to_json())

# convert the object into a dict
chatbot_create_request_dict = chatbot_create_request_instance.to_dict()
# create an instance of ChatbotCreateRequest from a dict
chatbot_create_request_from_dict = ChatbotCreateRequest.from_dict(chatbot_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


