# PromptUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name | [optional] 
**description** | **str** | Document description | [optional] 
**prompt_text** | **str** | Prompt text | [optional] 
**prompt_url** | [**AppUrlInput**](AppUrlInput.md) | Prompt URL | [optional] 
**cat_id** | **str** | Category ID | [optional] 

## Example

```python
from flowhunt.models.prompt_update_request import PromptUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptUpdateRequest from a JSON string
prompt_update_request_instance = PromptUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PromptUpdateRequest.to_json())

# convert the object into a dict
prompt_update_request_dict = prompt_update_request_instance.to_dict()
# create an instance of PromptUpdateRequest from a dict
prompt_update_request_from_dict = PromptUpdateRequest.from_dict(prompt_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


