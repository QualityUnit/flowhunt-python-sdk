# GoogleAdsGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[GoogleAdsGroupResponse]**](GoogleAdsGroupResponse.md) | List of Google Ads Groups | 

## Example

```python
from flowhunt.models.google_ads_groups_response import GoogleAdsGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsGroupsResponse from a JSON string
google_ads_groups_response_instance = GoogleAdsGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsGroupsResponse.to_json())

# convert the object into a dict
google_ads_groups_response_dict = google_ads_groups_response_instance.to_dict()
# create an instance of GoogleAdsGroupsResponse from a dict
google_ads_groups_response_from_dict = GoogleAdsGroupsResponse.from_dict(google_ads_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


