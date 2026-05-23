# ProjectInboxSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectInboxEntryResponse]**](ProjectInboxEntryResponse.md) |  | 
**total** | **int** |  | 
**sorting_key_value** | **str** |  | [optional] 
**scroll_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.project_inbox_search_response import ProjectInboxSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInboxSearchResponse from a JSON string
project_inbox_search_response_instance = ProjectInboxSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectInboxSearchResponse.to_json())

# convert the object into a dict
project_inbox_search_response_dict = project_inbox_search_response_instance.to_dict()
# create an instance of ProjectInboxSearchResponse from a dict
project_inbox_search_response_from_dict = ProjectInboxSearchResponse.from_dict(project_inbox_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


