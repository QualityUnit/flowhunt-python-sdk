# FlowSessionV3FlowAssistantInitMetadata

Metadata for V3 Flow Assistant initialization events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | **str** | Initialization stage (e.g., &#39;starting&#39;, &#39;creating_agent&#39;, &#39;ready&#39;) | 
**message** | **str** | User-friendly message describing the current stage | 

## Example

```python
from flowhunt.models.flow_session_v3_flow_assistant_init_metadata import FlowSessionV3FlowAssistantInitMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionV3FlowAssistantInitMetadata from a JSON string
flow_session_v3_flow_assistant_init_metadata_instance = FlowSessionV3FlowAssistantInitMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionV3FlowAssistantInitMetadata.to_json())

# convert the object into a dict
flow_session_v3_flow_assistant_init_metadata_dict = flow_session_v3_flow_assistant_init_metadata_instance.to_dict()
# create an instance of FlowSessionV3FlowAssistantInitMetadata from a dict
flow_session_v3_flow_assistant_init_metadata_from_dict = FlowSessionV3FlowAssistantInitMetadata.from_dict(flow_session_v3_flow_assistant_init_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


