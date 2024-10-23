# FlowSessionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content | 
**role** | [**FlowRequestChatRole**](FlowRequestChatRole.md) | The role | 

## Example

```python
from flowhunt.models.flow_session_message import FlowSessionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionMessage from a JSON string
flow_session_message_instance = FlowSessionMessage.from_json(json)
# print the JSON string representation of the object
print(FlowSessionMessage.to_json())

# convert the object into a dict
flow_session_message_dict = flow_session_message_instance.to_dict()
# create an instance of FlowSessionMessage from a dict
flow_session_message_from_dict = FlowSessionMessage.from_dict(flow_session_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


