# ScheduleUrlSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | Schedule ID | [optional] 
**domain_id** | **str** | Domain ID | [optional] 
**url_id** | **str** | URL ID | [optional] 
**url** | **str** | URL | [optional] 
**text_timestamp_from** | **datetime** | Get urls indexed from this time | [optional] 
**text_timestamp_to** | **datetime** | Get urls indexed before this time | [optional] 
**url_title** | **str** | URL Title | [optional] 
**is_original_url** | **bool** | Is Original URL - False means it is redirected url or not canonical url | [optional] 
**created_at_from** | **datetime** | Get urls created after this time | [optional] 
**created_at_to** | **datetime** | Get urls created before this time | [optional] 
**limit** | **int** | Limit of the search | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

## Example

```python
from flowhunt.models.schedule_url_search_request import ScheduleUrlSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUrlSearchRequest from a JSON string
schedule_url_search_request_instance = ScheduleUrlSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleUrlSearchRequest.to_json())

# convert the object into a dict
schedule_url_search_request_dict = schedule_url_search_request_instance.to_dict()
# create an instance of ScheduleUrlSearchRequest from a dict
schedule_url_search_request_from_dict = ScheduleUrlSearchRequest.from_dict(schedule_url_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


