# PromptCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | 
**name** | **str** | Document name | 
**description** | **str** | Document description | [optional] 
**prompt_text** | **str** | Prompt text | 
**prompt_url** | [**AppUrlInput**](AppUrlInput.md) | Prompt URL | [optional] 

## Example

```python
from flowhunt.models.prompt_create_request import PromptCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptCreateRequest from a JSON string
prompt_create_request_instance = PromptCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PromptCreateRequest.to_json())

# convert the object into a dict
prompt_create_request_dict = prompt_create_request_instance.to_dict()
# create an instance of PromptCreateRequest from a dict
prompt_create_request_from_dict = PromptCreateRequest.from_dict(prompt_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


