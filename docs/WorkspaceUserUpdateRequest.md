# WorkspaceUserUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](Role.md) | Role of the user in the workspace | [optional] 

## Example

```python
from flowhunt-python-sdk.models.workspace_user_update_request import WorkspaceUserUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserUpdateRequest from a JSON string
workspace_user_update_request_instance = WorkspaceUserUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserUpdateRequest.to_json())

# convert the object into a dict
workspace_user_update_request_dict = workspace_user_update_request_instance.to_dict()
# create an instance of WorkspaceUserUpdateRequest from a dict
workspace_user_update_request_from_dict = WorkspaceUserUpdateRequest.from_dict(workspace_user_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


