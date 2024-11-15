# GridColumnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**grid_id** | **str** | Grid ID | 
**col_id** | **str** | Column ID | 
**name** | **str** | Name of the column | 
**position** | **int** | Position of the column | 
**data_type** | [**ColumnDataType**](ColumnDataType.md) | Data type of the column | 
**data_type_options** | **str** |  | [optional] 
**input_columns** | **List[str]** |  | [optional] 
**executor_type** | [**ColumnExecutorType**](ColumnExecutorType.md) | Executor type of the column | 
**executor_flow_id** | **str** |  | [optional] 
**executor_input_template** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.grid_column_response import GridColumnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GridColumnResponse from a JSON string
grid_column_response_instance = GridColumnResponse.from_json(json)
# print the JSON string representation of the object
print(GridColumnResponse.to_json())

# convert the object into a dict
grid_column_response_dict = grid_column_response_instance.to_dict()
# create an instance of GridColumnResponse from a dict
grid_column_response_from_dict = GridColumnResponse.from_dict(grid_column_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


