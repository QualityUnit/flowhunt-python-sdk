# NodeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | [optional] 
**title** | **str** | Node title | [optional] 
**body** | **str** | Node content body | [optional] 
**appended_offload_id** | **str** | Offload ID to append to the node&#39;s sources list | [optional] 

## Example

```python
from flowhunt.models.node_update_request import NodeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeUpdateRequest from a JSON string
node_update_request_instance = NodeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NodeUpdateRequest.to_json())

# convert the object into a dict
node_update_request_dict = node_update_request_instance.to_dict()
# create an instance of NodeUpdateRequest from a dict
node_update_request_from_dict = NodeUpdateRequest.from_dict(node_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


