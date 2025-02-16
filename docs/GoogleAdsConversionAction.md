# GoogleAdsConversionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the conversion action | 
**name** | **str** | The name of the conversion action | 

## Example

```python
from flowhunt.models.google_ads_conversion_action import GoogleAdsConversionAction

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsConversionAction from a JSON string
google_ads_conversion_action_instance = GoogleAdsConversionAction.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsConversionAction.to_json())

# convert the object into a dict
google_ads_conversion_action_dict = google_ads_conversion_action_instance.to_dict()
# create an instance of GoogleAdsConversionAction from a dict
google_ads_conversion_action_from_dict = GoogleAdsConversionAction.from_dict(google_ads_conversion_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


