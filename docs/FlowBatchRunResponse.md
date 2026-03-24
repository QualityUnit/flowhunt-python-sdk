# FlowBatchRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_run_id** | **str** |  | 
**flow_id** | **str** |  | 
**workspace_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**columns** | [**List[FlowBatchColumnDefinition]**](FlowBatchColumnDefinition.md) |  | [optional] 
**max_parallel** | **int** |  | 
**status** | [**FlowBatchRunStatus**](FlowBatchRunStatus.md) |  | 
**total_rows** | **int** |  | 
**completed_rows** | **int** |  | 
**failed_rows** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.flow_batch_run_response import FlowBatchRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRunResponse from a JSON string
flow_batch_run_response_instance = FlowBatchRunResponse.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRunResponse.to_json())

# convert the object into a dict
flow_batch_run_response_dict = flow_batch_run_response_instance.to_dict()
# create an instance of FlowBatchRunResponse from a dict
flow_batch_run_response_from_dict = FlowBatchRunResponse.from_dict(flow_batch_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


