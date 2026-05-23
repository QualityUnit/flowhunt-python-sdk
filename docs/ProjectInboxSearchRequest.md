# ProjectInboxSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Filter by entry kind (info / agent_update / task_completed / task_failed / approval_request). | [optional] 
**status** | **str** | Filter by status (unread / read / archived). | [optional] 
**unread_only** | **bool** | Convenience flag — overrides status when true to return only unread entries. | [optional] [default to False]
**limit** | **int** |  | [optional] [default to 50]
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from flowhunt.models.project_inbox_search_request import ProjectInboxSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInboxSearchRequest from a JSON string
project_inbox_search_request_instance = ProjectInboxSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectInboxSearchRequest.to_json())

# convert the object into a dict
project_inbox_search_request_dict = project_inbox_search_request_instance.to_dict()
# create an instance of ProjectInboxSearchRequest from a dict
project_inbox_search_request_from_dict = ProjectInboxSearchRequest.from_dict(project_inbox_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


