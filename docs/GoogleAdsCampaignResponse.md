# GoogleAdsCampaignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**customer_id** | **int** | Google Ads Customer ID | 
**campaign_id** | **int** | Google Ads Campaign ID | 
**campaign_name** | **str** | Google Ads Campaign Name | 
**campaign_status** | [**GoogleAdsCampaignStatus**](GoogleAdsCampaignStatus.md) | Campaign Status | 
**language_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**min_queries** | **int** |  | [optional] 
**cluster_strength** | **int** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action Type | 

## Example

```python
from flowhunt.models.google_ads_campaign_response import GoogleAdsCampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCampaignResponse from a JSON string
google_ads_campaign_response_instance = GoogleAdsCampaignResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCampaignResponse.to_json())

# convert the object into a dict
google_ads_campaign_response_dict = google_ads_campaign_response_instance.to_dict()
# create an instance of GoogleAdsCampaignResponse from a dict
google_ads_campaign_response_from_dict = GoogleAdsCampaignResponse.from_dict(google_ads_campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


