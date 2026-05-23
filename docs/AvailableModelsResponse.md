# AvailableModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grouped_options** | **Dict[str, List[str]]** |  | 
**custom_model_labels** | **Dict[str, str]** |  | 
**custom_model_families** | [**Dict[str, CustomModelFamily]**](CustomModelFamily.md) |  | 

## Example

```python
from flowhunt.models.available_models_response import AvailableModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableModelsResponse from a JSON string
available_models_response_instance = AvailableModelsResponse.from_json(json)
# print the JSON string representation of the object
print(AvailableModelsResponse.to_json())

# convert the object into a dict
available_models_response_dict = available_models_response_instance.to_dict()
# create an instance of AvailableModelsResponse from a dict
available_models_response_from_dict = AvailableModelsResponse.from_dict(available_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


