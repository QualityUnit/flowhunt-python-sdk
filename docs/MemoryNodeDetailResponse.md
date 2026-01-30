# MemoryNodeDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Node ID | 
**cat_id** | **str** | Category ID | [optional] 
**depth** | **int** | Node depth in hierarchy | [optional] 
**title** | **str** | Node title | [optional] 
**body** | **str** | Node content body | [optional] 
**path** | **str** | Node path in hierarchy | [optional] 
**offload_ids** | **List[str]** | List of offload IDs for original source content | [optional] 
**sources** | [**List[Source]**](Source.md) | List of source references | [optional] 

## Example

```python
from flowhunt.models.memory_node_detail_response import MemoryNodeDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryNodeDetailResponse from a JSON string
memory_node_detail_response_instance = MemoryNodeDetailResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryNodeDetailResponse.to_json())

# convert the object into a dict
memory_node_detail_response_dict = memory_node_detail_response_instance.to_dict()
# create an instance of MemoryNodeDetailResponse from a dict
memory_node_detail_response_from_dict = MemoryNodeDetailResponse.from_dict(memory_node_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


