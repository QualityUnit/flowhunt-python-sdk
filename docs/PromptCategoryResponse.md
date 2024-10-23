# PromptCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**cat_id** | **str** | Category ID | 
**cat_name** | **str** | Category name | 
**color** | **str** | Category color | 
**description** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.prompt_category_response import PromptCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptCategoryResponse from a JSON string
prompt_category_response_instance = PromptCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(PromptCategoryResponse.to_json())

# convert the object into a dict
prompt_category_response_dict = prompt_category_response_instance.to_dict()
# create an instance of PromptCategoryResponse from a dict
prompt_category_response_from_dict = PromptCategoryResponse.from_dict(prompt_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


