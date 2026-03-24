# WorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**name** | **str** | Name of the workspace | 
**credit_limit** | **int** | Credit consumption limit for this workspace (Premium/Enterprise only). None means no limit. | [optional] 
**credits_consumed** | **int** | Credits consumed in this workspace during the current billing period. Only present when credit_limit is set. | [optional] 
**credit_alert_threshold** | **int** | Credit alert threshold. When credit balance drops to or below this amount, notifications are sent. None means the system default (10% of monthly plan value) is used. | [optional] 

## Example

```python
from flowhunt.models.workspace_response import WorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceResponse from a JSON string
workspace_response_instance = WorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceResponse.to_json())

# convert the object into a dict
workspace_response_dict = workspace_response_instance.to_dict()
# create an instance of WorkspaceResponse from a dict
workspace_response_from_dict = WorkspaceResponse.from_dict(workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


