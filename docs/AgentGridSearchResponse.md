# AgentGridSearchResponse

Schema for agent grid search response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[Dict[str, object]]** | Search result rows | 
**total_count** | **int** | Total number of matching rows | 

## Example

```python
from flowhunt.models.agent_grid_search_response import AgentGridSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridSearchResponse from a JSON string
agent_grid_search_response_instance = AgentGridSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridSearchResponse.to_json())

# convert the object into a dict
agent_grid_search_response_dict = agent_grid_search_response_instance.to_dict()
# create an instance of AgentGridSearchResponse from a dict
agent_grid_search_response_from_dict = AgentGridSearchResponse.from_dict(agent_grid_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


