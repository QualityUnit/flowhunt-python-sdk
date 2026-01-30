# FeedbackChartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_day** | [**List[PerDayFeedback]**](PerDayFeedback.md) | Response message | [optional] [default to []]
**totals** | [**TotalFeedback**](TotalFeedback.md) | Total counts | [optional] 

## Example

```python
from flowhunt.models.feedback_chart_response import FeedbackChartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackChartResponse from a JSON string
feedback_chart_response_instance = FeedbackChartResponse.from_json(json)
# print the JSON string representation of the object
print(FeedbackChartResponse.to_json())

# convert the object into a dict
feedback_chart_response_dict = feedback_chart_response_instance.to_dict()
# create an instance of FeedbackChartResponse from a dict
feedback_chart_response_from_dict = FeedbackChartResponse.from_dict(feedback_chart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


