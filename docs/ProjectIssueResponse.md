# ProjectIssueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Issue ID | 
**project_id** | **str** | Project ID | 
**workspace_id** | **str** | Workspace ID | 
**title** | **str** | Issue title | 
**description** | **str** | Issue description | [optional] 
**status** | **str** | Issue status | 
**issue_type** | **str** | Issue type | [optional] [default to 'normal']
**frequency** | **str** | Frequency for periodic issues | [optional] 
**next_run** | **str** | Next scheduled execution time | [optional] 
**last_run** | **str** | Last execution time | [optional] 
**tag_ids** | **List[str]** | Tag IDs | [optional] 
**comments** | [**List[ProjectIssueCommentResponse]**](ProjectIssueCommentResponse.md) | Issue comments | [optional] 
**created_at** | **str** | Created at | 
**updated_at** | **str** | Updated at | 
**created_by** | **str** | Created by user ID | 
**run_user_comment_id** | **str** | ID of the user comment that should focus the next task run. Set when the user reopens an issue with a comment; cleared after the task dispatcher consumes it. | [optional] 
**session_id** | **str** | ID of the flow session that ran (or is running) this issue. Used to deep-link from the issue drawer to the run detail view. | [optional] 

## Example

```python
from flowhunt.models.project_issue_response import ProjectIssueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueResponse from a JSON string
project_issue_response_instance = ProjectIssueResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueResponse.to_json())

# convert the object into a dict
project_issue_response_dict = project_issue_response_instance.to_dict()
# create an instance of ProjectIssueResponse from a dict
project_issue_response_from_dict = ProjectIssueResponse.from_dict(project_issue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


