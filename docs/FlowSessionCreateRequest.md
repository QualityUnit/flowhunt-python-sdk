# FlowSessionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**chatbot_id** | **str** | The chatbot ID | 

## Example

```python
from flowhunt-python-sdk.models.flow_session_create_request import FlowSessionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionCreateRequest from a JSON string
flow_session_create_request_instance = FlowSessionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionCreateRequest.to_json())

# convert the object into a dict
flow_session_create_request_dict = flow_session_create_request_instance.to_dict()
# create an instance of FlowSessionCreateRequest from a dict
flow_session_create_request_from_dict = FlowSessionCreateRequest.from_dict(flow_session_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


