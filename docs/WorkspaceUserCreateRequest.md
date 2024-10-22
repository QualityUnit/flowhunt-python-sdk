# WorkspaceUserCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the user to add to the workspace | 
**role** | [**Role**](Role.md) | Role of the user in the workspace | 

## Example

```python
from flowhunt-python-sdk.models.workspace_user_create_request import WorkspaceUserCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserCreateRequest from a JSON string
workspace_user_create_request_instance = WorkspaceUserCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserCreateRequest.to_json())

# convert the object into a dict
workspace_user_create_request_dict = workspace_user_create_request_instance.to_dict()
# create an instance of WorkspaceUserCreateRequest from a dict
workspace_user_create_request_from_dict = WorkspaceUserCreateRequest.from_dict(workspace_user_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


