# FlowBatchColumnDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Column display name | 
**key** | **str** | Column variable key (used as flow variable) | 

## Example

```python
from flowhunt.models.flow_batch_column_definition import FlowBatchColumnDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchColumnDefinition from a JSON string
flow_batch_column_definition_instance = FlowBatchColumnDefinition.from_json(json)
# print the JSON string representation of the object
print(FlowBatchColumnDefinition.to_json())

# convert the object into a dict
flow_batch_column_definition_dict = flow_batch_column_definition_instance.to_dict()
# create an instance of FlowBatchColumnDefinition from a dict
flow_batch_column_definition_from_dict = FlowBatchColumnDefinition.from_dict(flow_batch_column_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


