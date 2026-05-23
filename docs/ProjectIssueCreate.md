# ProjectIssueCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Issue title | 
**description** | **str** | Issue description | [optional] 
**status** | **str** | Issue status | [optional] 
**issue_type** | **str** | Issue type: normal or periodic | [optional] [default to 'normal']
**frequency** | **str** | Frequency for periodic issues (e.g. daily, weekly) | [optional] 
**next_run** | **datetime** | Schedule this issue to run at a specific UTC time. Leave empty to run on the next dispatcher tick. | [optional] 
**tag_ids** | **List[str]** | Tag IDs | [optional] 

## Example

```python
from flowhunt.models.project_issue_create import ProjectIssueCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueCreate from a JSON string
project_issue_create_instance = ProjectIssueCreate.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueCreate.to_json())

# convert the object into a dict
project_issue_create_dict = project_issue_create_instance.to_dict()
# create an instance of ProjectIssueCreate from a dict
project_issue_create_from_dict = ProjectIssueCreate.from_dict(project_issue_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


