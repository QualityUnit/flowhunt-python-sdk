# ProjectIssueCommentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The comment body the user wants to attach to the issue. | 
**reopen** | **bool** | If true, also move the issue back to &#39;open&#39; and record the comment id so the next task run focuses on this feedback. | [optional] [default to False]

## Example

```python
from flowhunt.models.project_issue_comment_create import ProjectIssueCommentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueCommentCreate from a JSON string
project_issue_comment_create_instance = ProjectIssueCommentCreate.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueCommentCreate.to_json())

# convert the object into a dict
project_issue_comment_create_dict = project_issue_comment_create_instance.to_dict()
# create an instance of ProjectIssueCommentCreate from a dict
project_issue_comment_create_from_dict = ProjectIssueCommentCreate.from_dict(project_issue_comment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


