# GenerateAgentConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | The type of agent: supervisor, lead, or worker. Optional for edit_team mode. | [optional] [default to 'worker']
**description** | **str** | What is this agent used for? Required for single_agent/full_team/project_only modes. | [optional] 
**agents_spec** | **Dict[str, object]** | Current team agents_spec for context | [optional] 
**mode** | **str** | Generation mode: single_agent, full_team, project_only, or edit_team | [optional] [default to 'single_agent']
**message** | **str** | User message for edit_team mode (what to change) | [optional] 

## Example

```python
from flowhunt.models.generate_agent_config_request import GenerateAgentConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAgentConfigRequest from a JSON string
generate_agent_config_request_instance = GenerateAgentConfigRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateAgentConfigRequest.to_json())

# convert the object into a dict
generate_agent_config_request_dict = generate_agent_config_request_instance.to_dict()
# create an instance of GenerateAgentConfigRequest from a dict
generate_agent_config_request_from_dict = GenerateAgentConfigRequest.from_dict(generate_agent_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


