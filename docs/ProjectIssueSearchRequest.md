# ProjectIssueSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Full-text search query | [optional] 
**status** | **str** | Filter by status | [optional] 
**issue_type** | **str** | Filter by issue type | [optional] 
**tag_ids** | **List[str]** | Filter by tag IDs | [optional] 
**session_id** | **str** | Filter to issues whose flow session_id matches this value. Used by the run detail page to deep-link back to the issue that spawned the run. | [optional] 
**limit** | **int** | Limit results | [optional] [default to 50]
**pagination** | [**Pagination**](Pagination.md) | Cursor-based pagination. sorting_key_value&#x3D;created_at ISO string, scroll_id&#x3D;issue_id | [optional] 

## Example

```python
from flowhunt.models.project_issue_search_request import ProjectIssueSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueSearchRequest from a JSON string
project_issue_search_request_instance = ProjectIssueSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueSearchRequest.to_json())

# convert the object into a dict
project_issue_search_request_dict = project_issue_search_request_instance.to_dict()
# create an instance of ProjectIssueSearchRequest from a dict
project_issue_search_request_from_dict = ProjectIssueSearchRequest.from_dict(project_issue_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


