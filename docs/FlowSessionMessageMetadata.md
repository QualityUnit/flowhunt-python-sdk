# FlowSessionMessageMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**message** | **str** | Message | 
**sender** | [**HumanAgentSender**](HumanAgentSender.md) |  | [optional] 

## Example

```python
from flowhunt.models.flow_session_message_metadata import FlowSessionMessageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionMessageMetadata from a JSON string
flow_session_message_metadata_instance = FlowSessionMessageMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionMessageMetadata.to_json())

# convert the object into a dict
flow_session_message_metadata_dict = flow_session_message_metadata_instance.to_dict()
# create an instance of FlowSessionMessageMetadata from a dict
flow_session_message_metadata_from_dict = FlowSessionMessageMetadata.from_dict(flow_session_message_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


