# OllamaListModelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_base_url** | **str** |  | 

## Example

```python
from flowhunt.models.ollama_list_models_request import OllamaListModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OllamaListModelsRequest from a JSON string
ollama_list_models_request_instance = OllamaListModelsRequest.from_json(json)
# print the JSON string representation of the object
print(OllamaListModelsRequest.to_json())

# convert the object into a dict
ollama_list_models_request_dict = ollama_list_models_request_instance.to_dict()
# create an instance of OllamaListModelsRequest from a dict
ollama_list_models_request_from_dict = OllamaListModelsRequest.from_dict(ollama_list_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


