# MemoryMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message | 

## Example

```python
from flowhunt.models.memory_message_response import MemoryMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryMessageResponse from a JSON string
memory_message_response_instance = MemoryMessageResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryMessageResponse.to_json())

# convert the object into a dict
memory_message_response_dict = memory_message_response_instance.to_dict()
# create an instance of MemoryMessageResponse from a dict
memory_message_response_from_dict = MemoryMessageResponse.from_dict(memory_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


