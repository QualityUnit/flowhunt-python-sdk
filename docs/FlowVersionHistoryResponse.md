# FlowVersionHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Agent ID | 
**name** | **str** | Agent name | 
**description** | **str** | Agent description | 
**version_nr** | **int** | version number | [optional] 
**flow_type** | [**FlowType**](FlowType.md) | Agent type | 
**executed_at** | **datetime** | Executed at | [optional] 
**category_id** | **str** | The category ID | [optional] 
**enable_cache** | **bool** | Enable cache | 
**user** | [**UserResponse**](UserResponse.md) | User details | [optional] 
**branch** | **str** | Agent branch | 
**created_at** | **datetime** | Created at | [optional] 
**commit_title** | **str** | Commit title | [optional] 

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


