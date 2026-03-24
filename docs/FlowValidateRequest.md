# FlowValidateRequest

Request to validate an entire V3 flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[FlowNode]**](FlowNode.md) | List of nodes to validate | 

## Example

```python
from flowhunt.models.flow_validate_request import FlowValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowValidateRequest from a JSON string
flow_validate_request_instance = FlowValidateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowValidateRequest.to_json())

# convert the object into a dict
flow_validate_request_dict = flow_validate_request_instance.to_dict()
# create an instance of FlowValidateRequest from a dict
flow_validate_request_from_dict = FlowValidateRequest.from_dict(flow_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


