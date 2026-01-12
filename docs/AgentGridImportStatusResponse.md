# AgentGridImportStatusResponse

Schema for CSV import status response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_id** | **str** | Import identifier | 
**status** | **str** | Import status: processing, completed, or failed | 
**total_rows** | **int** | Total number of rows being imported | 
**processed_batches** | **int** | Number of batches processed so far | 
**total_batches** | **int** | Total number of batches | 
**successful_rows** | **int** | Number of rows successfully imported | 
**failed_rows** | **int** | Number of rows that failed to import | 
**progress_percentage** | **float** | Import progress as a percentage (0-100) | 
**errors** | [**List[AgentGridImportError]**](AgentGridImportError.md) | List of import errors (max 1000) | [optional] 
**started_at** | **str** | Import start timestamp | [optional] 
**completed_at** | **str** | Import completion timestamp (null if still processing) | [optional] 

## Example

```python
from flowhunt.models.agent_grid_import_status_response import AgentGridImportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridImportStatusResponse from a JSON string
agent_grid_import_status_response_instance = AgentGridImportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridImportStatusResponse.to_json())

# convert the object into a dict
agent_grid_import_status_response_dict = agent_grid_import_status_response_instance.to_dict()
# create an instance of AgentGridImportStatusResponse from a dict
agent_grid_import_status_response_from_dict = AgentGridImportStatusResponse.from_dict(agent_grid_import_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


