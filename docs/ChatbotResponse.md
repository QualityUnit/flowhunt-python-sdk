# ChatbotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace id | 
**chatbot_id** | **str** | Chatbot id | 
**title** | **str** | Tenant name | 
**description** | **str** |  | [optional] 
**flow_id** | **str** | Flow ID | 
**status** | [**ChatbotStatus**](ChatbotStatus.md) |  | 
**url_suffix** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**max_window_size** | **str** |  | [optional] 
**msg_rpm** | **int** |  | [optional] 
**msg_ip_rpm** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.chatbot_response import ChatbotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotResponse from a JSON string
chatbot_response_instance = ChatbotResponse.from_json(json)
# print the JSON string representation of the object
print(ChatbotResponse.to_json())

# convert the object into a dict
chatbot_response_dict = chatbot_response_instance.to_dict()
# create an instance of ChatbotResponse from a dict
chatbot_response_from_dict = ChatbotResponse.from_dict(chatbot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


