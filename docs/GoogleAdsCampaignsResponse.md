# GoogleAdsCampaignsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaigns** | [**List[GoogleAdsCampaignResponse]**](GoogleAdsCampaignResponse.md) | List of Google Ads Campaigns | 

## Example

```python
from flowhunt.models.google_ads_campaigns_response import GoogleAdsCampaignsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCampaignsResponse from a JSON string
google_ads_campaigns_response_instance = GoogleAdsCampaignsResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCampaignsResponse.to_json())

# convert the object into a dict
google_ads_campaigns_response_dict = google_ads_campaigns_response_instance.to_dict()
# create an instance of GoogleAdsCampaignsResponse from a dict
google_ads_campaigns_response_from_dict = GoogleAdsCampaignsResponse.from_dict(google_ads_campaigns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


