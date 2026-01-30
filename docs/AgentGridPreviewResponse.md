# AgentGridPreviewResponse

Schema for agent grid preview response (first N rows).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[Dict[str, object]]** | Preview rows | 
**total_count** | **int** | Total number of rows in the table | 

## Example

```python
from flowhunt.models.agent_grid_preview_response import AgentGridPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridPreviewResponse from a JSON string
agent_grid_preview_response_instance = AgentGridPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridPreviewResponse.to_json())

# convert the object into a dict
agent_grid_preview_response_dict = agent_grid_preview_response_instance.to_dict()
# create an instance of AgentGridPreviewResponse from a dict
agent_grid_preview_response_from_dict = AgentGridPreviewResponse.from_dict(agent_grid_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


