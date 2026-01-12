# FlowSessionAgentCotMetadata

Metadata for agent chain of thought / reasoning events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cot_id** | **str** | Unique CoT identifier for updates | 
**content** | **str** | Chain of thought / reasoning text | 

## Example

```python
from flowhunt.models.flow_session_agent_cot_metadata import FlowSessionAgentCotMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionAgentCotMetadata from a JSON string
flow_session_agent_cot_metadata_instance = FlowSessionAgentCotMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionAgentCotMetadata.to_json())

# convert the object into a dict
flow_session_agent_cot_metadata_dict = flow_session_agent_cot_metadata_instance.to_dict()
# create an instance of FlowSessionAgentCotMetadata from a dict
flow_session_agent_cot_metadata_from_dict = FlowSessionAgentCotMetadata.from_dict(flow_session_agent_cot_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


