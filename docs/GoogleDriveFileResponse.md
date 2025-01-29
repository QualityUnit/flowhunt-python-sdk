# GoogleDriveFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

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


