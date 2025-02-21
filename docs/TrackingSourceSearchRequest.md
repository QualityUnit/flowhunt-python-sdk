# TrackingSourceSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**source_type** | [**TrackingSourceTypes**](TrackingSourceTypes.md) |  | [optional] 
**click_id** | **str** |  | [optional] 
**click_id_name** | [**TrackingClickIdNames**](TrackingClickIdNames.md) |  | [optional] 
**utm_source** | **str** |  | [optional] 
**utm_medium** | **str** |  | [optional] 
**utm_campaign** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**include_expired** | **bool** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

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


