# GoogleAdsRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_type** | [**GoogleAdsRecommendationType**](GoogleAdsRecommendationType.md) |  | 
**campaign_id** | **str** |  | 
**campaign_name** | **str** |  | [optional] 
**group_id** | **str** |  | 
**group_name** | **str** |  | [optional] 
**action_status** | [**GoogleAdsRecommendationStatus**](GoogleAdsRecommendationStatus.md) |  | 
**confidence** | [**GoogleAdsRecommendationConfidence**](GoogleAdsRecommendationConfidence.md) |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_recommendation import GoogleAdsRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsRecommendation from a JSON string
google_ads_recommendation_instance = GoogleAdsRecommendation.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsRecommendation.to_json())

# convert the object into a dict
google_ads_recommendation_dict = google_ads_recommendation_instance.to_dict()
# create an instance of GoogleAdsRecommendation from a dict
google_ads_recommendation_from_dict = GoogleAdsRecommendation.from_dict(google_ads_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


