# FlowCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The flow name | 
**description** | **str** | The flow description | 
**detailed_description** | **str** |  | [optional] 
**config** | [**FlowConfig**](FlowConfig.md) | The flow configuration | 
**category_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_create import FlowCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCreate from a JSON string
flow_create_instance = FlowCreate.from_json(json)
# print the JSON string representation of the object
print(FlowCreate.to_json())

# convert the object into a dict
flow_create_dict = flow_create_instance.to_dict()
# create an instance of FlowCreate from a dict
flow_create_from_dict = FlowCreate.from_dict(flow_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


