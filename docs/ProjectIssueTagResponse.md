# ProjectIssueTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tag ID | 
**project_id** | **str** | Project ID | 
**name** | **str** | Tag name | 
**description** | **str** | Tag description | [optional] 
**color** | **str** | Tag color hex code | 
**created_at** | **datetime** | Created at | 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from flowhunt.models.project_issue_tag_response import ProjectIssueTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueTagResponse from a JSON string
project_issue_tag_response_instance = ProjectIssueTagResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueTagResponse.to_json())

# convert the object into a dict
project_issue_tag_response_dict = project_issue_tag_response_instance.to_dict()
# create an instance of ProjectIssueTagResponse from a dict
project_issue_tag_response_from_dict = ProjectIssueTagResponse.from_dict(project_issue_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


