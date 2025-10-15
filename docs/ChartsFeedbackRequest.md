# ChartsFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.charts_feedback_request import ChartsFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChartsFeedbackRequest from a JSON string
charts_feedback_request_instance = ChartsFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(ChartsFeedbackRequest.to_json())

# convert the object into a dict
charts_feedback_request_dict = charts_feedback_request_instance.to_dict()
# create an instance of ChartsFeedbackRequest from a dict
charts_feedback_request_from_dict = ChartsFeedbackRequest.from_dict(charts_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


