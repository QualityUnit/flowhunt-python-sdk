# ChartSessionDurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_day** | [**List[PerDaySessionDurationResponse]**](PerDaySessionDurationResponse.md) |  | [optional] 

## Example

```python
from flowhunt.models.chart_session_duration_response import ChartSessionDurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSessionDurationResponse from a JSON string
chart_session_duration_response_instance = ChartSessionDurationResponse.from_json(json)
# print the JSON string representation of the object
print(ChartSessionDurationResponse.to_json())

# convert the object into a dict
chart_session_duration_response_dict = chart_session_duration_response_instance.to_dict()
# create an instance of ChartSessionDurationResponse from a dict
chart_session_duration_response_from_dict = ChartSessionDurationResponse.from_dict(chart_session_duration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


