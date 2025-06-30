# ChatbotUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**status** | [**ChatbotStatus**](ChatbotStatus.md) |  | [optional] 
**url_suffix** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**max_window_size** | **str** |  | [optional] 
**msg_rpm** | **int** |  | [optional] 
**msg_ip_rpm** | **int** |  | [optional] 
**chatbot_description** | **str** |  | [optional] 
**show_chatbot_header** | **bool** |  | [optional] 
**chat_bubble_bg_color** | **str** |  | [optional] 
**chat_bubble_icon_color** | **str** |  | [optional] 
**chat_bubble_img_url** | **str** |  | [optional] 
**chatbot_theme** | **str** |  | [optional] 
**chatbot_position** | **str** |  | [optional] 
**message_placeholder** | **str** |  | [optional] 
**chatbot_header_text** | **str** |  | [optional] 
**chatbot_header_logo_url** | **str** |  | [optional] 
**assistant_avatar_image_url** | **str** |  | [optional] 
**remove_branding** | **bool** |  | [optional] 
**chatbot_style** | **str** |  | [optional] 
**session_message_history** | **bool** |  | [optional] 
**chatbot_bubble_size** | **int** |  | [optional] 
**message_header_logo_url** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.chatbot_update_request import ChatbotUpdateRequest

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


