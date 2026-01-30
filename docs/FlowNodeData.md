# FlowNodeData

Node data structure for flow validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Component type (e.g., &#39;AgentGridSearch&#39;) | 
**node** | **Dict[str, object]** | Node configuration with template | [optional] 

## Example

```python
from flowhunt.models.flow_node_data import FlowNodeData

# TODO update the JSON string below
json = "{}"
# create an instance of FlowNodeData from a JSON string
flow_node_data_instance = FlowNodeData.from_json(json)
# print the JSON string representation of the object
print(FlowNodeData.to_json())

# convert the object into a dict
flow_node_data_dict = flow_node_data_instance.to_dict()
# create an instance of FlowNodeData from a dict
flow_node_data_from_dict = FlowNodeData.from_dict(flow_node_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


