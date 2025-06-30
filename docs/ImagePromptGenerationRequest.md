# ImagePromptGenerationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_prompt** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.image_prompt_generation_request import ImagePromptGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromptGenerationRequest from a JSON string
image_prompt_generation_request_instance = ImagePromptGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(ImagePromptGenerationRequest.to_json())

# convert the object into a dict
image_prompt_generation_request_dict = image_prompt_generation_request_instance.to_dict()
# create an instance of ImagePromptGenerationRequest from a dict
image_prompt_generation_request_from_dict = ImagePromptGenerationRequest.from_dict(image_prompt_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


