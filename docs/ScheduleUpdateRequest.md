# ScheduleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | [**ScheduleFrequency**](ScheduleFrequency.md) |  | [optional] 
**status** | [**ScheduleStatus**](ScheduleStatus.md) |  | [optional] 
**with_screenshot** | [**BoolChar**](BoolChar.md) |  | [optional] 
**with_proxy_rotation** | [**BoolChar**](BoolChar.md) |  | [optional] 
**disallow_urls** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.schedule_update_request import ScheduleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUpdateRequest from a JSON string
schedule_update_request_instance = ScheduleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleUpdateRequest.to_json())

# convert the object into a dict
schedule_update_request_dict = schedule_update_request_instance.to_dict()
# create an instance of ScheduleUpdateRequest from a dict
schedule_update_request_from_dict = ScheduleUpdateRequest.from_dict(schedule_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


