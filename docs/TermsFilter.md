# TermsFilter

Multi-value filter — emits an ES ``terms`` query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] [default to 'terms']
**values** | **List[object]** | Set of allowed values (any-of) | 

## Example

```python
from flowhunt.models.terms_filter import TermsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TermsFilter from a JSON string
terms_filter_instance = TermsFilter.from_json(json)
# print the JSON string representation of the object
print(TermsFilter.to_json())

# convert the object into a dict
terms_filter_dict = terms_filter_instance.to_dict()
# create an instance of TermsFilter from a dict
terms_filter_from_dict = TermsFilter.from_dict(terms_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


