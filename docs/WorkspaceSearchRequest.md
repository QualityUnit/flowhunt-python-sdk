# WorkspaceSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.workspace_search_request import WorkspaceSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSearchRequest from a JSON string
workspace_search_request_instance = WorkspaceSearchRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSearchRequest.to_json())

# convert the object into a dict
workspace_search_request_dict = workspace_search_request_instance.to_dict()
# create an instance of WorkspaceSearchRequest from a dict
workspace_search_request_from_dict = WorkspaceSearchRequest.from_dict(workspace_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


