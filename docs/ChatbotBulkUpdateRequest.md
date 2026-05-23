# ChatbotBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ChatbotBulkUpdateItem]**](ChatbotBulkUpdateItem.md) |  | 

## Example

```python
from flowhunt.models.chatbot_bulk_update_request import ChatbotBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotBulkUpdateRequest from a JSON string
chatbot_bulk_update_request_instance = ChatbotBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ChatbotBulkUpdateRequest.to_json())

# convert the object into a dict
chatbot_bulk_update_request_dict = chatbot_bulk_update_request_instance.to_dict()
# create an instance of ChatbotBulkUpdateRequest from a dict
chatbot_bulk_update_request_from_dict = ChatbotBulkUpdateRequest.from_dict(chatbot_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


