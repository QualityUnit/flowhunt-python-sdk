# WordPressSiteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | Integration ID | 
**site_url** | **str** | Site URL | 
**name** | **str** |  | 
**home** | **str** |  | 

## Example

```python
from flowhunt.models.word_press_site_response import WordPressSiteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressSiteResponse from a JSON string
word_press_site_response_instance = WordPressSiteResponse.from_json(json)
# print the JSON string representation of the object
print(WordPressSiteResponse.to_json())

# convert the object into a dict
word_press_site_response_dict = word_press_site_response_instance.to_dict()
# create an instance of WordPressSiteResponse from a dict
word_press_site_response_from_dict = WordPressSiteResponse.from_dict(word_press_site_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


