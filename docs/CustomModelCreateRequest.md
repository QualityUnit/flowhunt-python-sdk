# CustomModelCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**api_base_url** | **str** |  | 
**model_id** | **str** |  | 
**api_key** | **str** |  | [optional] 
**compatibility** | [**CustomModelCompatibility**](CustomModelCompatibility.md) |  | [optional] 
**provider** | [**CustomModelProvider**](CustomModelProvider.md) |  | [optional] 
**reasoning_effort** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.custom_model_create_request import CustomModelCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModelCreateRequest from a JSON string
custom_model_create_request_instance = CustomModelCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomModelCreateRequest.to_json())

# convert the object into a dict
custom_model_create_request_dict = custom_model_create_request_instance.to_dict()
# create an instance of CustomModelCreateRequest from a dict
custom_model_create_request_from_dict = CustomModelCreateRequest.from_dict(custom_model_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


