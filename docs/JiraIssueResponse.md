# JiraIssueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**summary** | **str** |  | 
**status** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.jira_issue_response import JiraIssueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraIssueResponse from a JSON string
jira_issue_response_instance = JiraIssueResponse.from_json(json)
# print the JSON string representation of the object
print(JiraIssueResponse.to_json())

# convert the object into a dict
jira_issue_response_dict = jira_issue_response_instance.to_dict()
# create an instance of JiraIssueResponse from a dict
jira_issue_response_from_dict = JiraIssueResponse.from_dict(jira_issue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


