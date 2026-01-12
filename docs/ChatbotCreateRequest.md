# ChatbotCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**flow_id** | **str** | Chatbot Agent ID | [optional] 
**status** | [**ChatbotStatus**](ChatbotStatus.md) |  | 
**url_suffix** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**max_window_size** | **str** |  | [optional] 
**msg_rpm** | **int** | Rate limit number of message per hour | [optional] 
**msg_ip_rpm** | **int** | Rate limit number of message per hour from the same IP | [optional] 
**ratelimit_msg** | **str** | Custom message to display when rate limit is exceeded | [optional] 
**chatbot_description** | **str** | A description of the chatbot | [optional] 
**show_chatbot_header** | **bool** | Whether to show the chatbot header | [optional] [default to True]
**chat_bubble_bg_color** | **str** | Background color of chat bubble in hexadecimal | [optional] 
**chat_bubble_icon_color** | **str** | Icon color of chat bubble in hexadecimal | [optional] 
**chat_bubble_img_url** | **str** | URL to load the chat bubble image | [optional] 
**chatbot_theme** | **str** | Chatbot theme (light or dark) | [optional] 
**chatbot_position** | **str** | Chatbot position (BR, BL, TR, TL) | [optional] [default to 'BR']
**text_direction** | **str** | Text direction (A&#x3D;Auto, L&#x3D;LTR, R&#x3D;RTL) | [optional] [default to 'A']
**message_placeholder** | **str** | Placeholder text for message input | [optional] 
**chatbot_header_text** | **str** | Text displayed in chatbot header | [optional] 
**chatbot_header_logo_url** | **str** | URL for the chatbot header logo | [optional] 
**assistant_avatar_image_url** | **str** | URL for the assistant avatar image | [optional] 
**remove_branding** | **bool** | Whether to remove FlowHunt branding from the chatbot | [optional] [default to False]
**chatbot_style** | **str** | Chatbot style (default or custom) | [optional] 
**session_message_history** | **bool** | Session message history | [optional] [default to False]
**chatbot_bubble_size** | **int** | Chatbot bubble size | [optional] 
**message_header_logo_url** | **str** | URL for the message header logo | [optional] 
**popup_messages** | **List[str]** | List of popup markdown messages | [optional] 
**popup_messages_delay** | **int** | Delay in seconds before showing popup messages | [optional] 

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


