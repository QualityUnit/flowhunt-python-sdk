# GoogleAdsAnalyzeKeywordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**date_from** | **date** |  | [optional] 
**force_update** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_analyze_keywords_request import GoogleAdsAnalyzeKeywordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsAnalyzeKeywordsRequest from a JSON string
google_ads_analyze_keywords_request_instance = GoogleAdsAnalyzeKeywordsRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsAnalyzeKeywordsRequest.to_json())

# convert the object into a dict
google_ads_analyze_keywords_request_dict = google_ads_analyze_keywords_request_instance.to_dict()
# create an instance of GoogleAdsAnalyzeKeywordsRequest from a dict
google_ads_analyze_keywords_request_from_dict = GoogleAdsAnalyzeKeywordsRequest.from_dict(google_ads_analyze_keywords_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


