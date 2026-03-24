# TrackingEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[TrackingEventResponse]**](TrackingEventResponse.md) |  | 

## Example

```python
from flowhunt.models.tracking_events_response import TrackingEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventsResponse from a JSON string
tracking_events_response_instance = TrackingEventsResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingEventsResponse.to_json())

# convert the object into a dict
tracking_events_response_dict = tracking_events_response_instance.to_dict()
# create an instance of TrackingEventsResponse from a dict
tracking_events_response_from_dict = TrackingEventsResponse.from_dict(tracking_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


