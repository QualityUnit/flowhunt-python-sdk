# FlowEventsSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search term for metadata.message | [optional] 
**start_date** | **datetime** | The start date | [optional] 
**end_date** | **datetime** | The end date | [optional] 

## Example

```python
from flowhunt.models.flow_events_search_request import FlowEventsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowEventsSearchRequest from a JSON string
flow_events_search_request_instance = FlowEventsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FlowEventsSearchRequest.to_json())

# convert the object into a dict
flow_events_search_request_dict = flow_events_search_request_instance.to_dict()
# create an instance of FlowEventsSearchRequest from a dict
flow_events_search_request_from_dict = FlowEventsSearchRequest.from_dict(flow_events_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


