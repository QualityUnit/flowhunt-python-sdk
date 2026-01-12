# AgentGridRowsBulkInsertRequest

Schema for bulk inserting rows into an agent grid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[Dict[str, object]]** | List of rows to insert | 

## Example

```python
from flowhunt.models.agent_grid_rows_bulk_insert_request import AgentGridRowsBulkInsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridRowsBulkInsertRequest from a JSON string
agent_grid_rows_bulk_insert_request_instance = AgentGridRowsBulkInsertRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGridRowsBulkInsertRequest.to_json())

# convert the object into a dict
agent_grid_rows_bulk_insert_request_dict = agent_grid_rows_bulk_insert_request_instance.to_dict()
# create an instance of AgentGridRowsBulkInsertRequest from a dict
agent_grid_rows_bulk_insert_request_from_dict = AgentGridRowsBulkInsertRequest.from_dict(agent_grid_rows_bulk_insert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


