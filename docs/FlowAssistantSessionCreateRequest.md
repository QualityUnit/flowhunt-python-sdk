# FlowAssistantSessionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_flow_id** | **str** | The Agent ID currently being enhanced by the AI Agent. | [optional] 
**start_with_welcome_message** | **bool** | Whether to start with a welcome message. | [optional] [default to False]

## Example

```python
from flowhunt.models.flow_assistant_session_create_request import FlowAssistantSessionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantSessionCreateRequest from a JSON string
flow_assistant_session_create_request_instance = FlowAssistantSessionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantSessionCreateRequest.to_json())

# convert the object into a dict
flow_assistant_session_create_request_dict = flow_assistant_session_create_request_instance.to_dict()
# create an instance of FlowAssistantSessionCreateRequest from a dict
flow_assistant_session_create_request_from_dict = FlowAssistantSessionCreateRequest.from_dict(flow_assistant_session_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


