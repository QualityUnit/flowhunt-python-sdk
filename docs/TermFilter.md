# TermFilter

Exact-match filter — emits an ES ``term`` query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] [default to 'term']
**value** | **object** |  | 

## Example

```python
from flowhunt.models.term_filter import TermFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TermFilter from a JSON string
term_filter_instance = TermFilter.from_json(json)
# print the JSON string representation of the object
print(TermFilter.to_json())

# convert the object into a dict
term_filter_dict = term_filter_instance.to_dict()
# create an instance of TermFilter from a dict
term_filter_from_dict = TermFilter.from_dict(term_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


