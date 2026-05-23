# SuggestionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Suggestion index | 
**question** | **str** | Suggested question text | 
**icon** | **str** | Emoji or icon name | [optional] 

## Example

```python
from flowhunt.models.suggestion_response import SuggestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestionResponse from a JSON string
suggestion_response_instance = SuggestionResponse.from_json(json)
# print the JSON string representation of the object
print(SuggestionResponse.to_json())

# convert the object into a dict
suggestion_response_dict = suggestion_response_instance.to_dict()
# create an instance of SuggestionResponse from a dict
suggestion_response_from_dict = SuggestionResponse.from_dict(suggestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


