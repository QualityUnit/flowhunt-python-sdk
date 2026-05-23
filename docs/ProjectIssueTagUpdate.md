# ProjectIssueTagUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tag name | [optional] 
**description** | **str** | Tag description | [optional] 
**color** | **str** | Tag color hex code | [optional] 

## Example

```python
from flowhunt.models.project_issue_tag_update import ProjectIssueTagUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueTagUpdate from a JSON string
project_issue_tag_update_instance = ProjectIssueTagUpdate.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueTagUpdate.to_json())

# convert the object into a dict
project_issue_tag_update_dict = project_issue_tag_update_instance.to_dict()
# create an instance of ProjectIssueTagUpdate from a dict
project_issue_tag_update_from_dict = ProjectIssueTagUpdate.from_dict(project_issue_tag_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


