# WordPressCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | 
**link** | **str** |  | 
**parent** | **int** |  | 
**count** | **int** |  | 

## Example

```python
from flowhunt.models.word_press_category_response import WordPressCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressCategoryResponse from a JSON string
word_press_category_response_instance = WordPressCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(WordPressCategoryResponse.to_json())

# convert the object into a dict
word_press_category_response_dict = word_press_category_response_instance.to_dict()
# create an instance of WordPressCategoryResponse from a dict
word_press_category_response_from_dict = WordPressCategoryResponse.from_dict(word_press_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


