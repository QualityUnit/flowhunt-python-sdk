# GoogleAdsKeywordRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**customer_id** | **str** | Customer ID | 
**campaign_id** | **str** | Campaign ID | 
**campaign_name** | **str** | Campaign Name | 
**group_id** | **str** | Group ID | 
**group_name** | **str** | Group Name | 
**keyword_id** | **str** | Keyword ID | 
**keyword** | **str** | Keyword | 
**created_at** | **datetime** | Created At | [optional] 
**recommendations** | [**List[GoogleAdsRecommendation]**](GoogleAdsRecommendation.md) | Recommendet actions | [optional] [default to []]

## Example

```python
from flowhunt.models.google_ads_keyword_recommendation import GoogleAdsKeywordRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsKeywordRecommendation from a JSON string
google_ads_keyword_recommendation_instance = GoogleAdsKeywordRecommendation.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsKeywordRecommendation.to_json())

# convert the object into a dict
google_ads_keyword_recommendation_dict = google_ads_keyword_recommendation_instance.to_dict()
# create an instance of GoogleAdsKeywordRecommendation from a dict
google_ads_keyword_recommendation_from_dict = GoogleAdsKeywordRecommendation.from_dict(google_ads_keyword_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


