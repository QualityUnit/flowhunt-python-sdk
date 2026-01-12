# AgentGridRowInsertResponse

Schema for row insert response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** | ID of the inserted row | 

## Example

```python
from flowhunt.models.agent_grid_row_insert_response import AgentGridRowInsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridRowInsertResponse from a JSON string
agent_grid_row_insert_response_instance = AgentGridRowInsertResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridRowInsertResponse.to_json())

# convert the object into a dict
agent_grid_row_insert_response_dict = agent_grid_row_insert_response_instance.to_dict()
# create an instance of AgentGridRowInsertResponse from a dict
agent_grid_row_insert_response_from_dict = AgentGridRowInsertResponse.from_dict(agent_grid_row_insert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


