# GoogleAdsGroupsSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id | [optional] 
**campaign_id** | **str** | Campaign id | [optional] 
**group_id** | **str** | Group id | [optional] 
**group_name** | **str** | Group name | [optional] 
**language_code** | **str** | Language code | [optional] 
**country** | **str** | Country | [optional] 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) | Action type | [optional] 
**group_status** | [**GoogleAdsGroupStatus**](GoogleAdsGroupStatus.md) | Group status | [optional] 
**limit** | **int** | Limit of the search | [optional] [default to 50]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

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


