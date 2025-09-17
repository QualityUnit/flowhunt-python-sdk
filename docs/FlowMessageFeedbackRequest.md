# FlowMessageFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**feedback** | [**MessageFeedback**](MessageFeedback.md) |  | [optional] 

## Example

```python
from flowhunt.models.flow_message_feedback_request import FlowMessageFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowMessageFeedbackRequest from a JSON string
flow_message_feedback_request_instance = FlowMessageFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(FlowMessageFeedbackRequest.to_json())

# convert the object into a dict
flow_message_feedback_request_dict = flow_message_feedback_request_instance.to_dict()
# create an instance of FlowMessageFeedbackRequest from a dict
flow_message_feedback_request_from_dict = FlowMessageFeedbackRequest.from_dict(flow_message_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


