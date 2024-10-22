# WorkspaceRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**workspace_name** | **str** | Workspace Name | 
**owner_name** | **str** | Name of the owner of the workspace | 
**owner_email** | **str** | Email of the owner of the workspace | 
**role** | **str** | Role of the user in the workspace (A - Admin, E - Editor, M - Member, G - Guest) | 

## Example

```python
from flowhunt-python-sdk.models.workspace_role import WorkspaceRole

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRole from a JSON string
workspace_role_instance = WorkspaceRole.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRole.to_json())

# convert the object into a dict
workspace_role_dict = workspace_role_instance.to_dict()
# create an instance of WorkspaceRole from a dict
workspace_role_from_dict = WorkspaceRole.from_dict(workspace_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


