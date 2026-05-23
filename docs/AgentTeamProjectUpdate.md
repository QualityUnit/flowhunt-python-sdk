# AgentTeamProjectUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The project name | [optional] 
**description** | **str** | The project description | [optional] 
**specification** | **str** | The project specification | [optional] 
**color** | **str** | Project color in hex format | [optional] 
**icon** | **str** | Project icon name (e.g. TbRocket) | [optional] 
**image_url** | **str** | Project avatar image URL | [optional] 
**channel_spec** | **Dict[str, object]** | Channel specification (e.g. Slack config) | [optional] 
**agents_spec** | **Dict[str, object]** | Agents configuration (nodes and connections) | [optional] 
**max_task_concurrency** | **int** | Maximum number of issues that can be processed concurrently. Defaults to 1. Capped by your subscription plan. | [optional] 
**hitl_mode** | **str** | Tool approval mode: &#39;disabled&#39;, &#39;side_effects_only&#39;, or &#39;all_third_party&#39; | [optional] [default to 'disabled']
**hitl_approved_tools** | **List[str]** | List of tool names permanently approved for this project | [optional] 
**sandbox_enabled** | **bool** | Whether agents run inside an isolated sandbox container. Requires a paid plan (Trial, Pro, Premium, or Enterprise). | [optional] 
**sandbox_clone_url** | **str** | Optional git repository URL cloned into /sandbox at session start. | [optional] 
**sandbox_clone_ref** | **str** | Optional branch or ref checked out after cloning the repo. | [optional] 

## Example

```python
from flowhunt.models.agent_team_project_update import AgentTeamProjectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTeamProjectUpdate from a JSON string
agent_team_project_update_instance = AgentTeamProjectUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentTeamProjectUpdate.to_json())

# convert the object into a dict
agent_team_project_update_dict = agent_team_project_update_instance.to_dict()
# create an instance of AgentTeamProjectUpdate from a dict
agent_team_project_update_from_dict = AgentTeamProjectUpdate.from_dict(agent_team_project_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


