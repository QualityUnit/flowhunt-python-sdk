# ProjectIssueUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Issue title | [optional] 
**description** | **str** | Issue description | [optional] 
**status** | **str** | Issue status | [optional] 
**issue_type** | **str** | Issue type | [optional] 
**frequency** | **str** | Frequency for periodic issues | [optional] 
**next_run** | **datetime** | Reschedule this issue to run at a specific UTC time. Must be in the future. | [optional] 
**tag_ids** | **List[str]** | Tag IDs | [optional] 

## Example

```python
from flowhunt.models.project_issue_update import ProjectIssueUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueUpdate from a JSON string
project_issue_update_instance = ProjectIssueUpdate.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueUpdate.to_json())

# convert the object into a dict
project_issue_update_dict = project_issue_update_instance.to_dict()
# create an instance of ProjectIssueUpdate from a dict
project_issue_update_from_dict = ProjectIssueUpdate.from_dict(project_issue_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


