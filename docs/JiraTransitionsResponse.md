# JiraTransitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transitions** | [**List[JiraTransitionResponse]**](JiraTransitionResponse.md) |  | 

## Example

```python
from flowhunt.models.jira_transitions_response import JiraTransitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraTransitionsResponse from a JSON string
jira_transitions_response_instance = JiraTransitionsResponse.from_json(json)
# print the JSON string representation of the object
print(JiraTransitionsResponse.to_json())

# convert the object into a dict
jira_transitions_response_dict = jira_transitions_response_instance.to_dict()
# create an instance of JiraTransitionsResponse from a dict
jira_transitions_response_from_dict = JiraTransitionsResponse.from_dict(jira_transitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


