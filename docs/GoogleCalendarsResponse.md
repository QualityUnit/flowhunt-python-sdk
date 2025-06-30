# GoogleCalendarsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | [**List[GoogleCalendarResponse]**](GoogleCalendarResponse.md) |  | 

## Example

```python
from flowhunt.models.google_calendars_response import GoogleCalendarsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCalendarsResponse from a JSON string
google_calendars_response_instance = GoogleCalendarsResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleCalendarsResponse.to_json())

# convert the object into a dict
google_calendars_response_dict = google_calendars_response_instance.to_dict()
# create an instance of GoogleCalendarsResponse from a dict
google_calendars_response_from_dict = GoogleCalendarsResponse.from_dict(google_calendars_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


