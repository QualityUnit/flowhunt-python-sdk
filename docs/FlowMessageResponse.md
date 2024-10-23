# FlowMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**session_id** | **str** | Session ID | 
**role** | [**FlowMessageRole**](FlowMessageRole.md) | Chat role | 
**created_at** | **datetime** | Created at | 
**message** | **str** | Message | 
**credits** | **int** | Credits | 

## Example

```python
from flowhunt.models.flow_message_response import FlowMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowMessageResponse from a JSON string
flow_message_response_instance = FlowMessageResponse.from_json(json)
# print the JSON string representation of the object
print(FlowMessageResponse.to_json())

# convert the object into a dict
flow_message_response_dict = flow_message_response_instance.to_dict()
# create an instance of FlowMessageResponse from a dict
flow_message_response_from_dict = FlowMessageResponse.from_dict(flow_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


