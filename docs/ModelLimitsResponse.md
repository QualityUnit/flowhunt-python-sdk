# ModelLimitsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_outputs** | **int** |  | [optional] [default to 1]
**step_options** | **List[int]** |  | [optional] 
**guidance_options** | **List[int]** |  | [optional] 
**duration_options** | **List[int]** |  | [optional] 
**default_steps** | **int** |  | [optional] 
**min_steps** | **int** |  | [optional] 
**max_steps** | **int** |  | [optional] 
**max_reference_images** | **int** |  | [optional] [default to 10]
**resolution_type** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.model_limits_response import ModelLimitsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelLimitsResponse from a JSON string
model_limits_response_instance = ModelLimitsResponse.from_json(json)
# print the JSON string representation of the object
print(ModelLimitsResponse.to_json())

# convert the object into a dict
model_limits_response_dict = model_limits_response_instance.to_dict()
# create an instance of ModelLimitsResponse from a dict
model_limits_response_from_dict = ModelLimitsResponse.from_dict(model_limits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


