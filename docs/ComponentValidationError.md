# ComponentValidationError

Single component validation error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**param_name** | **str** | The parameter that failed validation | 
**error_level** | **str** | Severity level of the validation issue | [optional] [default to 'error']
**message** | **str** | Human-readable error message | 

## Example

```python
from flowhunt.models.component_validation_error import ComponentValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentValidationError from a JSON string
component_validation_error_instance = ComponentValidationError.from_json(json)
# print the JSON string representation of the object
print(ComponentValidationError.to_json())

# convert the object into a dict
component_validation_error_dict = component_validation_error_instance.to_dict()
# create an instance of ComponentValidationError from a dict
component_validation_error_from_dict = ComponentValidationError.from_dict(component_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


