# ToolFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Tool name | 
**tool_call_count** | **int** | Tool call count | 

## Example

```python
from flowhunt.models.tool_feedback import ToolFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of ToolFeedback from a JSON string
tool_feedback_instance = ToolFeedback.from_json(json)
# print the JSON string representation of the object
print(ToolFeedback.to_json())

# convert the object into a dict
tool_feedback_dict = tool_feedback_instance.to_dict()
# create an instance of ToolFeedback from a dict
tool_feedback_from_dict = ToolFeedback.from_dict(tool_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


