# MicrosoftPowerBiWorkspacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[MicrosoftPowerBiWorkspaceResponse]**](MicrosoftPowerBiWorkspaceResponse.md) |  | 

## Example

```python
from flowhunt.models.microsoft_power_bi_workspaces_response import MicrosoftPowerBiWorkspacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPowerBiWorkspacesResponse from a JSON string
microsoft_power_bi_workspaces_response_instance = MicrosoftPowerBiWorkspacesResponse.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPowerBiWorkspacesResponse.to_json())

# convert the object into a dict
microsoft_power_bi_workspaces_response_dict = microsoft_power_bi_workspaces_response_instance.to_dict()
# create an instance of MicrosoftPowerBiWorkspacesResponse from a dict
microsoft_power_bi_workspaces_response_from_dict = MicrosoftPowerBiWorkspacesResponse.from_dict(microsoft_power_bi_workspaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


