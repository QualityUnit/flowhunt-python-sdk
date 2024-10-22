# PromptCategoryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_name** | **str** | Category name | 
**color** | **str** | Category color | 
**description** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.prompt_category_create_request import PromptCategoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptCategoryCreateRequest from a JSON string
prompt_category_create_request_instance = PromptCategoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PromptCategoryCreateRequest.to_json())

# convert the object into a dict
prompt_category_create_request_dict = prompt_category_create_request_instance.to_dict()
# create an instance of PromptCategoryCreateRequest from a dict
prompt_category_create_request_from_dict = PromptCategoryCreateRequest.from_dict(prompt_category_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


