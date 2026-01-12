# FlowEventsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session ID | 
**event_id** | **str** | Event ID | 
**event_type** | [**MessageType**](MessageType.md) | Event type | 
**action_type** | [**FlowEventActionType**](FlowEventActionType.md) | Action type | 
**var_date** | **str** | Created at (format: YYYY-MM-DD HH:MM ) | [optional] 
**message_id** | **str** | Message ID | [optional] 
**message** | **str** | Message content | [optional] 

## Example

```python
from flowhunt.models.flow_events_search_response import FlowEventsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowEventsSearchResponse from a JSON string
flow_events_search_response_instance = FlowEventsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(FlowEventsSearchResponse.to_json())

# convert the object into a dict
flow_events_search_response_dict = flow_events_search_response_instance.to_dict()
# create an instance of FlowEventsSearchResponse from a dict
flow_events_search_response_from_dict = FlowEventsSearchResponse.from_dict(flow_events_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


