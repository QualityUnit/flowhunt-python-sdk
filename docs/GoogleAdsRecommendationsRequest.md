# GoogleAdsRecommendationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id to get recommendations for | 
**campaign_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_recommendations_request import GoogleAdsRecommendationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsRecommendationsRequest from a JSON string
google_ads_recommendations_request_instance = GoogleAdsRecommendationsRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsRecommendationsRequest.to_json())

# convert the object into a dict
google_ads_recommendations_request_dict = google_ads_recommendations_request_instance.to_dict()
# create an instance of GoogleAdsRecommendationsRequest from a dict
google_ads_recommendations_request_from_dict = GoogleAdsRecommendationsRequest.from_dict(google_ads_recommendations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


