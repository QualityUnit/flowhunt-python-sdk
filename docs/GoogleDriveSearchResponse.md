# GoogleDriveSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** |  | [optional] 
**files** | [**List[GoogleDriveFileResponse]**](GoogleDriveFileResponse.md) | Files | 

## Example

```python
from flowhunt.models.google_drive_search_response import GoogleDriveSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveSearchResponse from a JSON string
google_drive_search_response_instance = GoogleDriveSearchResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveSearchResponse.to_json())

# convert the object into a dict
google_drive_search_response_dict = google_drive_search_response_instance.to_dict()
# create an instance of GoogleDriveSearchResponse from a dict
google_drive_search_response_from_dict = GoogleDriveSearchResponse.from_dict(google_drive_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


