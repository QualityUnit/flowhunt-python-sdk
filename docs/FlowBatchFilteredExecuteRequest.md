# FlowBatchFilteredExecuteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rerun_all** | **bool** | If True, reset matching completed/failed rows to pending before running | [optional] [default to False]
**max_concurrency** | **int** | Override max_parallel for this execution (capped by plan limit) | [optional] 

## Example

```python
from flowhunt.models.flow_batch_filtered_execute_request import FlowBatchFilteredExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchFilteredExecuteRequest from a JSON string
flow_batch_filtered_execute_request_instance = FlowBatchFilteredExecuteRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchFilteredExecuteRequest.to_json())

# convert the object into a dict
flow_batch_filtered_execute_request_dict = flow_batch_filtered_execute_request_instance.to_dict()
# create an instance of FlowBatchFilteredExecuteRequest from a dict
flow_batch_filtered_execute_request_from_dict = FlowBatchFilteredExecuteRequest.from_dict(flow_batch_filtered_execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


