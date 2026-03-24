# FlowAssistantDeleteComponentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | Action ID | 
**component_id** | **str** | Component ID | 
**component_type** | **str** | Component name | 
**component_display_name** | **str** | Component display name | [optional] 
**component_icon** | **str** | Component icon | [optional] 

## Example

```python
from flowhunt.models.flow_assistant_delete_component_metadata import FlowAssistantDeleteComponentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantDeleteComponentMetadata from a JSON string
flow_assistant_delete_component_metadata_instance = FlowAssistantDeleteComponentMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantDeleteComponentMetadata.to_json())

# convert the object into a dict
flow_assistant_delete_component_metadata_dict = flow_assistant_delete_component_metadata_instance.to_dict()
# create an instance of FlowAssistantDeleteComponentMetadata from a dict
flow_assistant_delete_component_metadata_from_dict = FlowAssistantDeleteComponentMetadata.from_dict(flow_assistant_delete_component_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


