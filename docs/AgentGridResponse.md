# AgentGridResponse

Schema for an agent grid (Flow Table) response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_grid_id** | **str** | Agent Grid ID | 
**workspace_id** | **str** | Workspace ID | 
**name** | **str** | Name of the Flow Table | 
**description** | **str** | Description of the Flow Table | [optional] 
**schema_fields** | [**List[AgentGridFieldResponse]**](AgentGridFieldResponse.md) | List of fields defining the table schema | 
**semantic_search_enabled** | **bool** | Whether semantic search is enabled | 
**row_count** | **int** | Number of rows in the table | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

## Example

```python
from flowhunt.models.agent_grid_response import AgentGridResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridResponse from a JSON string
agent_grid_response_instance = AgentGridResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridResponse.to_json())

# convert the object into a dict
agent_grid_response_dict = agent_grid_response_instance.to_dict()
# create an instance of AgentGridResponse from a dict
agent_grid_response_from_dict = AgentGridResponse.from_dict(agent_grid_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


