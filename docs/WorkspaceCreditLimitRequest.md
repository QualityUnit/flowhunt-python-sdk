# WorkspaceCreditLimitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_limit** | **int** | Credit consumption limit for this workspace (null to remove the limit). Only available for PRO, AGENCY, and ENTERPRISE subscription plans. | [optional] 

## Example

```python
from flowhunt.models.workspace_credit_limit_request import WorkspaceCreditLimitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreditLimitRequest from a JSON string
workspace_credit_limit_request_instance = WorkspaceCreditLimitRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreditLimitRequest.to_json())

# convert the object into a dict
workspace_credit_limit_request_dict = workspace_credit_limit_request_instance.to_dict()
# create an instance of WorkspaceCreditLimitRequest from a dict
workspace_credit_limit_request_from_dict = WorkspaceCreditLimitRequest.from_dict(workspace_credit_limit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


