# GoogleAdsSourceTrackingCodeExample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The ID of the customer | 
**customer_name** | **str** | The name of the customer | 
**tracking_code** | **str** | Example tracking code using our JS library | 
**description** | **str** | Description of when to use this tracking code | 

## Example

```python
from flowhunt.models.google_ads_source_tracking_code_example import GoogleAdsSourceTrackingCodeExample

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsSourceTrackingCodeExample from a JSON string
google_ads_source_tracking_code_example_instance = GoogleAdsSourceTrackingCodeExample.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsSourceTrackingCodeExample.to_json())

# convert the object into a dict
google_ads_source_tracking_code_example_dict = google_ads_source_tracking_code_example_instance.to_dict()
# create an instance of GoogleAdsSourceTrackingCodeExample from a dict
google_ads_source_tracking_code_example_from_dict = GoogleAdsSourceTrackingCodeExample.from_dict(google_ads_source_tracking_code_example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


