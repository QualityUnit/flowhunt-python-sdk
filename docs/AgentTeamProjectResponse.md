# AgentTeamProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Project ID | 
**name** | **str** | Project name | 
**description** | **str** | Project description | [optional] 
**specification** | **str** | Project specification | [optional] 
**agents_spec** | **Dict[str, object]** | Team agents specification | [optional] 
**suggestions** | **List[Dict[str, object]]** | LLM-generated chat suggestions | [optional] 
**color** | **str** | Project color | [optional] 
**icon** | **str** | Project icon name | [optional] 
**image_url** | **str** | Project avatar image URL | [optional] 
**channel_spec** | **Dict[str, object]** | Channel specification | [optional] 
**created_at** | **datetime** | Created at | 
**updated_at** | **datetime** | Updated at | [optional] 
**last_visited** | **datetime** | Last visited timestamp | [optional] 
**max_task_concurrency** | **int** | Maximum concurrent issue processing. None means default (1). | [optional] 
**hitl_mode** | **str** | Tool approval mode: &#39;disabled&#39;, &#39;side_effects_only&#39;, or &#39;all_third_party&#39; | [optional] [default to 'disabled']
**hitl_approved_tools** | **List[str]** | List of tool names permanently approved for this project | [optional] 
**model_options** | **Dict[str, List[str]]** | Available AI models grouped by provider | [optional] 
**sandbox_enabled** | **bool** | Whether agents run inside an isolated sandbox container. | [optional] [default to False]
**sandbox_clone_url** | **str** | Optional git repository URL cloned into /sandbox at session start. | [optional] 
**sandbox_clone_ref** | **str** | Optional branch or ref checked out after cloning the repo. | [optional] 

## Example

```python
from flowhunt.models.agent_team_project_response import AgentTeamProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTeamProjectResponse from a JSON string
agent_team_project_response_instance = AgentTeamProjectResponse.from_json(json)
# print the JSON string representation of the object
print(AgentTeamProjectResponse.to_json())

# convert the object into a dict
agent_team_project_response_dict = agent_team_project_response_instance.to_dict()
# create an instance of AgentTeamProjectResponse from a dict
agent_team_project_response_from_dict = AgentTeamProjectResponse.from_dict(agent_team_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


