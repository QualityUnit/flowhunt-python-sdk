# AgentTeamProjectSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Search by name | [optional] 
**limit** | **int** | Limit results | [optional] [default to 25]
**pagination** | [**Pagination**](Pagination.md) | Pagination | [optional] 

## Example

```python
from flowhunt.models.agent_team_project_search_request import AgentTeamProjectSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTeamProjectSearchRequest from a JSON string
agent_team_project_search_request_instance = AgentTeamProjectSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentTeamProjectSearchRequest.to_json())

# convert the object into a dict
agent_team_project_search_request_dict = agent_team_project_search_request_instance.to_dict()
# create an instance of AgentTeamProjectSearchRequest from a dict
agent_team_project_search_request_from_dict = AgentTeamProjectSearchRequest.from_dict(agent_team_project_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


