# FlowBatchRowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** |  | 
**batch_run_id** | **str** |  | 
**row_index** | **int** |  | 
**input_data** | **Dict[str, object]** |  | 
**status** | [**FlowBatchRowStatus**](FlowBatchRowStatus.md) |  | 
**output** | **str** |  | [optional] 
**output_artefacts** | [**List[FlowBatchArtefactInfo]**](FlowBatchArtefactInfo.md) |  | [optional] 
**error** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**credits_used** | **float** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.flow_batch_row_response import FlowBatchRowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchRowResponse from a JSON string
flow_batch_row_response_instance = FlowBatchRowResponse.from_json(json)
# print the JSON string representation of the object
print(FlowBatchRowResponse.to_json())

# convert the object into a dict
flow_batch_row_response_dict = flow_batch_row_response_instance.to_dict()
# create an instance of FlowBatchRowResponse from a dict
flow_batch_row_response_from_dict = FlowBatchRowResponse.from_dict(flow_batch_row_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


