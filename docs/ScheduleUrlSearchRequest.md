# ScheduleUrlSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | [optional] 
**domain_id** | **str** |  | [optional] 
**url_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**text_timestamp_from** | **datetime** |  | [optional] 
**text_timestamp_to** | **datetime** |  | [optional] 
**url_title** | **str** |  | [optional] 
**is_original_url** | **bool** |  | [optional] 
**created_at_from** | **datetime** |  | [optional] 
**created_at_to** | **datetime** |  | [optional] 
**limit** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

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


