# FlowValidationResponse

Response from flow-wide validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | Whether the entire flow is valid | 
**errors** | [**List[FlowValidationError]**](FlowValidationError.md) | List of validation errors across all nodes | [optional] 

## Example

```python
from flowhunt.models.flow_validation_response import FlowValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowValidationResponse from a JSON string
flow_validation_response_instance = FlowValidationResponse.from_json(json)
# print the JSON string representation of the object
print(FlowValidationResponse.to_json())

# convert the object into a dict
flow_validation_response_dict = flow_validation_response_instance.to_dict()
# create an instance of FlowValidationResponse from a dict
flow_validation_response_from_dict = FlowValidationResponse.from_dict(flow_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


