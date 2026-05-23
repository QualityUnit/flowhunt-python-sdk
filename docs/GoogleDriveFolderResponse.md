# GoogleDriveFolderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | Folder ID | 
**name** | **str** | Folder name | 
**parents** | **List[str]** | Parent folder IDs | [optional] 

## Example

```python
from flowhunt.models.google_drive_folder_response import GoogleDriveFolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveFolderResponse from a JSON string
google_drive_folder_response_instance = GoogleDriveFolderResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveFolderResponse.to_json())

# convert the object into a dict
google_drive_folder_response_dict = google_drive_folder_response_instance.to_dict()
# create an instance of GoogleDriveFolderResponse from a dict
google_drive_folder_response_from_dict = GoogleDriveFolderResponse.from_dict(google_drive_folder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


