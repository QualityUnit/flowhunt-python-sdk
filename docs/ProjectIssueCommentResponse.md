# ProjectIssueCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | Comment ID | 
**author** | **str** | Author name | 
**text** | **str** | Comment text | 
**created_at** | **str** | Created at | 
**artefacts** | [**List[ProjectIssueCommentArtefactResponse]**](ProjectIssueCommentArtefactResponse.md) | Artefacts attached to this comment | [optional] 
**comment_type** | **str** | Optional structured comment type (e.g. &#39;hitl_approval&#39;). | [optional] 
**metadata** | **Dict[str, object]** | Structured metadata for specialized comment types. | [optional] 

## Example

```python
from flowhunt.models.project_issue_comment_response import ProjectIssueCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueCommentResponse from a JSON string
project_issue_comment_response_instance = ProjectIssueCommentResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueCommentResponse.to_json())

# convert the object into a dict
project_issue_comment_response_dict = project_issue_comment_response_instance.to_dict()
# create an instance of ProjectIssueCommentResponse from a dict
project_issue_comment_response_from_dict = ProjectIssueCommentResponse.from_dict(project_issue_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


