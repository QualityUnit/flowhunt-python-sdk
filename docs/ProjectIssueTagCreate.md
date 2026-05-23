# ProjectIssueTagCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tag name | 
**description** | **str** | Tag description | [optional] 
**color** | **str** | Tag color hex code | [optional] [default to '#6B7280']

## Example

```python
from flowhunt.models.project_issue_tag_create import ProjectIssueTagCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueTagCreate from a JSON string
project_issue_tag_create_instance = ProjectIssueTagCreate.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueTagCreate.to_json())

# convert the object into a dict
project_issue_tag_create_dict = project_issue_tag_create_instance.to_dict()
# create an instance of ProjectIssueTagCreate from a dict
project_issue_tag_create_from_dict = ProjectIssueTagCreate.from_dict(project_issue_tag_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


