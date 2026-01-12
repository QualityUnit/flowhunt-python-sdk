# GoogleAdsKeywordAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id | 
**campaign_id** | **str** | Campaign id | 
**group_id** | **str** | Group id | 
**keywords** | **List[str]** | List of keywords to add | 
**is_negative** | **bool** | Is negative keyword | [optional] [default to False]
**match_type** | [**GoogleAdsMatchType**](GoogleAdsMatchType.md) | Match type | 

## Example

```python
from flowhunt.models.google_ads_keyword_add_request import GoogleAdsKeywordAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsKeywordAddRequest from a JSON string
google_ads_keyword_add_request_instance = GoogleAdsKeywordAddRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsKeywordAddRequest.to_json())

# convert the object into a dict
google_ads_keyword_add_request_dict = google_ads_keyword_add_request_instance.to_dict()
# create an instance of GoogleAdsKeywordAddRequest from a dict
google_ads_keyword_add_request_from_dict = GoogleAdsKeywordAddRequest.from_dict(google_ads_keyword_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


