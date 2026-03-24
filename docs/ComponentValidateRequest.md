# ComponentValidateRequest

Request to validate a V3 component configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **Dict[str, Dict[str, object]]** | Component template with parameter values. Format: {param_name: {value: any, ...}, ...} | 

## Example

```python
from flowhunt.models.component_validate_request import ComponentValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentValidateRequest from a JSON string
component_validate_request_instance = ComponentValidateRequest.from_json(json)
# print the JSON string representation of the object
print(ComponentValidateRequest.to_json())

# convert the object into a dict
component_validate_request_dict = component_validate_request_instance.to_dict()
# create an instance of ComponentValidateRequest from a dict
component_validate_request_from_dict = ComponentValidateRequest.from_dict(component_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


