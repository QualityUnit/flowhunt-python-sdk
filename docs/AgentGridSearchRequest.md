# AgentGridSearchRequest

Schema for searching rows in an agent grid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Full-text search query | [optional] 
**filters** | [**Dict[str, FiltersValue]**](FiltersValue.md) | Per-column filters keyed by field name. The body is a discriminated union on &#x60;&#x60;op&#x60;&#x60; (&#x60;&#x60;term&#x60;&#x60; | &#x60;&#x60;terms&#x60;&#x60; | &#x60;&#x60;match&#x60;&#x60; | &#x60;&#x60;range&#x60;&#x60;). | [optional] 
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


