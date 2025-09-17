# ScheduleCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | [**AppUrlInput**](AppUrlInput.md) |  | 
**frequency** | [**ScheduleFrequency**](ScheduleFrequency.md) |  | 
**schedule_type** | [**ScheduleType**](ScheduleType.md) |  | 
**with_screenshot** | [**BoolChar**](BoolChar.md) |  | [optional] 
**with_browser** | [**BoolChar**](BoolChar.md) |  | [optional] 
**follow_links** | [**BoolChar**](BoolChar.md) |  | [optional] 
**with_proxy_rotation** | **str** |  | [optional] 
**disallow_urls** | **str** |  | [optional] 
**filter_urls** | **str** |  | [optional] 
**custom_headers** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.schedule_create_request import ScheduleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCreateRequest from a JSON string
schedule_create_request_instance = ScheduleCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleCreateRequest.to_json())

# convert the object into a dict
schedule_create_request_dict = schedule_create_request_instance.to_dict()
# create an instance of ScheduleCreateRequest from a dict
schedule_create_request_from_dict = ScheduleCreateRequest.from_dict(schedule_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


