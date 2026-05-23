# CustomModelUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**api_base_url** | **str** |  | [optional] 
**model_id** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**compatibility** | [**CustomModelCompatibility**](CustomModelCompatibility.md) |  | [optional] 
**provider** | [**CustomModelProvider**](CustomModelProvider.md) |  | [optional] 
**reasoning_effort** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.custom_model_update_request import CustomModelUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModelUpdateRequest from a JSON string
custom_model_update_request_instance = CustomModelUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomModelUpdateRequest.to_json())

# convert the object into a dict
custom_model_update_request_dict = custom_model_update_request_instance.to_dict()
# create an instance of CustomModelUpdateRequest from a dict
custom_model_update_request_from_dict = CustomModelUpdateRequest.from_dict(custom_model_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


