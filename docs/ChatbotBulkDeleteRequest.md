# ChatbotBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.chatbot_bulk_delete_request import ChatbotBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotBulkDeleteRequest from a JSON string
chatbot_bulk_delete_request_instance = ChatbotBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ChatbotBulkDeleteRequest.to_json())

# convert the object into a dict
chatbot_bulk_delete_request_dict = chatbot_bulk_delete_request_instance.to_dict()
# create an instance of ChatbotBulkDeleteRequest from a dict
chatbot_bulk_delete_request_from_dict = ChatbotBulkDeleteRequest.from_dict(chatbot_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


