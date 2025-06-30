# TrackingEventData

Value object for tracking event data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value_text** | **str** |  | [optional] 
**value_number** | **float** |  | [optional] 
**value_boolean** | **bool** |  | [optional] 
**value_datetime** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_event_data import TrackingEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventData from a JSON string
tracking_event_data_instance = TrackingEventData.from_json(json)
# print the JSON string representation of the object
print(TrackingEventData.to_json())

# convert the object into a dict
tracking_event_data_dict = tracking_event_data_instance.to_dict()
# create an instance of TrackingEventData from a dict
tracking_event_data_from_dict = TrackingEventData.from_dict(tracking_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


