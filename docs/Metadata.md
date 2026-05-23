# Metadata

Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**message** | **str** | User-facing message explaining why access is needed | [default to '']
**sender** | [**HumanAgentSender**](HumanAgentSender.md) | Sender ID | [optional] 
**tool_name** | **str** | Name of the tool requiring approval | 
**loading_desc** | **str** | Loading description | 
**icon** | **str** | Icon | [optional] 
**color** | **str** | Color | [optional] 
**detailed_description** | **str** | Detailed Description | [optional] 
**feedback_message_id** | **str** | Message ID | 
**feedback** | [**MessageFeedback**](MessageFeedback.md) | Message Feedback | [optional] 
**agent_query** | **str** | Tool input arguments | 
**tool_response** | **str** | Tool response | 
**task_name** | **str** | Task name | 
**task_input** | **str** | Task input | 
**agent** | **str** | Agent that executed the task | 
**task_response** | **str** | Task response | 
**artefacts** | [**List[FlowSessionArtefactInfo]**](FlowSessionArtefactInfo.md) | List of artefact files created by agent | 
**cot_id** | **str** | Unique CoT identifier for updates | 
**content** | **str** | Chain of thought / reasoning text | 
**agent_name** | **str** | Name of the agent | 
**agent_type** | **str** | Agent type: supervisor, lead, or worker | 
**model** | **str** | LLM model name used by the agent | 
**task** | **str** | The full prompt sent to the subagent. | 
**started_by** | **str** | Name of the agent that initiated this delegation. | 
**target_agent** | **str** | Name of the subagent receiving the task. | 
**todo_id** | **str** | Unique todo list identifier for updates | 
**todos** | [**List[TodoItem]**](TodoItem.md) | List of todo items | 
**action_description** | **str** | Description of what the tool does | [optional] 
**duration_ms** | **int** | Duration in milliseconds | [optional] 
**stage** | **str** | Initialization stage (e.g., &#39;starting&#39;, &#39;creating_agent&#39;, &#39;ready&#39;) | 
**hook_id** | **str** | Hook ID for resuming the hook | 
**hook_name** | **str** | Internal pyworkflow hook name | 
**prompt_message** | **str** | Message to show the user | 
**script** | **str** | JS expression to evaluate in the visitor&#39;s browser | 
**timeout_ms** | **int** | Maximum time the widget should wait before returning a timeout error | [optional] [default to 5000]
**request_id** | **str** | Correlates the request with the response posted back from the widget | 
**hitl_id** | **str** | HITL request ID for correlation | [optional] [default to '']
**tool_args** | **Dict[str, object]** | Arguments the tool would be called with | 
**tool_description** | **str** | Description of the tool | [optional] [default to '']
**channel** | **str** | Notification channel type | [optional] [default to 'flowhunt']
**channel_config** | **Dict[str, object]** | Channel-specific configuration | [optional] 
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
**file_id** | **str** | File ID | 
**file_name** | **str** | File name | 
**file_type** | **str** | File type | [optional] 
**document_type** | **str** | Type of document (e.g., google_sheets) | 
**slug** | **str** | Integration slug that is missing | 
**integration_url** | **str** | URL for the user to set up the integration | 
**document_id** | **str** | ID of the document requiring access | 

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


