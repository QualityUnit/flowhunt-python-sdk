# LogsSearchRequest

Request model for searching logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_types** | **List[str]** | Filter by log types | [optional] 
**log_levels** | **List[str]** | Filter by log levels | [optional] 
**category_id** | **str** | Filter by category ID (e.g. Schedule ID or other group entinty ID) | [optional] 
**from_date** | **str** | Start date for the search range (ISO format) | [optional] 
**to_date** | **str** | End date for the search range (ISO format) | [optional] 
**search_text** | **str** | Text to search for in log messages | [optional] 
**page** | **int** | Page number for pagination | [optional] [default to 1]
**page_size** | **int** | Number of results per page | [optional] [default to 50]
**sort_by** | **str** | Field to sort results by | [optional] [default to 'created_at']
**sort_direction** | [**SortDirection**](SortDirection.md) | Sort direction (asc or desc) | [optional] 

## Example

```python
from flowhunt.models.logs_search_request import LogsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogsSearchRequest from a JSON string
logs_search_request_instance = LogsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(LogsSearchRequest.to_json())

# convert the object into a dict
logs_search_request_dict = logs_search_request_instance.to_dict()
# create an instance of LogsSearchRequest from a dict
logs_search_request_from_dict = LogsSearchRequest.from_dict(logs_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


