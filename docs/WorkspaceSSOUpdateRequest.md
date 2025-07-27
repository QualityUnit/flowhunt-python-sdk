# WorkspaceSSOUpdateRequest

Request DTO for updating workspace SSO settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether SSO is enabled | [optional] [default to True]
**idp_sso_url** | **str** |  | [optional] 
**idp_entity_id** | **str** |  | [optional] 
**idp_x509_cert** | **str** |  | [optional] 
**jit_provisioning_enabled** | **bool** | Enable Just-In-Time user provisioning | [optional] [default to False]
**email_attribute** | **str** |  | [optional] 
**name_id_format** | **str** |  | [optional] 
**first_name_attribute** | **str** |  | [optional] 
**last_name_attribute** | **str** |  | [optional] 
**role_attribute** | **str** |  | [optional] 
**login_method** | [**SamlLoginMethod**](SamlLoginMethod.md) |  | [optional] 
**idp_metadata_xml** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.workspace_sso_update_request import WorkspaceSSOUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSSOUpdateRequest from a JSON string
workspace_sso_update_request_instance = WorkspaceSSOUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSSOUpdateRequest.to_json())

# convert the object into a dict
workspace_sso_update_request_dict = workspace_sso_update_request_instance.to_dict()
# create an instance of WorkspaceSSOUpdateRequest from a dict
workspace_sso_update_request_from_dict = WorkspaceSSOUpdateRequest.from_dict(workspace_sso_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


