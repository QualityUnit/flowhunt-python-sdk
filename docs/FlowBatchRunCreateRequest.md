# FlowBatchRunCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Batch run name | 
**columns** | [**List[FlowBatchColumnDefinition]**](FlowBatchColumnDefinition.md) | Column definitions | [optional] 
**max_parallel** | **int** | Max concurrent row executions | [optional] [default to 10]

## Example

```python
from flowhunt.models.flow_batch_run_create_request import FlowBatchRunCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRunCreateRequest from a JSON string
flow_batch_run_create_request_instance = FlowBatchRunCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRunCreateRequest.to_json())

# convert the object into a dict
flow_batch_run_create_request_dict = flow_batch_run_create_request_instance.to_dict()
# create an instance of FlowBatchRunCreateRequest from a dict
flow_batch_run_create_request_from_dict = FlowBatchRunCreateRequest.from_dict(flow_batch_run_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


