# ProjectInboxEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workspace_id** | **str** |  | 
**project_id** | **str** |  | 
**kind** | **str** |  | 
**status** | **str** |  | 
**title** | **str** |  | 
**body** | **str** |  | 
**issue_id** | **str** |  | 
**session_id** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from flowhunt.models.project_inbox_entry_response import ProjectInboxEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInboxEntryResponse from a JSON string
project_inbox_entry_response_instance = ProjectInboxEntryResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectInboxEntryResponse.to_json())

# convert the object into a dict
project_inbox_entry_response_dict = project_inbox_entry_response_instance.to_dict()
# create an instance of ProjectInboxEntryResponse from a dict
project_inbox_entry_response_from_dict = ProjectInboxEntryResponse.from_dict(project_inbox_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


