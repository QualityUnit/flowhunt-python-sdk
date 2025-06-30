# ScheduleSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | [**ScheduleStatus**](ScheduleStatus.md) |  | [optional] 
**schedule_type** | [**ScheduleType**](ScheduleType.md) |  | [optional] 
**limit** | **int** | Limit of the search | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from flowhunt.models.schedule_search_request import ScheduleSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleSearchRequest from a JSON string
schedule_search_request_instance = ScheduleSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleSearchRequest.to_json())

# convert the object into a dict
schedule_search_request_dict = schedule_search_request_instance.to_dict()
# create an instance of ScheduleSearchRequest from a dict
schedule_search_request_from_dict = ScheduleSearchRequest.from_dict(schedule_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


