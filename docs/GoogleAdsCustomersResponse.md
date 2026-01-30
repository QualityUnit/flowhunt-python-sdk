# GoogleAdsCustomersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**List[GoogleAdsCustomerResponse]**](GoogleAdsCustomerResponse.md) | List of Google Ads Customers | 

## Example

```python
from flowhunt.models.google_ads_customers_response import GoogleAdsCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsCustomersResponse from a JSON string
google_ads_customers_response_instance = GoogleAdsCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsCustomersResponse.to_json())

# convert the object into a dict
google_ads_customers_response_dict = google_ads_customers_response_instance.to_dict()
# create an instance of GoogleAdsCustomersResponse from a dict
google_ads_customers_response_from_dict = GoogleAdsCustomersResponse.from_dict(google_ads_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


