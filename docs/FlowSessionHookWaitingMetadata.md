# FlowSessionHookWaitingMetadata

Metadata for hook waiting for input events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_id** | **str** | Hook ID for resuming the hook | 
**hook_name** | **str** | Hook name (e.g., &#39;wait_for_user_input&#39;) | 
**prompt_message** | **str** | Message to show the user | 

## Example

```python
from flowhunt.models.flow_session_hook_waiting_metadata import FlowSessionHookWaitingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionHookWaitingMetadata from a JSON string
flow_session_hook_waiting_metadata_instance = FlowSessionHookWaitingMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionHookWaitingMetadata.to_json())

# convert the object into a dict
flow_session_hook_waiting_metadata_dict = flow_session_hook_waiting_metadata_instance.to_dict()
# create an instance of FlowSessionHookWaitingMetadata from a dict
flow_session_hook_waiting_metadata_from_dict = FlowSessionHookWaitingMetadata.from_dict(flow_session_hook_waiting_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


