# MatchFilter

Full-text match filter — emits an ES ``match`` query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] [default to 'match']
**value** | **str** |  | 
**fuzzy** | **bool** | When true, emits &#x60;&#x60;fuzziness: AUTO&#x60;&#x60; for typo-tolerant matching. | [optional] [default to True]

## Example

```python
from flowhunt.models.match_filter import MatchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFilter from a JSON string
match_filter_instance = MatchFilter.from_json(json)
# print the JSON string representation of the object
print(MatchFilter.to_json())

# convert the object into a dict
match_filter_dict = match_filter_instance.to_dict()
# create an instance of MatchFilter from a dict
match_filter_from_dict = MatchFilter.from_dict(match_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


