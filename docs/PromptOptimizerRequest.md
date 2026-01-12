# PromptOptimizerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_text** | **str** | The prompt text to be optimized | 
**user_instructions** | **str** | Instructions for optimization | [optional] 

## Example

```python
from flowhunt.models.prompt_optimizer_request import PromptOptimizerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptOptimizerRequest from a JSON string
prompt_optimizer_request_instance = PromptOptimizerRequest.from_json(json)
# print the JSON string representation of the object
print(PromptOptimizerRequest.to_json())

# convert the object into a dict
prompt_optimizer_request_dict = prompt_optimizer_request_instance.to_dict()
# create an instance of PromptOptimizerRequest from a dict
prompt_optimizer_request_from_dict = PromptOptimizerRequest.from_dict(prompt_optimizer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


