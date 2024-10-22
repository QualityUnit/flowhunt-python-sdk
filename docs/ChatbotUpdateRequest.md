# ChatbotUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url_suffix** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**max_window_size** | **str** |  | [optional] 
**msg_rpm** | **int** |  | [optional] 
**msg_ip_rpm** | **int** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.chatbot_update_request import ChatbotUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotUpdateRequest from a JSON string
chatbot_update_request_instance = ChatbotUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ChatbotUpdateRequest.to_json())

# convert the object into a dict
chatbot_update_request_dict = chatbot_update_request_instance.to_dict()
# create an instance of ChatbotUpdateRequest from a dict
chatbot_update_request_from_dict = ChatbotUpdateRequest.from_dict(chatbot_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


