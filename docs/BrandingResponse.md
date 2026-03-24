# BrandingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding_logo_url** | **str** |  | [optional] 
**brand_avatar_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] [default to '']
**dashboard_primary_color** | **str** |  | [optional] 
**dashboard_secondary_color** | **str** |  | [optional] 
**show_ads_ai** | **bool** |  | [optional] [default to True]
**show_photomatic_ai** | **bool** |  | [optional] [default to True]

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


