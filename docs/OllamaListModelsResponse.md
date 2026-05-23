# OllamaListModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** |  | 

## Example

```python
from flowhunt.models.ollama_list_models_response import OllamaListModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OllamaListModelsResponse from a JSON string
ollama_list_models_response_instance = OllamaListModelsResponse.from_json(json)
# print the JSON string representation of the object
print(OllamaListModelsResponse.to_json())

# convert the object into a dict
ollama_list_models_response_dict = ollama_list_models_response_instance.to_dict()
# create an instance of OllamaListModelsResponse from a dict
ollama_list_models_response_from_dict = OllamaListModelsResponse.from_dict(ollama_list_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


