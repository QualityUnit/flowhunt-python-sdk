# FlowSessionInvocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**created_at** | **str** | Created at | 

## Example

```python
from flowhunt.models.flow_session_invocation_response import FlowSessionInvocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionInvocationResponse from a JSON string
flow_session_invocation_response_instance = FlowSessionInvocationResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionInvocationResponse.to_json())

# convert the object into a dict
flow_session_invocation_response_dict = flow_session_invocation_response_instance.to_dict()
# create an instance of FlowSessionInvocationResponse from a dict
flow_session_invocation_response_from_dict = FlowSessionInvocationResponse.from_dict(flow_session_invocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


