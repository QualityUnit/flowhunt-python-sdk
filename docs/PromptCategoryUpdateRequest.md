# PromptCategoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_name** | **str** | Category name | [optional] 
**color** | **str** | Category color | [optional] 
**description** | **str** | Category description | [optional] 

## Example

```python
from flowhunt.models.prompt_category_update_request import PromptCategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptCategoryUpdateRequest from a JSON string
prompt_category_update_request_instance = PromptCategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PromptCategoryUpdateRequest.to_json())

# convert the object into a dict
prompt_category_update_request_dict = prompt_category_update_request_instance.to_dict()
# create an instance of PromptCategoryUpdateRequest from a dict
prompt_category_update_request_from_dict = PromptCategoryUpdateRequest.from_dict(prompt_category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


