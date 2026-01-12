# FlowAssistantAddConnectionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | Action ID | 
**source_component_id** | **str** | Source component ID | 
**target_component_id** | **str** | Target component ID | 
**source_field_name** | **str** | Source field name | [optional] 
**target_field_name** | **str** | Target field name | [optional] 

## Example

```python
from flowhunt.models.flow_assistant_add_connection_metadata import FlowAssistantAddConnectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantAddConnectionMetadata from a JSON string
flow_assistant_add_connection_metadata_instance = FlowAssistantAddConnectionMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantAddConnectionMetadata.to_json())

# convert the object into a dict
flow_assistant_add_connection_metadata_dict = flow_assistant_add_connection_metadata_instance.to_dict()
# create an instance of FlowAssistantAddConnectionMetadata from a dict
flow_assistant_add_connection_metadata_from_dict = FlowAssistantAddConnectionMetadata.from_dict(flow_assistant_add_connection_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


