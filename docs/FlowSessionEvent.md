# FlowSessionEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**session_id** | **str** | Session ID | 
**event_id** | **str** | Event ID | 
**event_type** | [**MessageType**](MessageType.md) | Event type | 
**created_at_timestamp** | **str** | Created at | 
**action_type** | [**FlowEventActionType**](FlowEventActionType.md) | Action type | 
**credits** | **float** | Credits | 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**component_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_session_event import FlowSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionEvent from a JSON string
flow_session_event_instance = FlowSessionEvent.from_json(json)
# print the JSON string representation of the object
print(FlowSessionEvent.to_json())

# convert the object into a dict
flow_session_event_dict = flow_session_event_instance.to_dict()
# create an instance of FlowSessionEvent from a dict
flow_session_event_from_dict = FlowSessionEvent.from_dict(flow_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


