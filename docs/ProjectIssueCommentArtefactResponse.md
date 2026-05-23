# ProjectIssueCommentArtefactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Artefact ID | [optional] [default to '']
**name** | **str** | File name | [optional] [default to '']
**relative_path** | **str** | Relative path in workspace | [optional] [default to '']
**s3_key** | **str** | S3 object key | [optional] [default to '']
**mime_type** | **str** | MIME type | [optional] [default to '']
**size** | **int** | File size in bytes | [optional] [default to 0]
**modified_at** | **str** | Last modified timestamp | [optional] [default to '']
**download_url** | **str** | Direct download URL | [optional] [default to '']

## Example

```python
from flowhunt.models.project_issue_comment_artefact_response import ProjectIssueCommentArtefactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueCommentArtefactResponse from a JSON string
project_issue_comment_artefact_response_instance = ProjectIssueCommentArtefactResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueCommentArtefactResponse.to_json())

# convert the object into a dict
project_issue_comment_artefact_response_dict = project_issue_comment_artefact_response_instance.to_dict()
# create an instance of ProjectIssueCommentArtefactResponse from a dict
project_issue_comment_artefact_response_from_dict = ProjectIssueCommentArtefactResponse.from_dict(project_issue_comment_artefact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


