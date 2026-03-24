# JiraProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[JiraProjectResponse]**](JiraProjectResponse.md) |  | 

## Example

```python
from flowhunt.models.jira_projects_response import JiraProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraProjectsResponse from a JSON string
jira_projects_response_instance = JiraProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(JiraProjectsResponse.to_json())

# convert the object into a dict
jira_projects_response_dict = jira_projects_response_instance.to_dict()
# create an instance of JiraProjectsResponse from a dict
jira_projects_response_from_dict = JiraProjectsResponse.from_dict(jira_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


