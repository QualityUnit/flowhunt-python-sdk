# FlowBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FlowBulkCategoryUpdateItem]**](FlowBulkCategoryUpdateItem.md) |  | 

## Example

```python
from flowhunt.models.flow_bulk_update_request import FlowBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBulkUpdateRequest from a JSON string
flow_bulk_update_request_instance = FlowBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBulkUpdateRequest.to_json())

# convert the object into a dict
flow_bulk_update_request_dict = flow_bulk_update_request_instance.to_dict()
# create an instance of FlowBulkUpdateRequest from a dict
flow_bulk_update_request_from_dict = FlowBulkUpdateRequest.from_dict(flow_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


