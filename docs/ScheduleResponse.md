# ScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**schedule_id** | **str** | Schedule ID | 
**url** | **str** | URL to be scheduled | 
**frequency** | [**ScheduleFrequency**](ScheduleFrequency.md) | Frequency of the schedule D - Daily, W - Weekly, M - Monthly, Y - Yearly | 
**schedule_type** | [**ScheduleType**](ScheduleType.md) | Type of the schedule (U - URL, D - Domain, S - Sitemap) | 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**status** | [**ScheduleStatus**](ScheduleStatus.md) | Status of the schedule (N - New, F - Finished, P - Pending, E - Error, C - Cancelled | 
**status_message** | **str** |  | [optional] 
**cnt_scheduled** | **int** |  | 
**cnt_completed** | **int** |  | 
**cnt_failed** | **int** |  | 
**with_screenshot** | [**BoolChar**](BoolChar.md) |  | 
**with_proxy_rotation** | [**BoolChar**](BoolChar.md) |  | 
**disallow_urls** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.schedule_response import ScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleResponse from a JSON string
schedule_response_instance = ScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleResponse.to_json())

# convert the object into a dict
schedule_response_dict = schedule_response_instance.to_dict()
# create an instance of ScheduleResponse from a dict
schedule_response_from_dict = ScheduleResponse.from_dict(schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


