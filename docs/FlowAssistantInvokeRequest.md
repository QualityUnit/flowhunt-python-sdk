# FlowAssistantInvokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message of the user | 
**ai_model** | [**FlowAssistantAIModel**](FlowAssistantAIModel.md) | The AI model to use | [optional] 

## Example

```python
from flowhunt.models.flow_assistant_invoke_request import FlowAssistantInvokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantInvokeRequest from a JSON string
flow_assistant_invoke_request_instance = FlowAssistantInvokeRequest.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantInvokeRequest.to_json())

# convert the object into a dict
flow_assistant_invoke_request_dict = flow_assistant_invoke_request_instance.to_dict()
# create an instance of FlowAssistantInvokeRequest from a dict
flow_assistant_invoke_request_from_dict = FlowAssistantInvokeRequest.from_dict(flow_assistant_invoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


