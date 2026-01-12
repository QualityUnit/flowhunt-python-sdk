# ScheduleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | [**ScheduleFrequency**](ScheduleFrequency.md) | Frequency of the schedule (D - Daily, W - Weekly, M - Monthly, Y - Yearly) | [optional] 
**status** | [**ScheduleStatus**](ScheduleStatus.md) | Status of the schedule (N - New, F - Finished, P - Pending, E - Error, C - Cancelled | [optional] 
**with_screenshot** | [**BoolChar**](BoolChar.md) | Flag to take screenshot of all scheduled urls. Some domains doesn&#39;t support screenshots! | [optional] 
**with_browser** | [**BoolChar**](BoolChar.md) | Flag to use instance of real browser for crawling | [optional] 
**follow_links** | [**BoolChar**](BoolChar.md) | Flag to follow links on the page and schedule analyses of found links | [optional] 
**with_proxy_rotation** | **str** | Proxy rotation setting: NULL (no proxy), &#39;Y&#39; for random, or country code (e.g., &#39;us&#39;, &#39;gb&#39;) | [optional] 
**disallow_urls** | **str** | Disallow URLs containing string from the new line separated list | [optional] 
**filter_urls** | **str** | Allow just URLs containing one of the strings from the new line separated list | [optional] 
**custom_headers** | **str** | Custom headers for the request (new line separated values) | [optional] 
**urls_extra_config** | **str** | Extra configuration for URLs (JSON format). For URL_LIST_CRAWL type, contains list of URLs to crawl | [optional] 

## Example

```python
from flowhunt.models.schedule_update_request import ScheduleUpdateRequest

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


