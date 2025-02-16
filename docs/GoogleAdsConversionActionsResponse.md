# GoogleAdsConversionActionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_actions** | [**List[GoogleAdsConversionAction]**](GoogleAdsConversionAction.md) | List of conversion actions | 

## Example

```python
from flowhunt.models.google_ads_conversion_actions_response import GoogleAdsConversionActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsConversionActionsResponse from a JSON string
google_ads_conversion_actions_response_instance = GoogleAdsConversionActionsResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsConversionActionsResponse.to_json())

# convert the object into a dict
google_ads_conversion_actions_response_dict = google_ads_conversion_actions_response_instance.to_dict()
# create an instance of GoogleAdsConversionActionsResponse from a dict
google_ads_conversion_actions_response_from_dict = GoogleAdsConversionActionsResponse.from_dict(google_ads_conversion_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


