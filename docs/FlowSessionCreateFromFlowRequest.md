# FlowSessionCreateFromFlowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**flow_id** | **str** | The flow ID | 

## Example

```python
from flowhunt.models.flow_session_create_from_flow_request import FlowSessionCreateFromFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionCreateFromFlowRequest from a JSON string
flow_session_create_from_flow_request_instance = FlowSessionCreateFromFlowRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionCreateFromFlowRequest.to_json())

# convert the object into a dict
flow_session_create_from_flow_request_dict = flow_session_create_from_flow_request_instance.to_dict()
# create an instance of FlowSessionCreateFromFlowRequest from a dict
flow_session_create_from_flow_request_from_dict = FlowSessionCreateFromFlowRequest.from_dict(flow_session_create_from_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


