# GoogleAdsCustomersSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**min_queries** | **int** |  | [optional] 
**min_clicks** | **int** |  | [optional] 
**min_impressions** | **int** |  | [optional] 
**cluster_strength** | **int** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**next_update** | **datetime** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) |  | [optional] 
**ga_measurement_id** | **str** |  | [optional] 
**ga_api_secret** | **str** |  | [optional] 

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


