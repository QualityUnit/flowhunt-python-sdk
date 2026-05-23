# ModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**category** | **str** |  | 
**model_type** | **str** |  | 
**icon_hint** | **str** |  | 
**available_in_flow_v3** | **bool** |  | 
**capabilities** | [**ModelCapabilitiesResponse**](ModelCapabilitiesResponse.md) |  | 
**limits** | [**ModelLimitsResponse**](ModelLimitsResponse.md) |  | 

## Example

```python
from flowhunt.models.model_response import ModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelResponse from a JSON string
model_response_instance = ModelResponse.from_json(json)
# print the JSON string representation of the object
print(ModelResponse.to_json())

# convert the object into a dict
model_response_dict = model_response_instance.to_dict()
# create an instance of ModelResponse from a dict
model_response_from_dict = ModelResponse.from_dict(model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


