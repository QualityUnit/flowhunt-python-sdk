# SlackWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**workspace_name** | **str** |  | 
**integration_id** | **str** |  | 

## Example

```python
from flowhunt.models.slack_workspace_response import SlackWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SlackWorkspaceResponse from a JSON string
slack_workspace_response_instance = SlackWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(SlackWorkspaceResponse.to_json())

# convert the object into a dict
slack_workspace_response_dict = slack_workspace_response_instance.to_dict()
# create an instance of SlackWorkspaceResponse from a dict
slack_workspace_response_from_dict = SlackWorkspaceResponse.from_dict(slack_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


