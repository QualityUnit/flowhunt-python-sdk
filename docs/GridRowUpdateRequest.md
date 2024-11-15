# GridRowUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**data_type** | [**ColumnDataType**](ColumnDataType.md) |  | [optional] 
**data_type_options** | **str** |  | [optional] 
**input_columns** | **List[str]** |  | [optional] 
**executor_type** | [**ColumnExecutorType**](ColumnExecutorType.md) |  | [optional] 
**executor_flow_id** | **str** |  | [optional] 
**executor_input_template** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.grid_row_update_request import GridRowUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GridRowUpdateRequest from a JSON string
grid_row_update_request_instance = GridRowUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GridRowUpdateRequest.to_json())

# convert the object into a dict
grid_row_update_request_dict = grid_row_update_request_instance.to_dict()
# create an instance of GridRowUpdateRequest from a dict
grid_row_update_request_from_dict = GridRowUpdateRequest.from_dict(grid_row_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


