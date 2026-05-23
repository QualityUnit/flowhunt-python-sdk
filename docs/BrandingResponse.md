# BrandingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding_logo_url** | **str** |  | [optional] 
**brand_avatar_url** | **str** |  | [optional] 
**dashboard_primary_color** | **str** |  | [optional] 
**dashboard_secondary_color** | **str** |  | [optional] 
**show_ads_ai** | **bool** |  | [optional] [default to True]
**show_photomatic_ai** | **bool** |  | [optional] [default to True]
**show_ai_factory** | **bool** |  | [optional] [default to True]
**custom_my_agents_label** | **str** |  | [optional] 
**custom_my_assistants_label** | **str** |  | [optional] 
**custom_active_services_label** | **str** |  | [optional] 
**custom_more_label** | **str** |  | [optional] 
**custom_agents_search_label** | **str** |  | [optional] 
**custom_no_agents_label** | **str** |  | [optional] 
**custom_agent_column_label** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**smtp_host** | **str** |  | [optional] 
**smtp_port** | **int** |  | [optional] 
**smtp_encryption** | [**SmtpEncryption**](SmtpEncryption.md) |  | [optional] 
**smtp_sender_email** | **str** |  | [optional] 
**smtp_password_is_set** | **bool** |  | [optional] [default to False]
**custom_domain** | **str** |  | [optional] 
**custom_domain_status** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.branding_response import BrandingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingResponse from a JSON string
branding_response_instance = BrandingResponse.from_json(json)
# print the JSON string representation of the object
print(BrandingResponse.to_json())

# convert the object into a dict
branding_response_dict = branding_response_instance.to_dict()
# create an instance of BrandingResponse from a dict
branding_response_from_dict = BrandingResponse.from_dict(branding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


