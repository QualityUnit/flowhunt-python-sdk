# JiraAssigneesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[JiraAssigneeResponse]**](JiraAssigneeResponse.md) |  | 

## Example

```python
from flowhunt.models.jira_assignees_response import JiraAssigneesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraAssigneesResponse from a JSON string
jira_assignees_response_instance = JiraAssigneesResponse.from_json(json)
# print the JSON string representation of the object
print(JiraAssigneesResponse.to_json())

# convert the object into a dict
jira_assignees_response_dict = jira_assignees_response_instance.to_dict()
# create an instance of JiraAssigneesResponse from a dict
jira_assignees_response_from_dict = JiraAssigneesResponse.from_dict(jira_assignees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


