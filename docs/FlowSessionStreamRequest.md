# FlowSessionStreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[FlowSessionMessage]**](FlowSessionMessage.md) | The flow messages | 

## Example

```python
from flowhunt-python-sdk.models.flow_session_stream_request import FlowSessionStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionStreamRequest from a JSON string
flow_session_stream_request_instance = FlowSessionStreamRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionStreamRequest.to_json())

# convert the object into a dict
flow_session_stream_request_dict = flow_session_stream_request_instance.to_dict()
# create an instance of FlowSessionStreamRequest from a dict
flow_session_stream_request_from_dict = FlowSessionStreamRequest.from_dict(flow_session_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


