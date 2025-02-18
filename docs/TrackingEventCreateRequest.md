# TrackingEventCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | The name of the event | 
**unique_id** | **str** |  | [optional] 
**event_value** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**event_data** | [**List[TrackingEventData]**](TrackingEventData.md) |  | [optional] 
**link_ids** | **List[str]** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**conversion_action_id** | **str** |  | [optional] 
**include_in_conversions_metric** | **bool** |  | [optional] 
**with_address** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.tracking_event_create_request import TrackingEventCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventCreateRequest from a JSON string
tracking_event_create_request_instance = TrackingEventCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingEventCreateRequest.to_json())

# convert the object into a dict
tracking_event_create_request_dict = tracking_event_create_request_instance.to_dict()
# create an instance of TrackingEventCreateRequest from a dict
tracking_event_create_request_from_dict = TrackingEventCreateRequest.from_dict(tracking_event_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


