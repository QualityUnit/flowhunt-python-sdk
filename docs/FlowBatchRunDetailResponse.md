# FlowBatchRunDetailResponse


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
**rows** | [**List[FlowBatchRowResponse]**](FlowBatchRowResponse.md) |  | [optional] 
**next_cursor** | **int** | row_index of the last returned row when more pages exist, or null on the final page | [optional] 

## Example

```python
from flowhunt.models.flow_batch_run_detail_response import FlowBatchRunDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRunDetailResponse from a JSON string
flow_batch_run_detail_response_instance = FlowBatchRunDetailResponse.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRunDetailResponse.to_json())

# convert the object into a dict
flow_batch_run_detail_response_dict = flow_batch_run_detail_response_instance.to_dict()
# create an instance of FlowBatchRunDetailResponse from a dict
flow_batch_run_detail_response_from_dict = FlowBatchRunDetailResponse.from_dict(flow_batch_run_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


