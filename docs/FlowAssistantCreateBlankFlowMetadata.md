# FlowAssistantCreateBlankFlowMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_name** | **str** | Agent name | 
**flow_description** | **str** | Agent description | [optional] 
**flow_id** | **str** | Agent ID | 

## Example

```python
from flowhunt.models.flow_assistant_create_blank_flow_metadata import FlowAssistantCreateBlankFlowMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowAssistantCreateBlankFlowMetadata from a JSON string
flow_assistant_create_blank_flow_metadata_instance = FlowAssistantCreateBlankFlowMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowAssistantCreateBlankFlowMetadata.to_json())

# convert the object into a dict
flow_assistant_create_blank_flow_metadata_dict = flow_assistant_create_blank_flow_metadata_instance.to_dict()
# create an instance of FlowAssistantCreateBlankFlowMetadata from a dict
flow_assistant_create_blank_flow_metadata_from_dict = FlowAssistantCreateBlankFlowMetadata.from_dict(flow_assistant_create_blank_flow_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


