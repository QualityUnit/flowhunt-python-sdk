# DeleteNodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | [optional] 

## Example

```python
from flowhunt.models.delete_node_request import DeleteNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNodeRequest from a JSON string
delete_node_request_instance = DeleteNodeRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteNodeRequest.to_json())

# convert the object into a dict
delete_node_request_dict = delete_node_request_instance.to_dict()
# create an instance of DeleteNodeRequest from a dict
delete_node_request_from_dict = DeleteNodeRequest.from_dict(delete_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


