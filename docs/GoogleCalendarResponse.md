# GoogleCalendarResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | **str** | Calendar ID | 
**calendar_name** | **str** | Calendar name | 

## Example

```python
from flowhunt.models.google_calendar_response import GoogleCalendarResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCalendarResponse from a JSON string
google_calendar_response_instance = GoogleCalendarResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleCalendarResponse.to_json())

# convert the object into a dict
google_calendar_response_dict = google_calendar_response_instance.to_dict()
# create an instance of GoogleCalendarResponse from a dict
google_calendar_response_from_dict = GoogleCalendarResponse.from_dict(google_calendar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


