# MemoryNodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Node ID | 
**node_type** | [**NodeType**](NodeType.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.memory_node_response import MemoryNodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryNodeResponse from a JSON string
memory_node_response_instance = MemoryNodeResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryNodeResponse.to_json())

# convert the object into a dict
memory_node_response_dict = memory_node_response_instance.to_dict()
# create an instance of MemoryNodeResponse from a dict
memory_node_response_from_dict = MemoryNodeResponse.from_dict(memory_node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


