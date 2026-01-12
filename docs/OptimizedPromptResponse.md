# OptimizedPromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_text** | **str** | Prompt text | 

## Example

```python
from flowhunt.models.optimized_prompt_response import OptimizedPromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizedPromptResponse from a JSON string
optimized_prompt_response_instance = OptimizedPromptResponse.from_json(json)
# print the JSON string representation of the object
print(OptimizedPromptResponse.to_json())

# convert the object into a dict
optimized_prompt_response_dict = optimized_prompt_response_instance.to_dict()
# create an instance of OptimizedPromptResponse from a dict
optimized_prompt_response_from_dict = OptimizedPromptResponse.from_dict(optimized_prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


