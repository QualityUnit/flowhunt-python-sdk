# TrackingEventCreateRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[TrackingEventCreateRequest]**](TrackingEventCreateRequest.md) | The list of events to be created | 
**unique_id** | **str** |  | [optional] 
**fp** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**with_address** | **bool** |  | [optional] 
**ga** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_event_create_requests import TrackingEventCreateRequests

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventCreateRequests from a JSON string
tracking_event_create_requests_instance = TrackingEventCreateRequests.from_json(json)
# print the JSON string representation of the object
print(TrackingEventCreateRequests.to_json())

# convert the object into a dict
tracking_event_create_requests_dict = tracking_event_create_requests_instance.to_dict()
# create an instance of TrackingEventCreateRequests from a dict
tracking_event_create_requests_from_dict = TrackingEventCreateRequests.from_dict(tracking_event_create_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


