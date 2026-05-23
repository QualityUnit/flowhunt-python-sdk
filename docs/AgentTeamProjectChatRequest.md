# AgentTeamProjectChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | User message to send to the project&#39;s agent team | 
**session_id** | **str** | Session ID from a previous chat response. Pass this to continue an existing conversation. | [optional] 

## Example

```python
from flowhunt.models.agent_team_project_chat_request import AgentTeamProjectChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTeamProjectChatRequest from a JSON string
agent_team_project_chat_request_instance = AgentTeamProjectChatRequest.from_json(json)
# print the JSON string representation of the object
print(AgentTeamProjectChatRequest.to_json())

# convert the object into a dict
agent_team_project_chat_request_dict = agent_team_project_chat_request_instance.to_dict()
# create an instance of AgentTeamProjectChatRequest from a dict
agent_team_project_chat_request_from_dict = AgentTeamProjectChatRequest.from_dict(agent_team_project_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


