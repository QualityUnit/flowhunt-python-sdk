# AgentGridCreateRequest

Schema for creating a new agent grid (Flow Table).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Agent Grid (must be snake_case: lowercase letters, numbers, underscores only) | 
**description** | **str** | Description of the Flow Table | [optional] 
**schema_fields** | [**List[AgentGridFieldRequest]**](AgentGridFieldRequest.md) | List of fields defining the table schema | 
**semantic_search_enabled** | **bool** | Whether semantic search is enabled (not yet available) | [optional] [default to False]

## Example

```python
from flowhunt.models.agent_grid_create_request import AgentGridCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridCreateRequest from a JSON string
agent_grid_create_request_instance = AgentGridCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGridCreateRequest.to_json())

# convert the object into a dict
agent_grid_create_request_dict = agent_grid_create_request_instance.to_dict()
# create an instance of AgentGridCreateRequest from a dict
agent_grid_create_request_from_dict = AgentGridCreateRequest.from_dict(agent_grid_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


