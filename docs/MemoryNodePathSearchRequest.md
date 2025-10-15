# MemoryNodePathSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** |  | [optional] 
**node_path** | **str** |  | [optional] 
**depth** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.memory_node_path_search_request import MemoryNodePathSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryNodePathSearchRequest from a JSON string
memory_node_path_search_request_instance = MemoryNodePathSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MemoryNodePathSearchRequest.to_json())

# convert the object into a dict
memory_node_path_search_request_dict = memory_node_path_search_request_instance.to_dict()
# create an instance of MemoryNodePathSearchRequest from a dict
memory_node_path_search_request_from_dict = MemoryNodePathSearchRequest.from_dict(memory_node_path_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


