# AgentGridBulkInsertResponse

Schema for bulk insert response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_count** | **int** | Number of rows inserted | 

## Example

```python
from flowhunt.models.agent_grid_bulk_insert_response import AgentGridBulkInsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridBulkInsertResponse from a JSON string
agent_grid_bulk_insert_response_instance = AgentGridBulkInsertResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridBulkInsertResponse.to_json())

# convert the object into a dict
agent_grid_bulk_insert_response_dict = agent_grid_bulk_insert_response_instance.to_dict()
# create an instance of AgentGridBulkInsertResponse from a dict
agent_grid_bulk_insert_response_from_dict = AgentGridBulkInsertResponse.from_dict(agent_grid_bulk_insert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


