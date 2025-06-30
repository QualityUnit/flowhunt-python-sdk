# ChatbotSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from flowhunt.models.chatbot_search_request import ChatbotSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatbotSearchRequest from a JSON string
chatbot_search_request_instance = ChatbotSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ChatbotSearchRequest.to_json())

# convert the object into a dict
chatbot_search_request_dict = chatbot_search_request_instance.to_dict()
# create an instance of ChatbotSearchRequest from a dict
chatbot_search_request_from_dict = ChatbotSearchRequest.from_dict(chatbot_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


