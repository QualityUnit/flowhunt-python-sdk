# ScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**schedule_id** | **str** | Schedule ID | 
**url** | **str** | URL to be scheduled | 
**frequency** | [**ScheduleFrequency**](ScheduleFrequency.md) | Frequency of the schedule D - Daily, W - Weekly, M - Monthly, Y - Yearly | 
**schedule_type** | [**ScheduleType**](ScheduleType.md) | Type of the schedule (U - URL, D - Domain, S - Sitemap) | 
**start_time** | **datetime** | Start time of the schedule | [optional] 
**end_time** | **datetime** | End time of the schedule | [optional] 
**status** | [**ScheduleStatus**](ScheduleStatus.md) | Status of the schedule (N - New, F - Finished, P - Pending, E - Error, C - Cancelled | 
**status_message** | **str** | Status message | [optional] 
**cnt_scheduled** | **int** | Number of URLs scheduled | 
**cnt_completed** | **int** | Number of URLs completed | 
**cnt_failed** | **int** | Number of URLs failed | 
**with_screenshot** | [**BoolChar**](BoolChar.md) | Whether to take a screenshot | 
**with_browser** | [**BoolChar**](BoolChar.md) | Whether to use a real browser | 
**follow_links** | [**BoolChar**](BoolChar.md) | Whether to follow links | 
**with_proxy_rotation** | **str** | Proxy rotation setting: NULL (no proxy), &#39;random&#39;, or country code (e.g., &#39;us&#39;, &#39;gb&#39;) | [optional] 
**disallow_urls** | **str** | Disallow URLs containing string from the new line separated list | [optional] 
**filter_urls** | **str** | Allow just URLs containing one of the strings from the new line separated list | [optional] 
**custom_headers** | **str** | Custom headers for the request (new line separated values) | [optional] 
**urls_extra_config** | **str** | Extra configuration for URLs (JSON format). For URL_LIST_CRAWL type, contains list of URLs to crawl | [optional] 

## Example

```python
from flowhunt.models.schedule_response import ScheduleResponse

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


