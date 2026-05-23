# FlowSessionSubagentPromptMetadata

Metadata for the prompt that a supervisor sends to a subagent.  Emitted from ``start_async_task`` when a delegating agent spawns a coworker workflow. Tagged with ``component_name`` = the subagent's name and ``run_id`` = the subagent's pyworkflow run, so it surfaces in the subagent's tab in the UI and in the ``check_async_task`` activity log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | **str** | The full prompt sent to the subagent. | 
**started_by** | **str** | Name of the agent that initiated this delegation. | 
**target_agent** | **str** | Name of the subagent receiving the task. | 

## Example

```python
from flowhunt.models.flow_session_subagent_prompt_metadata import FlowSessionSubagentPromptMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionSubagentPromptMetadata from a JSON string
flow_session_subagent_prompt_metadata_instance = FlowSessionSubagentPromptMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionSubagentPromptMetadata.to_json())

# convert the object into a dict
flow_session_subagent_prompt_metadata_dict = flow_session_subagent_prompt_metadata_instance.to_dict()
# create an instance of FlowSessionSubagentPromptMetadata from a dict
flow_session_subagent_prompt_metadata_from_dict = FlowSessionSubagentPromptMetadata.from_dict(flow_session_subagent_prompt_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


