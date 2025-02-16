# GoogleAdsGroupUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** |  | 
**country** | **str** |  | 
**action_type** | [**GoogleAdsActionType**](GoogleAdsActionType.md) |  | 

## Example

```python
from flowhunt.models.google_ads_group_update_request import GoogleAdsGroupUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsGroupUpdateRequest from a JSON string
google_ads_group_update_request_instance = GoogleAdsGroupUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsGroupUpdateRequest.to_json())

# convert the object into a dict
google_ads_group_update_request_dict = google_ads_group_update_request_instance.to_dict()
# create an instance of GoogleAdsGroupUpdateRequest from a dict
google_ads_group_update_request_from_dict = GoogleAdsGroupUpdateRequest.from_dict(google_ads_group_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


