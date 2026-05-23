# ChatStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Chat session ID for polling events | 
**created_at** | **str** | Timestamp (ms since epoch) for polling | 

## Example

```python
from flowhunt.models.chat_start_response import ChatStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatStartResponse from a JSON string
chat_start_response_instance = ChatStartResponse.from_json(json)
# print the JSON string representation of the object
print(ChatStartResponse.to_json())

# convert the object into a dict
chat_start_response_dict = chat_start_response_instance.to_dict()
# create an instance of ChatStartResponse from a dict
chat_start_response_from_dict = ChatStartResponse.from_dict(chat_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


