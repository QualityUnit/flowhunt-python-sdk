# FlowSessionAgentInitializedMetadata

Metadata for agent initialized events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_name** | **str** | Name of the agent | 
**agent_type** | **str** | Agent type: supervisor, lead, or worker | 
**model** | **str** | LLM model name used by the agent | 

## Example

```python
from flowhunt.models.flow_session_agent_initialized_metadata import FlowSessionAgentInitializedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionAgentInitializedMetadata from a JSON string
flow_session_agent_initialized_metadata_instance = FlowSessionAgentInitializedMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionAgentInitializedMetadata.to_json())

# convert the object into a dict
flow_session_agent_initialized_metadata_dict = flow_session_agent_initialized_metadata_instance.to_dict()
# create an instance of FlowSessionAgentInitializedMetadata from a dict
flow_session_agent_initialized_metadata_from_dict = FlowSessionAgentInitializedMetadata.from_dict(flow_session_agent_initialized_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


