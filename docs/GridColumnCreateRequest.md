# GridColumnCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the grid column | 
**position** | **int** | Position of the grid column | 
**data_type** | [**ColumnDataType**](ColumnDataType.md) | Data type of the grid column | 
**data_type_options** | **str** |  | [optional] 
**input_columns** | **List[str]** |  | [optional] 
**executor_type** | [**ColumnExecutorType**](ColumnExecutorType.md) | Executor type of the grid column | 
**executor_flow_id** | **str** |  | [optional] 
**executor_input_template** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.grid_column_create_request import GridColumnCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GridColumnCreateRequest from a JSON string
grid_column_create_request_instance = GridColumnCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GridColumnCreateRequest.to_json())

# convert the object into a dict
grid_column_create_request_dict = grid_column_create_request_instance.to_dict()
# create an instance of GridColumnCreateRequest from a dict
grid_column_create_request_from_dict = GridColumnCreateRequest.from_dict(grid_column_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


