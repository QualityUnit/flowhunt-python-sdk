# GridSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grid_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | [**GridStatus**](GridStatus.md) |  | [optional] 
**modified** | **str** |  | [optional] 
**limit** | **int** | Limit of the search | [optional] [default to 100]

## Example

```python
from flowhunt.models.grid_search_request import GridSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GridSearchRequest from a JSON string
grid_search_request_instance = GridSearchRequest.from_json(json)
# print the JSON string representation of the object
print(GridSearchRequest.to_json())

# convert the object into a dict
grid_search_request_dict = grid_search_request_instance.to_dict()
# create an instance of GridSearchRequest from a dict
grid_search_request_from_dict = GridSearchRequest.from_dict(grid_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


