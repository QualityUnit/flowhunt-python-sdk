# FlowSessionMessageFeedbackMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_message_id** | **str** | Message ID | 
**feedback** | [**MessageFeedback**](MessageFeedback.md) | Message Feedback | [optional] 

## Example

```python
from flowhunt.models.flow_session_message_feedback_metadata import FlowSessionMessageFeedbackMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionMessageFeedbackMetadata from a JSON string
flow_session_message_feedback_metadata_instance = FlowSessionMessageFeedbackMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionMessageFeedbackMetadata.to_json())

# convert the object into a dict
flow_session_message_feedback_metadata_dict = flow_session_message_feedback_metadata_instance.to_dict()
# create an instance of FlowSessionMessageFeedbackMetadata from a dict
flow_session_message_feedback_metadata_from_dict = FlowSessionMessageFeedbackMetadata.from_dict(flow_session_message_feedback_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


