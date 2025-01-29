# GoogleDriveSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_by** | **str** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.google_drive_search_query import GoogleDriveSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveSearchQuery from a JSON string
google_drive_search_query_instance = GoogleDriveSearchQuery.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveSearchQuery.to_json())

# convert the object into a dict
google_drive_search_query_dict = google_drive_search_query_instance.to_dict()
# create an instance of GoogleDriveSearchQuery from a dict
google_drive_search_query_from_dict = GoogleDriveSearchQuery.from_dict(google_drive_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


