# PerDaySessionDurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in YYYY-MM-DD format | 
**average_duration** | **float** | Average session duration in seconds | [optional] [default to 0.0]
**session_count** | **int** | Count of unique sessions (visitor count) | [optional] [default to 0]

## Example

```python
from flowhunt.models.per_day_session_duration_response import PerDaySessionDurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PerDaySessionDurationResponse from a JSON string
per_day_session_duration_response_instance = PerDaySessionDurationResponse.from_json(json)
# print the JSON string representation of the object
print(PerDaySessionDurationResponse.to_json())

# convert the object into a dict
per_day_session_duration_response_dict = per_day_session_duration_response_instance.to_dict()
# create an instance of PerDaySessionDurationResponse from a dict
per_day_session_duration_response_from_dict = PerDaySessionDurationResponse.from_dict(per_day_session_duration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


