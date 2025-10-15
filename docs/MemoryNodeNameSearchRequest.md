# MemoryNodeNameSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**depth** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.memory_node_name_search_request import MemoryNodeNameSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryNodeNameSearchRequest from a JSON string
memory_node_name_search_request_instance = MemoryNodeNameSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MemoryNodeNameSearchRequest.to_json())

# convert the object into a dict
memory_node_name_search_request_dict = memory_node_name_search_request_instance.to_dict()
# create an instance of MemoryNodeNameSearchRequest from a dict
memory_node_name_search_request_from_dict = MemoryNodeNameSearchRequest.from_dict(memory_node_name_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


