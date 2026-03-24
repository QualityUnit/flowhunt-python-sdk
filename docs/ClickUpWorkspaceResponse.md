# ClickUpWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**team_name** | **str** |  | 
**integration_id** | **str** |  | 

## Example

```python
from flowhunt.models.click_up_workspace_response import ClickUpWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClickUpWorkspaceResponse from a JSON string
click_up_workspace_response_instance = ClickUpWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(ClickUpWorkspaceResponse.to_json())

# convert the object into a dict
click_up_workspace_response_dict = click_up_workspace_response_instance.to_dict()
# create an instance of ClickUpWorkspaceResponse from a dict
click_up_workspace_response_from_dict = ClickUpWorkspaceResponse.from_dict(click_up_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


