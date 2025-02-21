# GoogleAdsCustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**customer_id** | **str** | Google Ads Customer ID | 
**customer_name** | **str** | Google Ads Customer Name | 
**language_code** | **str** | Language Code | 
**country** | **str** | Country Code | 
**min_queries** | **int** | Minimum Queries | 
**cluster_strength** | **int** | Cluster Strength | 
**min_impressions** | **int** | Minimum Impressions | 
**min_clicks** | **int** | Minimum Clicks | 
**last_update** | **datetime** |  | [optional] 
**next_update** | **datetime** |  | [optional] 
**cron_settings** | **str** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action Type | 
**ga_measurement_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_customer_response import GoogleAdsCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCustomerResponse from a JSON string
google_ads_customer_response_instance = GoogleAdsCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCustomerResponse.to_json())

# convert the object into a dict
google_ads_customer_response_dict = google_ads_customer_response_instance.to_dict()
# create an instance of GoogleAdsCustomerResponse from a dict
google_ads_customer_response_from_dict = GoogleAdsCustomerResponse.from_dict(google_ads_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


