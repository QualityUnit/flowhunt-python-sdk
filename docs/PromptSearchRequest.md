# PromptSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_id** | **str** | Prompt ID | [optional] 
**cat_id** | **str** | Category ID | [optional] 
**name** | **str** | Prompt name | [optional] 
**description** | **str** | Prompt description | [optional] 
**prompt_text** | **str** | Prompt text | [optional] 
**prompt_url** | **str** | Prompt URL | [optional] 
**limit** | **int** | Limit | [optional] [default to 100]

## Example

```python
from flowhunt.models.prompt_search_request import PromptSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSearchRequest from a JSON string
prompt_search_request_instance = PromptSearchRequest.from_json(json)
# print the JSON string representation of the object
print(PromptSearchRequest.to_json())

# convert the object into a dict
prompt_search_request_dict = prompt_search_request_instance.to_dict()
# create an instance of PromptSearchRequest from a dict
prompt_search_request_from_dict = PromptSearchRequest.from_dict(prompt_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


