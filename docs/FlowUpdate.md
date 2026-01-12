# FlowUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The agent name | 
**description** | **str** | The agent description | 
**detailed_description** | **str** | The agent detailed description | [optional] 
**config** | [**FlowConfig**](FlowConfig.md) | The agent configuration | 
**category_id** | **str** | The category ID | [optional] 
**branch** | [**FlowBranch**](FlowBranch.md) | The agent branch | [optional] 
**enable_cache** | **bool** | Enable cache for the agent | [optional] [default to False]
**version_nr** | **int** | The agent version number | [optional] 

## Example

```python
from flowhunt.models.flow_update import FlowUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FlowUpdate from a JSON string
flow_update_instance = FlowUpdate.from_json(json)
# print the JSON string representation of the object
print(FlowUpdate.to_json())

# convert the object into a dict
flow_update_dict = flow_update_instance.to_dict()
# create an instance of FlowUpdate from a dict
flow_update_from_dict = FlowUpdate.from_dict(flow_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


