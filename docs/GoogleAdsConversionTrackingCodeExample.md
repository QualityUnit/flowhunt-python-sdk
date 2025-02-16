# GoogleAdsConversionTrackingCodeExample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_action_id** | **int** | The ID of the conversion action | 
**conversion_action_name** | **str** | The name of the conversion action | 
**tracking_code** | **str** | Example tracking code using our JS library | 
**description** | **str** | Description of when to use this tracking code | 

## Example

```python
from flowhunt.models.google_ads_conversion_tracking_code_example import GoogleAdsConversionTrackingCodeExample

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsConversionTrackingCodeExample from a JSON string
google_ads_conversion_tracking_code_example_instance = GoogleAdsConversionTrackingCodeExample.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsConversionTrackingCodeExample.to_json())

# convert the object into a dict
google_ads_conversion_tracking_code_example_dict = google_ads_conversion_tracking_code_example_instance.to_dict()
# create an instance of GoogleAdsConversionTrackingCodeExample from a dict
google_ads_conversion_tracking_code_example_from_dict = GoogleAdsConversionTrackingCodeExample.from_dict(google_ads_conversion_tracking_code_example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


