# TrackingSourceSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Filter by customer ID | [optional] 
**source_type** | [**TrackingSourceTypes**](TrackingSourceTypes.md) | Filter by source type | [optional] 
**click_id** | **str** | Filter by click ID | [optional] 
**click_id_name** | [**TrackingClickIdNames**](TrackingClickIdNames.md) | Filter by click ID name | [optional] 
**utm_source** | **str** | Filter by UTM source | [optional] 
**utm_medium** | **str** | Filter by UTM medium | [optional] 
**utm_campaign** | **str** | Filter by UTM campaign | [optional] 
**utm_channel** | **str** | Filter by UTM channel | [optional] 
**from_date** | **datetime** | Filter sources created after this date | [optional] 
**to_date** | **datetime** | Filter sources created before this date | [optional] 
**include_expired** | **bool** | Include expired sources | [optional] [default to False]
**page** | **int** | Page number | [optional] [default to 1]
**page_size** | **int** | Number of items per page | [optional] [default to 20]

## Example

```python
from flowhunt.models.tracking_source_search_request import TrackingSourceSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingSourceSearchRequest from a JSON string
tracking_source_search_request_instance = TrackingSourceSearchRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingSourceSearchRequest.to_json())

# convert the object into a dict
tracking_source_search_request_dict = tracking_source_search_request_instance.to_dict()
# create an instance of TrackingSourceSearchRequest from a dict
tracking_source_search_request_from_dict = TrackingSourceSearchRequest.from_dict(tracking_source_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


