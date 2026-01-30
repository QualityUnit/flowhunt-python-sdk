# FlowValidationError

Single flow validation error with node context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | ID of the node with the error | 
**component_type** | **str** | Type of the component | [optional] 
**param_name** | **str** | The parameter that failed validation | 
**error_level** | **str** | Severity level of the validation issue | [optional] [default to 'error']
**message** | **str** | Human-readable error message | 

## Example

```python
from flowhunt.models.flow_validation_error import FlowValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of FlowValidationError from a JSON string
flow_validation_error_instance = FlowValidationError.from_json(json)
# print the JSON string representation of the object
print(FlowValidationError.to_json())

# convert the object into a dict
flow_validation_error_dict = flow_validation_error_instance.to_dict()
# create an instance of FlowValidationError from a dict
flow_validation_error_from_dict = FlowValidationError.from_dict(flow_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


