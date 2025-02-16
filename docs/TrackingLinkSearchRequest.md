# TrackingLinkSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_link_id** | **str** |  | [optional] 
**dst_link_id** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**include_expired** | **bool** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_link_search_request import TrackingLinkSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingLinkSearchRequest from a JSON string
tracking_link_search_request_instance = TrackingLinkSearchRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingLinkSearchRequest.to_json())

# convert the object into a dict
tracking_link_search_request_dict = tracking_link_search_request_instance.to_dict()
# create an instance of TrackingLinkSearchRequest from a dict
tracking_link_search_request_from_dict = TrackingLinkSearchRequest.from_dict(tracking_link_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


