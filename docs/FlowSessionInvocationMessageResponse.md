# FlowSessionInvocationMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**response_status** | [**FlowSessionStatus**](FlowSessionStatus.md) | Response status | 
**loading_indicator** | [**Dict[str, FlowLoadingIndicator]**](FlowLoadingIndicator.md) |  | [optional] 
**intermediate_results** | [**Dict[str, TaskOutput]**](TaskOutput.md) |  | [optional] 
**final_response** | **List[str]** |  | [optional] 

## Example

```python
from flowhunt.models.flow_session_invocation_message_response import FlowSessionInvocationMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionInvocationMessageResponse from a JSON string
flow_session_invocation_message_response_instance = FlowSessionInvocationMessageResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionInvocationMessageResponse.to_json())

# convert the object into a dict
flow_session_invocation_message_response_dict = flow_session_invocation_message_response_instance.to_dict()
# create an instance of FlowSessionInvocationMessageResponse from a dict
flow_session_invocation_message_response_from_dict = FlowSessionInvocationMessageResponse.from_dict(flow_session_invocation_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


