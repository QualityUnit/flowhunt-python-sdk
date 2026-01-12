# FlowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Agent ID | 
**name** | **str** | Agent name | 
**description** | **str** | Agent description | 
**flow_type** | [**FlowType**](FlowType.md) | Agent type | 
**component_count** | **int** | Component count | 
**executed_at** | **datetime** | Executed at | [optional] 
**category_id** | **str** | The category ID | [optional] 
**enable_cache** | **bool** | Enable cache | 
**last_modified** | **datetime** | Last modified | [optional] 

## Example

```python
from flowhunt.models.flow_response import FlowResponse

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


