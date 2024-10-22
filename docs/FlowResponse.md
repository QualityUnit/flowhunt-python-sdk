# FlowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Flow ID | 
**name** | **str** | Flow name | 
**description** | **str** | Flow description | 
**flow_type** | [**FlowType**](FlowType.md) | Flow type | 
**component_count** | **int** | Component count | 
**executed_at** | **datetime** |  | [optional] 
**category_id** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.flow_response import FlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowResponse from a JSON string
flow_response_instance = FlowResponse.from_json(json)
# print the JSON string representation of the object
print(FlowResponse.to_json())

# convert the object into a dict
flow_response_dict = flow_response_instance.to_dict()
# create an instance of FlowResponse from a dict
flow_response_from_dict = FlowResponse.from_dict(flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


