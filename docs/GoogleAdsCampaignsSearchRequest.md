# GoogleAdsCampaignsSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** |  | [optional] 
**campaign_id** | **int** |  | [optional] 
**campaign_name** | **str** |  | [optional] 
**campaign_status** | [**GoogleAdsCampaignStatus**](GoogleAdsCampaignStatus.md) |  | [optional] 
**language_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_campaigns_search_request import GoogleAdsCampaignsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCampaignsSearchRequest from a JSON string
google_ads_campaigns_search_request_instance = GoogleAdsCampaignsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCampaignsSearchRequest.to_json())

# convert the object into a dict
google_ads_campaigns_search_request_dict = google_ads_campaigns_search_request_instance.to_dict()
# create an instance of GoogleAdsCampaignsSearchRequest from a dict
google_ads_campaigns_search_request_from_dict = GoogleAdsCampaignsSearchRequest.from_dict(google_ads_campaigns_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


