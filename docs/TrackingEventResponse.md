# TrackingEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**unique_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**event_value** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**include_in_conversions_metric** | **bool** |  | [optional] 
**event_data** | [**List[TrackingEventData]**](TrackingEventData.md) |  | [optional] 
**link_ids** | **List[object]** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_event_response import TrackingEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventResponse from a JSON string
tracking_event_response_instance = TrackingEventResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingEventResponse.to_json())

# convert the object into a dict
tracking_event_response_dict = tracking_event_response_instance.to_dict()
# create an instance of TrackingEventResponse from a dict
tracking_event_response_from_dict = TrackingEventResponse.from_dict(tracking_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


