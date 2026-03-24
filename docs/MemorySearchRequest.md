# MemorySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | [optional] 
**query** | **str** | Search query | [optional] 
**search_method** | [**SearchType**](SearchType.md) | Search method | [optional] 
**depth** | **int** | The depth of the search | [optional] [default to 1]

## Example

```python
from flowhunt.models.memory_search_request import MemorySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySearchRequest from a JSON string
memory_search_request_instance = MemorySearchRequest.from_json(json)
# print the JSON string representation of the object
print(MemorySearchRequest.to_json())

# convert the object into a dict
memory_search_request_dict = memory_search_request_instance.to_dict()
# create an instance of MemorySearchRequest from a dict
memory_search_request_from_dict = MemorySearchRequest.from_dict(memory_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


