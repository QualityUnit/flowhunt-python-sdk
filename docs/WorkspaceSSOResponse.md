# WorkspaceSSOResponse

Response DTO for workspace SSO settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**provider** | **str** |  | 
**domain** | **str** |  | 
**enabled** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**idp_sso_url** | **str** |  | [optional] 
**idp_metadata_xml** | **str** |  | [optional] 
**idp_entity_id** | **str** |  | [optional] 
**idp_x509_cert** | **str** |  | [optional] 
**login_method** | **str** |  | [optional] 
**jit_provisioning_enabled** | **bool** |  | [optional] [default to False]
**email_attribute** | **str** |  | [optional] 
**name_id_format** | **str** |  | [optional] 
**assertion_consumer_service_url** | **str** |  | [optional] 
**first_name_attribute** | **str** |  | [optional] 
**last_name_attribute** | **str** |  | [optional] 
**role_attribute** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.workspace_sso_response import WorkspaceSSOResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSSOResponse from a JSON string
workspace_sso_response_instance = WorkspaceSSOResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSSOResponse.to_json())

# convert the object into a dict
workspace_sso_response_dict = workspace_sso_response_instance.to_dict()
# create an instance of WorkspaceSSOResponse from a dict
workspace_sso_response_from_dict = WorkspaceSSOResponse.from_dict(workspace_sso_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


