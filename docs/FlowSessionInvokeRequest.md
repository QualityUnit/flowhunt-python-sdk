# FlowSessionInvokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message | 
**post_back_url** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_session_invoke_request import FlowSessionInvokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionInvokeRequest from a JSON string
flow_session_invoke_request_instance = FlowSessionInvokeRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionInvokeRequest.to_json())

# convert the object into a dict
flow_session_invoke_request_dict = flow_session_invoke_request_instance.to_dict()
# create an instance of FlowSessionInvokeRequest from a dict
flow_session_invoke_request_from_dict = FlowSessionInvokeRequest.from_dict(flow_session_invoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


