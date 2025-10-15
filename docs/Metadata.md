# Metadata

Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**message** | **str** | Message | 
**sender** | [**HumanAgentSender**](HumanAgentSender.md) |  | [optional] 
**tool_name** | **str** | Tool name | 
**loading_desc** | **str** | Loading description | 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**detailed_description** | **str** |  | [optional] 
**feedback_message_id** | **str** | Message ID | 
**feedback** | [**MessageFeedback**](MessageFeedback.md) |  | [optional] 
**agent_query** | **str** | Search query | 
**tool_response** | **str** | Tool response | 
**task_name** | **str** |  | 
**task_input** | **str** |  | 
**agent** | **str** |  | 
**task_response** | **str** |  | 
**action_id** | **str** | Action ID | 
**component_id** | **str** | Component ID | 
**component_type** | **str** | Component name | 
**component_display_name** | **str** |  | [optional] 
**component_icon** | **str** |  | [optional] 
**parameter_values** | **Dict[str, object]** |  | [optional] 
**source_component_id** | **str** | Source component ID | 
**target_component_id** | **str** | Target component ID | 
**source_field_name** | **str** |  | [optional] 
**target_field_name** | **str** |  | [optional] 
**flow_name** | **str** | Flow name | 
**flow_description** | **str** |  | [optional] 
**flow_id** | **str** | Flow ID | 

## Example

```python
from flowhunt.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


