# JiraAssigneeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.jira_assignee_response import JiraAssigneeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraAssigneeResponse from a JSON string
jira_assignee_response_instance = JiraAssigneeResponse.from_json(json)
# print the JSON string representation of the object
print(JiraAssigneeResponse.to_json())

# convert the object into a dict
jira_assignee_response_dict = jira_assignee_response_instance.to_dict()
# create an instance of JiraAssigneeResponse from a dict
jira_assignee_response_from_dict = JiraAssigneeResponse.from_dict(jira_assignee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


