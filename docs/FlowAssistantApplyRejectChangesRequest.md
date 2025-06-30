# FlowAssistantApplyRejectChangesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | The Flow ID currently being enhanced by the AI Agent. | 
**action_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_assistant_apply_reject_changes_request import FlowAssistantApplyRejectChangesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantApplyRejectChangesRequest from a JSON string
flow_assistant_apply_reject_changes_request_instance = FlowAssistantApplyRejectChangesRequest.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantApplyRejectChangesRequest.to_json())

# convert the object into a dict
flow_assistant_apply_reject_changes_request_dict = flow_assistant_apply_reject_changes_request_instance.to_dict()
# create an instance of FlowAssistantApplyRejectChangesRequest from a dict
flow_assistant_apply_reject_changes_request_from_dict = FlowAssistantApplyRejectChangesRequest.from_dict(flow_assistant_apply_reject_changes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


