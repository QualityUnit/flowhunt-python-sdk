# GoogleAdsGroupsSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** |  | [optional] 
**campaign_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) |  | [optional] 

## Example

```python
from flowhunt.models.google_ads_groups_search_request import GoogleAdsGroupsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsGroupsSearchRequest from a JSON string
google_ads_groups_search_request_instance = GoogleAdsGroupsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsGroupsSearchRequest.to_json())

# convert the object into a dict
google_ads_groups_search_request_dict = google_ads_groups_search_request_instance.to_dict()
# create an instance of GoogleAdsGroupsSearchRequest from a dict
google_ads_groups_search_request_from_dict = GoogleAdsGroupsSearchRequest.from_dict(google_ads_groups_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


