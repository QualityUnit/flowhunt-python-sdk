# PerDayFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in YYYY-MM-DD format | 
**positive** | **int** | Count of positive feedback | [optional] [default to 0]
**negative** | **int** | Count of negative feedback | [optional] [default to 0]
**session_count** | **int** | Count of unique sessions (visitor count) | [optional] [default to 0]
**human_message_count** | **int** | Count of human messages | [optional] [default to 0]
**tool_calling_count** | **int** | Count of tool calls | [optional] 

## Example

```python
from flowhunt.models.per_day_feedback import PerDayFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of PerDayFeedback from a JSON string
per_day_feedback_instance = PerDayFeedback.from_json(json)
# print the JSON string representation of the object
print(PerDayFeedback.to_json())

# convert the object into a dict
per_day_feedback_dict = per_day_feedback_instance.to_dict()
# create an instance of PerDayFeedback from a dict
per_day_feedback_from_dict = PerDayFeedback.from_dict(per_day_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


