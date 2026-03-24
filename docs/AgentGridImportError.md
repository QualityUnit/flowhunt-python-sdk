# AgentGridImportError

Schema for a single import error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** | Row number where the error occurred (1-indexed) | 
**var_field** | **str** | Field name that caused the error | 
**error** | **str** | Error message | 

## Example

```python
from flowhunt.models.agent_grid_import_error import AgentGridImportError

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridImportError from a JSON string
agent_grid_import_error_instance = AgentGridImportError.from_json(json)
# print the JSON string representation of the object
print(AgentGridImportError.to_json())

# convert the object into a dict
agent_grid_import_error_dict = agent_grid_import_error_instance.to_dict()
# create an instance of AgentGridImportError from a dict
agent_grid_import_error_from_dict = AgentGridImportError.from_dict(agent_grid_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


