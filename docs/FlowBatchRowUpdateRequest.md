# FlowBatchRowUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_data** | **Dict[str, object]** | Updated row input data | 
**status** | [**FlowBatchRowStatus**](FlowBatchRowStatus.md) | Optionally reset row status (e.g. back to pending) | [optional] 

## Example

```python
from flowhunt.models.flow_batch_row_update_request import FlowBatchRowUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRowUpdateRequest from a JSON string
flow_batch_row_update_request_instance = FlowBatchRowUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRowUpdateRequest.to_json())

# convert the object into a dict
flow_batch_row_update_request_dict = flow_batch_row_update_request_instance.to_dict()
# create an instance of FlowBatchRowUpdateRequest from a dict
flow_batch_row_update_request_from_dict = FlowBatchRowUpdateRequest.from_dict(flow_batch_row_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


