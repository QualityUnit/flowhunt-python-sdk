# GoogleAdsGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**customer_id** | **int** | Google Ads Customer ID | 
**campaign_id** | **int** | Google Ads Campaign ID | 
**group_id** | **int** | Google Ads Group | 
**group_name** | **str** | Google Ads Group Name | 
**group_status** | [**GoogleAdsGroupStatus**](GoogleAdsGroupStatus.md) | Group Status | 
**last_update** | **datetime** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action Type | 
**language_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**min_queries** | **int** |  | [optional] 
**cluster_strength** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_group_response import GoogleAdsGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsGroupResponse from a JSON string
google_ads_group_response_instance = GoogleAdsGroupResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsGroupResponse.to_json())

# convert the object into a dict
google_ads_group_response_dict = google_ads_group_response_instance.to_dict()
# create an instance of GoogleAdsGroupResponse from a dict
google_ads_group_response_from_dict = GoogleAdsGroupResponse.from_dict(google_ads_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


