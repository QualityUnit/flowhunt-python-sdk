# GridCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the grid | 

## Example

```python
from flowhunt.models.grid_create_request import GridCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GridCreateRequest from a JSON string
grid_create_request_instance = GridCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GridCreateRequest.to_json())

# convert the object into a dict
grid_create_request_dict = grid_create_request_instance.to_dict()
# create an instance of GridCreateRequest from a dict
grid_create_request_from_dict = GridCreateRequest.from_dict(grid_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


