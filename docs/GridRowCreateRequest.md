# GridRowCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the grid cell | 

## Example

```python
from flowhunt.models.grid_row_create_request import GridRowCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GridRowCreateRequest from a JSON string
grid_row_create_request_instance = GridRowCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GridRowCreateRequest.to_json())

# convert the object into a dict
grid_row_create_request_dict = grid_row_create_request_instance.to_dict()
# create an instance of GridRowCreateRequest from a dict
grid_row_create_request_from_dict = GridRowCreateRequest.from_dict(grid_row_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


