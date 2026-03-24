# FlowSessionV3ToolCallStartMetadata

Metadata for V3 tool call start events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Tool name | 
**agent_query** | **str** | Tool input arguments | 
**action_description** | **str** | Description of what the tool does | [optional] 

## Example

```python
from flowhunt.models.flow_session_v3_tool_call_start_metadata import FlowSessionV3ToolCallStartMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionV3ToolCallStartMetadata from a JSON string
flow_session_v3_tool_call_start_metadata_instance = FlowSessionV3ToolCallStartMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionV3ToolCallStartMetadata.to_json())

# convert the object into a dict
flow_session_v3_tool_call_start_metadata_dict = flow_session_v3_tool_call_start_metadata_instance.to_dict()
# create an instance of FlowSessionV3ToolCallStartMetadata from a dict
flow_session_v3_tool_call_start_metadata_from_dict = FlowSessionV3ToolCallStartMetadata.from_dict(flow_session_v3_tool_call_start_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


