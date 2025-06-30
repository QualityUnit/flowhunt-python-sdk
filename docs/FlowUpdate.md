# FlowUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The flow name | 
**description** | **str** | The flow description | 
**detailed_description** | **str** |  | [optional] 
**config** | [**FlowConfig**](FlowConfig.md) | The flow configuration | 
**category_id** | **str** |  | [optional] 
**branch** | [**FlowBranch**](FlowBranch.md) | The flow branch | [optional] 
**enable_cache** | **bool** |  | [optional] 
**version_nr** | **int** |  | [optional] 

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


