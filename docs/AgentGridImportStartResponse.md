# AgentGridImportStartResponse

Schema for CSV import start response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_id** | **str** | Unique identifier for tracking the import | 
**total_rows** | **int** | Total number of rows to import | 
**message** | **str** | Status message | 

## Example

```python
from flowhunt.models.agent_grid_import_start_response import AgentGridImportStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridImportStartResponse from a JSON string
agent_grid_import_start_response_instance = AgentGridImportStartResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridImportStartResponse.to_json())

# convert the object into a dict
agent_grid_import_start_response_dict = agent_grid_import_start_response_instance.to_dict()
# create an instance of AgentGridImportStartResponse from a dict
agent_grid_import_start_response_from_dict = AgentGridImportStartResponse.from_dict(agent_grid_import_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


