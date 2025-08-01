# GoogleAdsCustomerUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**min_queries** | **int** |  | [optional] 
**cluster_strength** | **int** |  | [optional] 
**min_impressions** | **int** |  | [optional] 
**min_clicks** | **int** |  | [optional] 
**process_negative_keywords** | [**BoolChar**](BoolChar.md) |  | [optional] 
**cron_settings** | **str** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) |  | [optional] 
**ga_measurement_id** | **str** |  | [optional] 
**ga_api_secret** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_customer_update_request import GoogleAdsCustomerUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCustomerUpdateRequest from a JSON string
google_ads_customer_update_request_instance = GoogleAdsCustomerUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCustomerUpdateRequest.to_json())

# convert the object into a dict
google_ads_customer_update_request_dict = google_ads_customer_update_request_instance.to_dict()
# create an instance of GoogleAdsCustomerUpdateRequest from a dict
google_ads_customer_update_request_from_dict = GoogleAdsCustomerUpdateRequest.from_dict(google_ads_customer_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


