# FlowBatchRowCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_data** | **Dict[str, object]** | Row input data keyed by column key | [optional] 

## Example

```python
from flowhunt.models.flow_batch_row_create_request import FlowBatchRowCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRowCreateRequest from a JSON string
flow_batch_row_create_request_instance = FlowBatchRowCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRowCreateRequest.to_json())

# convert the object into a dict
flow_batch_row_create_request_dict = flow_batch_row_create_request_instance.to_dict()
# create an instance of FlowBatchRowCreateRequest from a dict
flow_batch_row_create_request_from_dict = FlowBatchRowCreateRequest.from_dict(flow_batch_row_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


