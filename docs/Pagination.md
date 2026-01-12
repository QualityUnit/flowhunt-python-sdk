# Pagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sorting_key_value** | **str** | Sorting key value | [optional] 
**scroll_id** | **str** | Scroll ID for pagination | [optional] 

## Example

```python
from flowhunt.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


