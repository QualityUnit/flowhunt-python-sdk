# FlowSessionVariablesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_variables** | **Dict[str, object]** | Variables to merge into the session | 

## Example

```python
from flowhunt.models.flow_session_variables_request import FlowSessionVariablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionVariablesRequest from a JSON string
flow_session_variables_request_instance = FlowSessionVariablesRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionVariablesRequest.to_json())

# convert the object into a dict
flow_session_variables_request_dict = flow_session_variables_request_instance.to_dict()
# create an instance of FlowSessionVariablesRequest from a dict
flow_session_variables_request_from_dict = FlowSessionVariablesRequest.from_dict(flow_session_variables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


