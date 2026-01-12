# AgentGridRowInsertRequest

Schema for inserting a single row into an agent grid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Row data matching the table schema | 

## Example

```python
from flowhunt.models.agent_grid_row_insert_request import AgentGridRowInsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridRowInsertRequest from a JSON string
agent_grid_row_insert_request_instance = AgentGridRowInsertRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGridRowInsertRequest.to_json())

# convert the object into a dict
agent_grid_row_insert_request_dict = agent_grid_row_insert_request_instance.to_dict()
# create an instance of AgentGridRowInsertRequest from a dict
agent_grid_row_insert_request_from_dict = AgentGridRowInsertRequest.from_dict(agent_grid_row_insert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


