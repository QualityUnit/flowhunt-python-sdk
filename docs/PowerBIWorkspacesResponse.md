# PowerBIWorkspacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[PowerBIWorkspaceResponse]**](PowerBIWorkspaceResponse.md) |  | 

## Example

```python
from flowhunt.models.power_bi_workspaces_response import PowerBIWorkspacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBIWorkspacesResponse from a JSON string
power_bi_workspaces_response_instance = PowerBIWorkspacesResponse.from_json(json)
# print the JSON string representation of the object
print(PowerBIWorkspacesResponse.to_json())

# convert the object into a dict
power_bi_workspaces_response_dict = power_bi_workspaces_response_instance.to_dict()
# create an instance of PowerBIWorkspacesResponse from a dict
power_bi_workspaces_response_from_dict = PowerBIWorkspacesResponse.from_dict(power_bi_workspaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


