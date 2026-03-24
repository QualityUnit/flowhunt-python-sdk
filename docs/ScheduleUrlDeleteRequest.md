# ScheduleUrlDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_blocking_enabled** | **bool** | Whether to scipe url deletion from disallow urls in schedule | [optional] [default to False]

## Example

```python
from flowhunt.models.schedule_url_delete_request import ScheduleUrlDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUrlDeleteRequest from a JSON string
schedule_url_delete_request_instance = ScheduleUrlDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleUrlDeleteRequest.to_json())

# convert the object into a dict
schedule_url_delete_request_dict = schedule_url_delete_request_instance.to_dict()
# create an instance of ScheduleUrlDeleteRequest from a dict
schedule_url_delete_request_from_dict = ScheduleUrlDeleteRequest.from_dict(schedule_url_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


