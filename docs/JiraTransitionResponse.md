# JiraTransitionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from flowhunt.models.jira_transition_response import JiraTransitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraTransitionResponse from a JSON string
jira_transition_response_instance = JiraTransitionResponse.from_json(json)
# print the JSON string representation of the object
print(JiraTransitionResponse.to_json())

# convert the object into a dict
jira_transition_response_dict = jira_transition_response_instance.to_dict()
# create an instance of JiraTransitionResponse from a dict
jira_transition_response_from_dict = JiraTransitionResponse.from_dict(jira_transition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


