# MicrosoftPowerBiWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**workspace_name** | **str** | Workspace name | 

## Example

```python
from flowhunt.models.microsoft_power_bi_workspace_response import MicrosoftPowerBiWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPowerBiWorkspaceResponse from a JSON string
microsoft_power_bi_workspace_response_instance = MicrosoftPowerBiWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPowerBiWorkspaceResponse.to_json())

# convert the object into a dict
microsoft_power_bi_workspace_response_dict = microsoft_power_bi_workspace_response_instance.to_dict()
# create an instance of MicrosoftPowerBiWorkspaceResponse from a dict
microsoft_power_bi_workspace_response_from_dict = MicrosoftPowerBiWorkspaceResponse.from_dict(microsoft_power_bi_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


