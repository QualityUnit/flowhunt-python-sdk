# FlowConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **List[object]** | The agent nodes | 
**edges** | **List[object]** | The agent edges | 

## Example

```python
from flowhunt.models.flow_config import FlowConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FlowConfig from a JSON string
flow_config_instance = FlowConfig.from_json(json)
# print the JSON string representation of the object
print(FlowConfig.to_json())

# convert the object into a dict
flow_config_dict = flow_config_instance.to_dict()
# create an instance of FlowConfig from a dict
flow_config_from_dict = FlowConfig.from_dict(flow_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


