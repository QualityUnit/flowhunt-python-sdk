# ModelCapabilitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_loras** | **bool** |  | [optional] [default to False]
**supports_guidance** | **bool** |  | [optional] [default to False]
**supports_cfg** | **bool** |  | [optional] [default to False]
**supports_steps** | **bool** |  | [optional] [default to False]
**supports_multiple_outputs** | **bool** |  | [optional] [default to False]
**supports_aspect_ratio** | **bool** |  | [optional] [default to True]
**supports_characters** | **bool** |  | [optional] [default to False]
**supports_resolution** | **bool** |  | [optional] [default to False]
**supports_duration** | **bool** |  | [optional] [default to False]
**supports_audio** | **bool** |  | [optional] [default to False]
**supports_reference_images** | **bool** |  | [optional] [default to False]
**supports_reference_videos** | **bool** |  | [optional] [default to False]
**supports_start_image** | **bool** |  | [optional] [default to False]
**supports_last_image** | **bool** |  | [optional] [default to False]
**supports_prompt** | **bool** |  | [optional] [default to True]
**supports_size** | **bool** |  | [optional] [default to False]
**requires_reference_images** | **bool** |  | [optional] [default to False]
**requires_reference_videos** | **bool** |  | [optional] [default to False]

## Example

```python
from flowhunt.models.model_capabilities_response import ModelCapabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCapabilitiesResponse from a JSON string
model_capabilities_response_instance = ModelCapabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCapabilitiesResponse.to_json())

# convert the object into a dict
model_capabilities_response_dict = model_capabilities_response_instance.to_dict()
# create an instance of ModelCapabilitiesResponse from a dict
model_capabilities_response_from_dict = ModelCapabilitiesResponse.from_dict(model_capabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


