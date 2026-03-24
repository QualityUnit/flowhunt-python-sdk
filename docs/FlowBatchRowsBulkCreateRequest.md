# FlowBatchRowsBulkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[FlowBatchRowCreateRequest]**](FlowBatchRowCreateRequest.md) | Rows to add | 

## Example

```python
from flowhunt.models.flow_batch_rows_bulk_create_request import FlowBatchRowsBulkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRowsBulkCreateRequest from a JSON string
flow_batch_rows_bulk_create_request_instance = FlowBatchRowsBulkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRowsBulkCreateRequest.to_json())

# convert the object into a dict
flow_batch_rows_bulk_create_request_dict = flow_batch_rows_bulk_create_request_instance.to_dict()
# create an instance of FlowBatchRowsBulkCreateRequest from a dict
flow_batch_rows_bulk_create_request_from_dict = FlowBatchRowsBulkCreateRequest.from_dict(flow_batch_rows_bulk_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


