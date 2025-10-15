# ToolCallFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in YYYY-MM-DD format | 
**tool_calling_count** | **int** | Tool call count | [optional] [default to 0]
**tools** | [**List[ToolFeedback]**](ToolFeedback.md) |  | [optional] 

## Example

```python
from flowhunt.models.tool_call_feedback_response import ToolCallFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallFeedbackResponse from a JSON string
tool_call_feedback_response_instance = ToolCallFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(ToolCallFeedbackResponse.to_json())

# convert the object into a dict
tool_call_feedback_response_dict = tool_call_feedback_response_instance.to_dict()
# create an instance of ToolCallFeedbackResponse from a dict
tool_call_feedback_response_from_dict = ToolCallFeedbackResponse.from_dict(tool_call_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


