# AgentTeamProjectCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The project name | 
**description** | **str** | The project description | [optional] 
**specification** | **str** | The project specification | [optional] 
**color** | **str** | Project color in hex format | [optional] 
**icon** | **str** | Project icon name (e.g. TbRocket) | [optional] 
**image_url** | **str** | Project avatar image URL | [optional] 
**channel_spec** | **Dict[str, object]** | Channel specification (e.g. Slack config) | [optional] 
**agents_spec** | **Dict[str, object]** | Agents configuration (nodes and connections). When provided during onboarding the team is created with the AI-generated spec already in place — no follow-up update call needed. | [optional] 
**max_task_concurrency** | **int** | Maximum number of issues that can be processed concurrently. Defaults to 1. Capped by your subscription plan. | [optional] 
**hitl_mode** | **str** | Tool approval mode: &#39;disabled&#39;, &#39;side_effects_only&#39;, or &#39;all_third_party&#39; | [optional] [default to 'disabled']
**hitl_approved_tools** | **List[str]** | List of tool names permanently approved for this project | [optional] 
**sandbox_enabled** | **bool** | Whether agents run inside an isolated sandbox container. Requires a paid plan (Trial, Pro, Premium, or Enterprise). | [optional] 
**sandbox_clone_url** | **str** | Optional git repository URL cloned into /sandbox at session start. | [optional] 
**sandbox_clone_ref** | **str** | Optional branch or ref checked out after cloning the repo. | [optional] 
**template_id** | **str** | Slug of an AI Projects Library template to seed the project from. When set, the server hydrates agents_spec, specification, hitl config, color/icon, custom tags, and initial issues from the catalog. Client-provided values for these fields override the template only when explicitly set. | [optional] 

## Example

```python
from flowhunt.models.agent_team_project_create import AgentTeamProjectCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTeamProjectCreate from a JSON string
agent_team_project_create_instance = AgentTeamProjectCreate.from_json(json)
# print the JSON string representation of the object
print(AgentTeamProjectCreate.to_json())

# convert the object into a dict
agent_team_project_create_dict = agent_team_project_create_instance.to_dict()
# create an instance of AgentTeamProjectCreate from a dict
agent_team_project_create_from_dict = AgentTeamProjectCreate.from_dict(agent_team_project_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


