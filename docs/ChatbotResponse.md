# ChatbotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace id | 
**chatbot_id** | **str** | Chatbot id | 
**title** | **str** | Tenant name | 
**description** | **str** | Tenant description | [optional] 
**flow_id** | **str** | Agent ID | 
**status** | [**ChatbotStatus**](ChatbotStatus.md) | Status | 
**url_suffix** | **str** | URL suffix | [optional] 
**theme** | **str** | Theme | [optional] 
**max_window_size** | **str** | Max window size | [optional] 
**msg_rpm** | **int** | Messages per minute | [optional] 
**msg_ip_rpm** | **int** | Messages per IP per minute | [optional] 
**ratelimit_msg** | **str** | Custom message to display when rate limit is exceeded | [optional] 
**chatbot_description** | **str** | A description of the chatbot | [optional] 
**show_chatbot_header** | **bool** | Whether to show the chatbot header | [optional] 
**chat_bubble_bg_color** | **str** | Background color of chat bubble in hexadecimal | [optional] 
**chat_bubble_icon_color** | **str** | Icon color of chat bubble in hexadecimal | [optional] 
**chat_bubble_img_url** | **str** | URL to load the chat bubble image | [optional] 
**chatbot_theme** | **str** | Chatbot theme (light or dark) | [optional] 
**chatbot_position** | **str** | Chatbot position (BR, BL, TR, TL) | [optional] 
**text_direction** | **str** | Text direction (A&#x3D;Auto, L&#x3D;LTR, R&#x3D;RTL) | [optional] 
**message_placeholder** | **str** | Placeholder text for message input | [optional] 
**chatbot_header_text** | **str** | Text displayed in chatbot header | [optional] 
**chatbot_header_logo_url** | **str** | URL for the chatbot header logo | [optional] 
**assistant_avatar_image_url** | **str** | URL for the assistant avatar image | [optional] 
**remove_branding** | **bool** | Whether to remove FlowHunt branding from the chatbot | [optional] 
**chatbot_style** | **str** | Chatbot style (embedded or not) | [optional] 
**session_message_history** | **bool** | Whether to show session message history | [optional] 
**chatbot_bubble_size** | **int** | Chatbot bubble size  | [optional] 
**message_header_logo_url** | **str** | URL for the message header logo | [optional] 
**popup_messages** | **List[str]** | List of popup messages | [optional] 
**popup_messages_delay** | **int** | Delay between popup messages | [optional] 

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


