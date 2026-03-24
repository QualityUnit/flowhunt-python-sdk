# FlowBatchRunUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Batch run name | [optional] 
**columns** | [**List[FlowBatchColumnDefinition]**](FlowBatchColumnDefinition.md) | Column definitions | [optional] 
**max_parallel** | **int** | Max concurrent row executions | [optional] 

## Example

```python
from flowhunt.models.flow_batch_run_update_request import FlowBatchRunUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRunUpdateRequest from a JSON string
flow_batch_run_update_request_instance = FlowBatchRunUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRunUpdateRequest.to_json())

# convert the object into a dict
flow_batch_run_update_request_dict = flow_batch_run_update_request_instance.to_dict()
# create an instance of FlowBatchRunUpdateRequest from a dict
flow_batch_run_update_request_from_dict = FlowBatchRunUpdateRequest.from_dict(flow_batch_run_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


