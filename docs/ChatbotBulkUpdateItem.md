# ChatbotBulkUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatbot_id** | **str** |  | 
**status** | [**ChatbotStatus**](ChatbotStatus.md) |  | [optional] 

## Example

```python
from flowhunt.models.chatbot_bulk_update_item import ChatbotBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotBulkUpdateItem from a JSON string
chatbot_bulk_update_item_instance = ChatbotBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(ChatbotBulkUpdateItem.to_json())

# convert the object into a dict
chatbot_bulk_update_item_dict = chatbot_bulk_update_item_instance.to_dict()
# create an instance of ChatbotBulkUpdateItem from a dict
chatbot_bulk_update_item_from_dict = ChatbotBulkUpdateItem.from_dict(chatbot_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


