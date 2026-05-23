# AsanaWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_gid** | **str** |  | 
**workspace_name** | **str** |  | 
**integration_id** | **str** |  | 

## Example

```python
from flowhunt.models.asana_workspace_response import AsanaWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsanaWorkspaceResponse from a JSON string
asana_workspace_response_instance = AsanaWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(AsanaWorkspaceResponse.to_json())

# convert the object into a dict
asana_workspace_response_dict = asana_workspace_response_instance.to_dict()
# create an instance of AsanaWorkspaceResponse from a dict
asana_workspace_response_from_dict = AsanaWorkspaceResponse.from_dict(asana_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


