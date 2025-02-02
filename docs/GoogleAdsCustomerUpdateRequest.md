# GoogleAdsCustomerUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | Language code | 
**country** | **str** | Country | 
**min_queries** | **int** | Min queries | 
**cluster_strength** | **int** | Cluster strength | 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action type | 

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


