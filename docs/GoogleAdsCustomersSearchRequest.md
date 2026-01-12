# GoogleAdsCustomersSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id | [optional] 
**customer_name** | **str** | Customer name | [optional] 
**language_code** | **str** | Language code | [optional] 
**country** | **str** | Country | [optional] 
**min_queries** | **int** | Min queries | [optional] 
**min_clicks** | **int** | Min clicks | [optional] 
**process_negative_keywords** | [**BoolChar**](BoolChar.md) | Process negative keywords | [optional] 
**min_impressions** | **int** | Min impressions | [optional] 
**cluster_strength** | **int** | Cluster strength | [optional] 
**last_update** | **datetime** | Last update | [optional] 
**next_update** | **datetime** | Next update | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action type | [optional] 
**ga_measurement_id** | **str** | Google Analytics Measurement ID | [optional] 
**ga_api_secret** | **str** | Google Analytics API Secret | [optional] 

## Example

```python
from flowhunt.models.google_ads_customers_search_request import GoogleAdsCustomersSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCustomersSearchRequest from a JSON string
google_ads_customers_search_request_instance = GoogleAdsCustomersSearchRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCustomersSearchRequest.to_json())

# convert the object into a dict
google_ads_customers_search_request_dict = google_ads_customers_search_request_instance.to_dict()
# create an instance of GoogleAdsCustomersSearchRequest from a dict
google_ads_customers_search_request_from_dict = GoogleAdsCustomersSearchRequest.from_dict(google_ads_customers_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


