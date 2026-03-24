# GoogleAdsCampaignUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | Language code, if None, value is inherited from customer | 
**country** | **str** | Country, if None, value is inherited from customer | 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action type, if None, value is inherited from customer | 

## Example

```python
from flowhunt.models.google_ads_campaign_update_request import GoogleAdsCampaignUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCampaignUpdateRequest from a JSON string
google_ads_campaign_update_request_instance = GoogleAdsCampaignUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCampaignUpdateRequest.to_json())

# convert the object into a dict
google_ads_campaign_update_request_dict = google_ads_campaign_update_request_instance.to_dict()
# create an instance of GoogleAdsCampaignUpdateRequest from a dict
google_ads_campaign_update_request_from_dict = GoogleAdsCampaignUpdateRequest.from_dict(google_ads_campaign_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


