# FiltersValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] [default to 'range']
**value** | **str** |  | 
**values** | **List[object]** | Set of allowed values (any-of) | 
**fuzzy** | **bool** | When true, emits &#x60;&#x60;fuzziness: AUTO&#x60;&#x60; for typo-tolerant matching. | [optional] [default to True]
**gte** | **object** |  | [optional] 
**lte** | **object** |  | [optional] 

## Example

```python
from flowhunt.models.filters_value import FiltersValue

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersValue from a JSON string
filters_value_instance = FiltersValue.from_json(json)
# print the JSON string representation of the object
print(FiltersValue.to_json())

# convert the object into a dict
filters_value_dict = filters_value_instance.to_dict()
# create an instance of FiltersValue from a dict
filters_value_from_dict = FiltersValue.from_dict(filters_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


