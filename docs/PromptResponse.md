# PromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_id** | **str** | Prompt ID | 
**cat_id** | **str** | Category ID | 
**workspace_id** | **str** | Workspace ID | 
**name** | **str** | Prompt name | 
**description** | **str** |  | [optional] 
**prompt_text** | **str** | Prompt text | 
**prompt_url** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.prompt_response import PromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptResponse from a JSON string
prompt_response_instance = PromptResponse.from_json(json)
# print the JSON string representation of the object
print(PromptResponse.to_json())

# convert the object into a dict
prompt_response_dict = prompt_response_instance.to_dict()
# create an instance of PromptResponse from a dict
prompt_response_from_dict = PromptResponse.from_dict(prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


