# WorkspaceSSOListResponse

Response DTO for list of workspace SSO settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WorkspaceSSOResponse]**](WorkspaceSSOResponse.md) |  | 

## Example

```python
from flowhunt.models.workspace_sso_list_response import WorkspaceSSOListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSSOListResponse from a JSON string
workspace_sso_list_response_instance = WorkspaceSSOListResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSSOListResponse.to_json())

# convert the object into a dict
workspace_sso_list_response_dict = workspace_sso_list_response_instance.to_dict()
# create an instance of WorkspaceSSOListResponse from a dict
workspace_sso_list_response_from_dict = WorkspaceSSOListResponse.from_dict(workspace_sso_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


