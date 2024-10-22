# FlowInvokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**human_input** | **str** | The human input | 
**variables** | **object** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.flow_invoke_request import FlowInvokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowInvokeRequest from a JSON string
flow_invoke_request_instance = FlowInvokeRequest.from_json(json)
# print the JSON string representation of the object
print(FlowInvokeRequest.to_json())

# convert the object into a dict
flow_invoke_request_dict = flow_invoke_request_instance.to_dict()
# create an instance of FlowInvokeRequest from a dict
flow_invoke_request_from_dict = FlowInvokeRequest.from_dict(flow_invoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


