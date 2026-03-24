# ComponentValidationResponse

Response from component validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | Whether the component config is valid | 
**errors** | [**List[ComponentValidationError]**](ComponentValidationError.md) | List of validation errors/warnings | [optional] 

## Example

```python
from flowhunt.models.component_validation_response import ComponentValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentValidationResponse from a JSON string
component_validation_response_instance = ComponentValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ComponentValidationResponse.to_json())

# convert the object into a dict
component_validation_response_dict = component_validation_response_instance.to_dict()
# create an instance of ComponentValidationResponse from a dict
component_validation_response_from_dict = ComponentValidationResponse.from_dict(component_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


