# JiraProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from flowhunt.models.jira_project_response import JiraProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraProjectResponse from a JSON string
jira_project_response_instance = JiraProjectResponse.from_json(json)
# print the JSON string representation of the object
print(JiraProjectResponse.to_json())

# convert the object into a dict
jira_project_response_dict = jira_project_response_instance.to_dict()
# create an instance of JiraProjectResponse from a dict
jira_project_response_from_dict = JiraProjectResponse.from_dict(jira_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


