# CustomModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_model_id** | **str** |  | 
**name** | **str** |  | 
**api_base_url** | **str** |  | 
**model_id** | **str** |  | 
**compatibility** | [**CustomModelCompatibility**](CustomModelCompatibility.md) |  | 
**provider** | [**CustomModelProvider**](CustomModelProvider.md) |  | 
**model_family** | [**CustomModelFamily**](CustomModelFamily.md) |  | [optional] 
**reasoning_effort** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from flowhunt.models.custom_model_response import CustomModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModelResponse from a JSON string
custom_model_response_instance = CustomModelResponse.from_json(json)
# print the JSON string representation of the object
print(CustomModelResponse.to_json())

# convert the object into a dict
custom_model_response_dict = custom_model_response_instance.to_dict()
# create an instance of CustomModelResponse from a dict
custom_model_response_from_dict = CustomModelResponse.from_dict(custom_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


