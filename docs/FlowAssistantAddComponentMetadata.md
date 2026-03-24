# FlowAssistantAddComponentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | Action ID | 
**component_id** | **str** | Component ID | 
**component_type** | **str** | Component name | 
**component_display_name** | **str** | Component display name | [optional] 
**component_icon** | **str** | Component icon | [optional] 
**parameter_values** | **Dict[str, object]** | Parameter values | [optional] 

## Example

```python
from flowhunt.models.flow_assistant_add_component_metadata import FlowAssistantAddComponentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantAddComponentMetadata from a JSON string
flow_assistant_add_component_metadata_instance = FlowAssistantAddComponentMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantAddComponentMetadata.to_json())

# convert the object into a dict
flow_assistant_add_component_metadata_dict = flow_assistant_add_component_metadata_instance.to_dict()
# create an instance of FlowAssistantAddComponentMetadata from a dict
flow_assistant_add_component_metadata_from_dict = FlowAssistantAddComponentMetadata.from_dict(flow_assistant_add_component_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


