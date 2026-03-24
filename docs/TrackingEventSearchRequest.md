# TrackingEventSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | Filter by event name | [optional] 
**from_date** | **datetime** | Filter events created after this date | [optional] 
**to_date** | **datetime** | Filter events created before this date | [optional] 
**include_expired** | **bool** | Include expired events | [optional] [default to False]
**page** | **int** | Page number | [optional] [default to 1]
**page_size** | **int** | Number of items per page | [optional] [default to 20]

## Example

```python
from flowhunt.models.tracking_event_search_request import TrackingEventSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventSearchRequest from a JSON string
tracking_event_search_request_instance = TrackingEventSearchRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingEventSearchRequest.to_json())

# convert the object into a dict
tracking_event_search_request_dict = tracking_event_search_request_instance.to_dict()
# create an instance of TrackingEventSearchRequest from a dict
tracking_event_search_request_from_dict = TrackingEventSearchRequest.from_dict(tracking_event_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


