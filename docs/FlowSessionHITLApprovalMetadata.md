# FlowSessionHITLApprovalMetadata

Metadata for HITL approval requested events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_id** | **str** | Hook ID for resuming the hook | 
**hitl_id** | **str** | HITL request ID for correlation | [optional] [default to '']
**tool_name** | **str** | Name of the tool requiring approval | 
**tool_args** | **Dict[str, object]** | Arguments the tool would be called with | 
**tool_description** | **str** | Description of the tool | [optional] [default to '']
**channel** | **str** | Notification channel type | [optional] [default to 'flowhunt']
**channel_config** | **Dict[str, object]** | Channel-specific configuration | [optional] 

## Example

```python
from flowhunt.models.flow_session_hitl_approval_metadata import FlowSessionHITLApprovalMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionHITLApprovalMetadata from a JSON string
flow_session_hitl_approval_metadata_instance = FlowSessionHITLApprovalMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionHITLApprovalMetadata.to_json())

# convert the object into a dict
flow_session_hitl_approval_metadata_dict = flow_session_hitl_approval_metadata_instance.to_dict()
# create an instance of FlowSessionHITLApprovalMetadata from a dict
flow_session_hitl_approval_metadata_from_dict = FlowSessionHITLApprovalMetadata.from_dict(flow_session_hitl_approval_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


