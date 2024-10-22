# WorkspaceUsersSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](Role.md) |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.workspace_users_search_request import WorkspaceUsersSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUsersSearchRequest from a JSON string
workspace_users_search_request_instance = WorkspaceUsersSearchRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUsersSearchRequest.to_json())

# convert the object into a dict
workspace_users_search_request_dict = workspace_users_search_request_instance.to_dict()
# create an instance of WorkspaceUsersSearchRequest from a dict
workspace_users_search_request_from_dict = WorkspaceUsersSearchRequest.from_dict(workspace_users_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


