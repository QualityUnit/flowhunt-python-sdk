# GoogleDriveFoldersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[GoogleDriveFolderResponse]**](GoogleDriveFolderResponse.md) |  | 

## Example

```python
from flowhunt.models.google_drive_folders_response import GoogleDriveFoldersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveFoldersResponse from a JSON string
google_drive_folders_response_instance = GoogleDriveFoldersResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveFoldersResponse.to_json())

# convert the object into a dict
google_drive_folders_response_dict = google_drive_folders_response_instance.to_dict()
# create an instance of GoogleDriveFoldersResponse from a dict
google_drive_folders_response_from_dict = GoogleDriveFoldersResponse.from_dict(google_drive_folders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


