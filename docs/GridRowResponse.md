# GridRowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**grid_id** | **str** | Grid ID | 
**row_id** | **str** | Row ID | 
**created** | **float** | Created timestamp | 
**cells** | [**List[GrigCell]**](GrigCell.md) |  | [optional] 

## Example

```python
from flowhunt.models.grid_row_response import GridRowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GridRowResponse from a JSON string
grid_row_response_instance = GridRowResponse.from_json(json)
# print the JSON string representation of the object
print(GridRowResponse.to_json())

# convert the object into a dict
grid_row_response_dict = grid_row_response_instance.to_dict()
# create an instance of GridRowResponse from a dict
grid_row_response_from_dict = GridRowResponse.from_dict(grid_row_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


