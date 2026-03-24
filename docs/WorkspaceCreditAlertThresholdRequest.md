# WorkspaceCreditAlertThresholdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_alert_threshold** | **int** | Credit alert threshold for this workspace. When the credit balance drops to or below this amount, an email and in-app notification will be sent. Set to null to use the system default (10% of monthly plan value). Available to all plan tiers. | [optional] 

## Example

```python
from flowhunt.models.workspace_credit_alert_threshold_request import WorkspaceCreditAlertThresholdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreditAlertThresholdRequest from a JSON string
workspace_credit_alert_threshold_request_instance = WorkspaceCreditAlertThresholdRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreditAlertThresholdRequest.to_json())

# convert the object into a dict
workspace_credit_alert_threshold_request_dict = workspace_credit_alert_threshold_request_instance.to_dict()
# create an instance of WorkspaceCreditAlertThresholdRequest from a dict
workspace_credit_alert_threshold_request_from_dict = WorkspaceCreditAlertThresholdRequest.from_dict(workspace_credit_alert_threshold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


