# GridResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**grid_id** | **str** | Grid ID | 
**title** | **str** | Title of the grid | 
**status** | [**GridStatus**](GridStatus.md) | Status of the grid (F - Finished, R - Running, E - Error, P - Paused) | 
**modified** | **datetime** | Modified date of the grid | 

## Example

```python
from flowhunt.models.grid_response import GridResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GridResponse from a JSON string
grid_response_instance = GridResponse.from_json(json)
# print the JSON string representation of the object
print(GridResponse.to_json())

# convert the object into a dict
grid_response_dict = grid_response_instance.to_dict()
# create an instance of GridResponse from a dict
grid_response_from_dict = GridResponse.from_dict(grid_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


