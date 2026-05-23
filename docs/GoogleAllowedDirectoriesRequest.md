# GoogleAllowedDirectoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_directory_ids** | **List[str]** | Drive folder IDs the integration restricts Google Drive tools to. An empty list clears the restriction. | [optional] 

## Example

```python
from flowhunt.models.google_allowed_directories_request import GoogleAllowedDirectoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAllowedDirectoriesRequest from a JSON string
google_allowed_directories_request_instance = GoogleAllowedDirectoriesRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAllowedDirectoriesRequest.to_json())

# convert the object into a dict
google_allowed_directories_request_dict = google_allowed_directories_request_instance.to_dict()
# create an instance of GoogleAllowedDirectoriesRequest from a dict
google_allowed_directories_request_from_dict = GoogleAllowedDirectoriesRequest.from_dict(google_allowed_directories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


