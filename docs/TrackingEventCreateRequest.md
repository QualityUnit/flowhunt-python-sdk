# TrackingEventCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | The name of the event | 
**unique_id** | **str** | The unique ID of the event, if more events will be recorded with the same ID, they will be ignored | [optional] 
**event_value** | **float** | The value of the event | [optional] 
**currency** | **str** | Currency associated with the conversion value. This is the ISO 4217 3-character currency code. For example: USD, EUR. | [optional] [default to 'USD']
**event_data** | [**List[TrackingEventData]**](TrackingEventData.md) | The data of the event | [optional] 
**link_ids** | **List[str]** | The link ID of the event | [optional] 
**valid_until** | **datetime** | The date until the event is valid | [optional] 
**conversion_action_id** | **str** | The conversion action ID (Google Ads) - not used anymore, functionality removed | [optional] 
**include_in_conversions_metric** | **bool** | The flag to indicate if the event should be included in the conversions metric | [optional] [default to True]
**url** | **str** | The URL of the page where the event was recorded | [optional] 

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


