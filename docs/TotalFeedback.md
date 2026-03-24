# TotalFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive** | **int** | Total count of positive feedback | [optional] [default to 0]
**negative** | **int** | Total count of negative feedback | [optional] [default to 0]
**session_count** | **int** | Total count of unique sessions (visitor count) | [optional] [default to 0]
**human_message_count** | **float** | Average human messages per session | [optional] [default to 0.0]
**tool_calling_count** | **float** | Average tool calls per session | [optional] [default to 0.0]

## Example

```python
from flowhunt.models.total_feedback import TotalFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of TotalFeedback from a JSON string
total_feedback_instance = TotalFeedback.from_json(json)
# print the JSON string representation of the object
print(TotalFeedback.to_json())

# convert the object into a dict
total_feedback_dict = total_feedback_instance.to_dict()
# create an instance of TotalFeedback from a dict
total_feedback_from_dict = TotalFeedback.from_dict(total_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


