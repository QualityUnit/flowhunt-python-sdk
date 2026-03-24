# BrandingUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding_logo_url** | **str** |  | [optional] 
**brand_avatar_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**dashboard_primary_color** | **str** |  | [optional] 
**dashboard_secondary_color** | **str** |  | [optional] 
**show_ads_ai** | **bool** |  | [optional] 
**show_photomatic_ai** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.branding_update_request import BrandingUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingUpdateRequest from a JSON string
branding_update_request_instance = BrandingUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BrandingUpdateRequest.to_json())

# convert the object into a dict
branding_update_request_dict = branding_update_request_instance.to_dict()
# create an instance of BrandingUpdateRequest from a dict
branding_update_request_from_dict = BrandingUpdateRequest.from_dict(branding_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


