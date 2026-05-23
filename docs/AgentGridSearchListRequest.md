# AgentGridSearchListRequest

Schema for searching/listing Flow Tables (Agent Grids) in a workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional case-insensitive substring filter on the Flow Table name or description. When omitted or empty all grids are returned. | [optional] 

## Example

```python
from flowhunt.models.agent_grid_search_list_request import AgentGridSearchListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridSearchListRequest from a JSON string
agent_grid_search_list_request_instance = AgentGridSearchListRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGridSearchListRequest.to_json())

# convert the object into a dict
agent_grid_search_list_request_dict = agent_grid_search_list_request_instance.to_dict()
# create an instance of AgentGridSearchListRequest from a dict
agent_grid_search_list_request_from_dict = AgentGridSearchListRequest.from_dict(agent_grid_search_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


