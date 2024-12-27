# FlowSessionToolCallMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Tool name | 
**agent_query** | **str** | Search query | 
**tool_response** | **str** | Tool response | 

## Example

```python
from flowhunt.models.flow_session_tool_call_metadata import FlowSessionToolCallMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionToolCallMetadata from a JSON string
flow_session_tool_call_metadata_instance = FlowSessionToolCallMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionToolCallMetadata.to_json())

# convert the object into a dict
flow_session_tool_call_metadata_dict = flow_session_tool_call_metadata_instance.to_dict()
# create an instance of FlowSessionToolCallMetadata from a dict
flow_session_tool_call_metadata_from_dict = FlowSessionToolCallMetadata.from_dict(flow_session_tool_call_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


