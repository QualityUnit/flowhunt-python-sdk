# GoogleAdsConversionTrackingSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_ads_conversion_customer** | **str** | The Google Ads conversion customer | 
**conversion_tracking_status** | [**GoogleAdsConversionTrackingStatusEnum**](GoogleAdsConversionTrackingStatusEnum.md) | The conversion tracking status | 
**conversion_tracking_id** | **int** | The conversion tracking ID | 
**cross_account_conversion_tracking_id** | **int** | The cross-account conversion tracking ID | 

## Example

```python
from flowhunt.models.google_ads_conversion_tracking_settings_response import GoogleAdsConversionTrackingSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsConversionTrackingSettingsResponse from a JSON string
google_ads_conversion_tracking_settings_response_instance = GoogleAdsConversionTrackingSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsConversionTrackingSettingsResponse.to_json())

# convert the object into a dict
google_ads_conversion_tracking_settings_response_dict = google_ads_conversion_tracking_settings_response_instance.to_dict()
# create an instance of GoogleAdsConversionTrackingSettingsResponse from a dict
google_ads_conversion_tracking_settings_response_from_dict = GoogleAdsConversionTrackingSettingsResponse.from_dict(google_ads_conversion_tracking_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


