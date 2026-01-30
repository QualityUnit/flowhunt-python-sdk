# FlowSessionV3ToolCallEndMetadata

Metadata for V3 tool call end events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Tool name | 
**agent_query** | **str** | Tool input arguments | 
**tool_response** | **str** | Tool response | 
**duration_ms** | **int** | Duration in milliseconds | [optional] 
**action_description** | **str** | Description of what the tool does | [optional] 

## Example

```python
from flowhunt.models.flow_session_v3_tool_call_end_metadata import FlowSessionV3ToolCallEndMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionV3ToolCallEndMetadata from a JSON string
flow_session_v3_tool_call_end_metadata_instance = FlowSessionV3ToolCallEndMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionV3ToolCallEndMetadata.to_json())

# convert the object into a dict
flow_session_v3_tool_call_end_metadata_dict = flow_session_v3_tool_call_end_metadata_instance.to_dict()
# create an instance of FlowSessionV3ToolCallEndMetadata from a dict
flow_session_v3_tool_call_end_metadata_from_dict = FlowSessionV3ToolCallEndMetadata.from_dict(flow_session_v3_tool_call_end_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


