# ScheduleUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | 
**domain_id** | **str** |  | 
**url_id** | **str** |  | 
**url** | **str** |  | 
**last_text_timestamp** | **datetime** |  | 
**page_screenshot** | [**UrlScreenshotResponse**](UrlScreenshotResponse.md) |  | 
**url_title** | **str** |  | 
**url_meta_description** | **str** |  | 
**url_og_image** | **str** |  | 
**is_original_url** | **bool** |  | 
**dest_url_id** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from flowhunt.models.schedule_url_response import ScheduleUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUrlResponse from a JSON string
schedule_url_response_instance = ScheduleUrlResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleUrlResponse.to_json())

# convert the object into a dict
schedule_url_response_dict = schedule_url_response_instance.to_dict()
# create an instance of ScheduleUrlResponse from a dict
schedule_url_response_from_dict = ScheduleUrlResponse.from_dict(schedule_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


