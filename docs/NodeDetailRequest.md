# NodeDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | [optional] 
**parent_node_id** | **str** | Parent node ID | [optional] 
**title** | **str** | Node title | [optional] 
**body** | **str** | Node content body | [optional] 
**position** | **int** | Position among siblings | [optional] [default to 0]
**sources** | [**List[Source]**](Source.md) | List of source IDs | [optional] 

## Example

```python
from flowhunt.models.node_detail_request import NodeDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDetailRequest from a JSON string
node_detail_request_instance = NodeDetailRequest.from_json(json)
# print the JSON string representation of the object
print(NodeDetailRequest.to_json())

# convert the object into a dict
node_detail_request_dict = node_detail_request_instance.to_dict()
# create an instance of NodeDetailRequest from a dict
node_detail_request_from_dict = NodeDetailRequest.from_dict(node_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


