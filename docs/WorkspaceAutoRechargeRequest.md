# WorkspaceAutoRechargeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether auto-recharge is enabled for this workspace. | 
**threshold** | **int** | Credit balance threshold that triggers a recharge. Required when enabled is true. | [optional] 
**amount** | **int** | Number of credits to add when threshold is crossed. Required when enabled is true. | [optional] 

## Example

```python
from flowhunt.models.workspace_auto_recharge_request import WorkspaceAutoRechargeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceAutoRechargeRequest from a JSON string
workspace_auto_recharge_request_instance = WorkspaceAutoRechargeRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceAutoRechargeRequest.to_json())

# convert the object into a dict
workspace_auto_recharge_request_dict = workspace_auto_recharge_request_instance.to_dict()
# create an instance of WorkspaceAutoRechargeRequest from a dict
workspace_auto_recharge_request_from_dict = WorkspaceAutoRechargeRequest.from_dict(workspace_auto_recharge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


