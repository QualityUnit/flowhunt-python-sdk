# FlowSessionHookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_name** | **str** | The hook name to fire (must match a ChatHook trigger node) | 
**payload** | **Dict[str, object]** | Arbitrary JSON payload for the hook | [optional] 
**flow_variables** | **Dict[str, object]** | Variables to merge into the session before firing the hook | [optional] 

## Example

```python
from flowhunt.models.flow_session_hook_request import FlowSessionHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionHookRequest from a JSON string
flow_session_hook_request_instance = FlowSessionHookRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionHookRequest.to_json())

# convert the object into a dict
flow_session_hook_request_dict = flow_session_hook_request_instance.to_dict()
# create an instance of FlowSessionHookRequest from a dict
flow_session_hook_request_from_dict = FlowSessionHookRequest.from_dict(flow_session_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


