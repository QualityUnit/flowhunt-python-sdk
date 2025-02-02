# GoogleDriveFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID | 
**name** | **str** | Name | 
**kind** | **str** | Kind of document retrieved | 
**viewed_by_me** | **bool** | Viewed by me | 
**created_time** | **str** | Created time | 
**mime_type** | **str** | Mime type | 
**has_thumbnail** | **bool** | Has thumbnail | 
**thumbnail_link** | **str** |  | [optional] 
**size** | **str** | Size | 
**icon_link** | **str** |  | [optional] 
**web_view_link** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.google_drive_file_response import GoogleDriveFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveFileResponse from a JSON string
google_drive_file_response_instance = GoogleDriveFileResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveFileResponse.to_json())

# convert the object into a dict
google_drive_file_response_dict = google_drive_file_response_instance.to_dict()
# create an instance of GoogleDriveFileResponse from a dict
google_drive_file_response_from_dict = GoogleDriveFileResponse.from_dict(google_drive_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


