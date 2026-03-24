# WorkspaceUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | 
**email** | **str** | Email of the user | 
**name** | **str** | Name of the user | 
**avatar_url** | **str** | Avatar URL of the user | [optional] 
**role** | [**Role**](Role.md) | Role of the user (A - Admin, E - Editor, M - member, G - Guest) | 

## Example

```python
from flowhunt.models.workspace_user_response import WorkspaceUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserResponse from a JSON string
workspace_user_response_instance = WorkspaceUserResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserResponse.to_json())

# convert the object into a dict
workspace_user_response_dict = workspace_user_response_instance.to_dict()
# create an instance of WorkspaceUserResponse from a dict
workspace_user_response_from_dict = WorkspaceUserResponse.from_dict(workspace_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


