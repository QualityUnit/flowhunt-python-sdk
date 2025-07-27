# WorkspaceSSODomainVerificationCreateRequest

Request model for creating a new domain verification record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name to verify (e.g., example.com) | 

## Example

```python
from flowhunt.models.workspace_sso_domain_verification_create_request import WorkspaceSSODomainVerificationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSSODomainVerificationCreateRequest from a JSON string
workspace_sso_domain_verification_create_request_instance = WorkspaceSSODomainVerificationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSSODomainVerificationCreateRequest.to_json())

# convert the object into a dict
workspace_sso_domain_verification_create_request_dict = workspace_sso_domain_verification_create_request_instance.to_dict()
# create an instance of WorkspaceSSODomainVerificationCreateRequest from a dict
workspace_sso_domain_verification_create_request_from_dict = WorkspaceSSODomainVerificationCreateRequest.from_dict(workspace_sso_domain_verification_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


