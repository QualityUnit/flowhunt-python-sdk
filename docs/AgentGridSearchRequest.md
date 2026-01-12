# AgentGridSearchRequest

Schema for searching rows in an agent grid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Full-text search query | [optional] 
**filters** | **Dict[str, object]** | Field filters for exact matching | [optional] 
**limit** | **int** | Maximum number of rows to return | [optional] [default to 50]
**offset** | **int** | Number of rows to skip | [optional] [default to 0]

## Example

```python
from flowhunt.models.agent_grid_search_request import AgentGridSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridSearchRequest from a JSON string
agent_grid_search_request_instance = AgentGridSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGridSearchRequest.to_json())

# convert the object into a dict
agent_grid_search_request_dict = agent_grid_search_request_instance.to_dict()
# create an instance of AgentGridSearchRequest from a dict
agent_grid_search_request_from_dict = AgentGridSearchRequest.from_dict(agent_grid_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


