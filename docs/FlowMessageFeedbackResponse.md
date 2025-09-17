# FlowMessageFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_message** | **str** | Response message | 

## Example

```python
from flowhunt.models.flow_message_feedback_response import FlowMessageFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowMessageFeedbackResponse from a JSON string
flow_message_feedback_response_instance = FlowMessageFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(FlowMessageFeedbackResponse.to_json())

# convert the object into a dict
flow_message_feedback_response_dict = flow_message_feedback_response_instance.to_dict()
# create an instance of FlowMessageFeedbackResponse from a dict
flow_message_feedback_response_from_dict = FlowMessageFeedbackResponse.from_dict(flow_message_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


