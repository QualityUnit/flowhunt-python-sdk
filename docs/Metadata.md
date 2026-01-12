# Metadata

Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**message** | **str** | Message | 
**sender** | [**HumanAgentSender**](HumanAgentSender.md) | Sender ID | [optional] 
**tool_name** | **str** | Tool name | 
**loading_desc** | **str** | Loading description | 
**icon** | **str** | Icon | [optional] 
**color** | **str** | Color | [optional] 
**detailed_description** | **str** | Detailed Description | [optional] 
**feedback_message_id** | **str** | Message ID | 
**feedback** | [**MessageFeedback**](MessageFeedback.md) | Message Feedback | [optional] 
**agent_query** | **str** | Search query | 
**tool_response** | **str** | Tool response | 
**task_name** | **str** | Task name | 
**task_input** | **str** | Task input | 
**agent** | **str** | Agent that executed the task | 
**task_response** | **str** | Task response | 
**artefacts** | [**List[FlowSessionArtefactInfo]**](FlowSessionArtefactInfo.md) | List of artefact files created by agent | 
**cot_id** | **str** | Unique CoT identifier for updates | 
**content** | **str** | Chain of thought / reasoning text | 
**todo_id** | **str** | Unique todo list identifier for updates | 
**todos** | [**List[TodoItem]**](TodoItem.md) | List of todo items | 
**action_id** | **str** | Action ID | 
**component_id** | **str** | Component ID | 
**component_type** | **str** | Component name | 
**component_display_name** | **str** | Component display name | [optional] 
**component_icon** | **str** | Component icon | [optional] 
**parameter_values** | **Dict[str, object]** | Parameter values | [optional] 
**source_component_id** | **str** | Source component ID | 
**target_component_id** | **str** | Target component ID | 
**source_field_name** | **str** | Source field name | [optional] 
**target_field_name** | **str** | Target field name | [optional] 
**flow_name** | **str** | Agent name | 
**flow_description** | **str** | Agent description | [optional] 
**flow_id** | **str** | Agent ID | 

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


