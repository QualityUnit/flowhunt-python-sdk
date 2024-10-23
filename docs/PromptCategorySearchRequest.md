# PromptCategorySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** |  | [optional] 
**cat_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.prompt_category_search_request import PromptCategorySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptCategorySearchRequest from a JSON string
prompt_category_search_request_instance = PromptCategorySearchRequest.from_json(json)
# print the JSON string representation of the object
print(PromptCategorySearchRequest.to_json())

# convert the object into a dict
prompt_category_search_request_dict = prompt_category_search_request_instance.to_dict()
# create an instance of PromptCategorySearchRequest from a dict
prompt_category_search_request_from_dict = PromptCategorySearchRequest.from_dict(prompt_category_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


