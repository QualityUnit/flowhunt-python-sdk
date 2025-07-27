# WorkspaceSSOCreateRequest

Request DTO for creating workspace SSO settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | SSO provider (e.g., &#39;microsoft&#39;) | 
**enabled** | **bool** | Whether SSO is enabled | [optional] [default to True]
**idp_sso_url** | **str** | Identity Provider SSO URL | [optional] 
**jit_provisioning_enabled** | **bool** |  | [optional] 
**email_attribute** | **str** |  | [optional] 
**name_id_format** | **str** |  | [optional] 
**first_name_attribute** | **str** |  | [optional] 
**last_name_attribute** | **str** |  | [optional] 
**role_attribute** | **str** |  | [optional] 
**login_method** | [**SamlLoginMethod**](SamlLoginMethod.md) |  | [optional] 
**idp_metadata_xml** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.workspace_sso_create_request import WorkspaceSSOCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSSOCreateRequest from a JSON string
workspace_sso_create_request_instance = WorkspaceSSOCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSSOCreateRequest.to_json())

# convert the object into a dict
workspace_sso_create_request_dict = workspace_sso_create_request_instance.to_dict()
# create an instance of WorkspaceSSOCreateRequest from a dict
workspace_sso_create_request_from_dict = WorkspaceSSOCreateRequest.from_dict(workspace_sso_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


