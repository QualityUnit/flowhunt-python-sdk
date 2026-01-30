# JiraIssuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issues** | [**List[JiraIssueResponse]**](JiraIssueResponse.md) |  | 

## Example

```python
from flowhunt.models.jira_issues_response import JiraIssuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraIssuesResponse from a JSON string
jira_issues_response_instance = JiraIssuesResponse.from_json(json)
# print the JSON string representation of the object
print(JiraIssuesResponse.to_json())

# convert the object into a dict
jira_issues_response_dict = jira_issues_response_instance.to_dict()
# create an instance of JiraIssuesResponse from a dict
jira_issues_response_from_dict = JiraIssuesResponse.from_dict(jira_issues_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


