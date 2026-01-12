# MemorySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Node ID | 
**name** | **str** | Node title | [optional] 
**path** | **str** | Node path in hierarchy | [optional] 
**parent_id** | **str** | Parent node ID | [optional] 
**children** | [**List[MemorySearchResponse]**](MemorySearchResponse.md) | Child nodes | [optional] [default to []]

## Example

```python
from flowhunt.models.memory_search_response import MemorySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySearchResponse from a JSON string
memory_search_response_instance = MemorySearchResponse.from_json(json)
# print the JSON string representation of the object
print(MemorySearchResponse.to_json())

# convert the object into a dict
memory_search_response_dict = memory_search_response_instance.to_dict()
# create an instance of MemorySearchResponse from a dict
memory_search_response_from_dict = MemorySearchResponse.from_dict(memory_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


