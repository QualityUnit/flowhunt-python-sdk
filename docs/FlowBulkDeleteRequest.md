# FlowBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.flow_bulk_delete_request import FlowBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBulkDeleteRequest from a JSON string
flow_bulk_delete_request_instance = FlowBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBulkDeleteRequest.to_json())

# convert the object into a dict
flow_bulk_delete_request_dict = flow_bulk_delete_request_instance.to_dict()
# create an instance of FlowBulkDeleteRequest from a dict
flow_bulk_delete_request_from_dict = FlowBulkDeleteRequest.from_dict(flow_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


