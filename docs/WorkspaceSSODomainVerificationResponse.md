# WorkspaceSSODomainVerificationResponse

Response model for domain verification records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**domain** | **str** |  | 
**nonce** | **str** |  | 
**verified** | **bool** |  | 
**verification_hash** | **str** |  | 
**created_at** | **datetime** |  | 
**last_verified_at** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.workspace_sso_domain_verification_response import WorkspaceSSODomainVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSSODomainVerificationResponse from a JSON string
workspace_sso_domain_verification_response_instance = WorkspaceSSODomainVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSSODomainVerificationResponse.to_json())

# convert the object into a dict
workspace_sso_domain_verification_response_dict = workspace_sso_domain_verification_response_instance.to_dict()
# create an instance of WorkspaceSSODomainVerificationResponse from a dict
workspace_sso_domain_verification_response_from_dict = WorkspaceSSODomainVerificationResponse.from_dict(workspace_sso_domain_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


