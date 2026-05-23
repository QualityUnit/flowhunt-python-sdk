# FlowSessionVariablesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **str** | Timestamp when variables were updated | 

## Example

```python
from flowhunt.models.flow_session_variables_response import FlowSessionVariablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionVariablesResponse from a JSON string
flow_session_variables_response_instance = FlowSessionVariablesResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionVariablesResponse.to_json())

# convert the object into a dict
flow_session_variables_response_dict = flow_session_variables_response_instance.to_dict()
# create an instance of FlowSessionVariablesResponse from a dict
flow_session_variables_response_from_dict = FlowSessionVariablesResponse.from_dict(flow_session_variables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


