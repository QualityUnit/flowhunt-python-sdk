# FlowVersionHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Flow ID | 
**name** | **str** | Flow name | 
**description** | **str** | Flow description | 
**flow_type** | [**FlowType**](FlowType.md) | Flow type | 
**executed_at** | **datetime** |  | [optional] 
**category_id** | **str** |  | [optional] 
**enable_cache** | **bool** | Enable cache | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**branch** | **str** | Flow branch | 
**created_at** | **datetime** |  | [optional] 
**commit_title** | **str** |  | [optional] 
**commit_description** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_version_history_response import FlowVersionHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowVersionHistoryResponse from a JSON string
flow_version_history_response_instance = FlowVersionHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(FlowVersionHistoryResponse.to_json())

# convert the object into a dict
flow_version_history_response_dict = flow_version_history_response_instance.to_dict()
# create an instance of FlowVersionHistoryResponse from a dict
flow_version_history_response_from_dict = FlowVersionHistoryResponse.from_dict(flow_version_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


