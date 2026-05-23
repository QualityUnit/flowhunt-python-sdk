# GoogleAllowedDirectoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_directory_ids** | **List[str]** | Directory IDs the integration restricts Google Drive tools to. | [optional] 

## Example

```python
from flowhunt.models.google_allowed_directories_response import GoogleAllowedDirectoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAllowedDirectoriesResponse from a JSON string
google_allowed_directories_response_instance = GoogleAllowedDirectoriesResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleAllowedDirectoriesResponse.to_json())

# convert the object into a dict
google_allowed_directories_response_dict = google_allowed_directories_response_instance.to_dict()
# create an instance of GoogleAllowedDirectoriesResponse from a dict
google_allowed_directories_response_from_dict = GoogleAllowedDirectoriesResponse.from_dict(google_allowed_directories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


