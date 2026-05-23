# ProjectIssueSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectIssueResponse]**](ProjectIssueResponse.md) | List of issues | 
**total** | **int** | Total count | 
**sorting_key_value** | **str** | created_at of last item (cursor for next page) | [optional] 
**scroll_id** | **str** | issue_id of last item (cursor for next page) | [optional] 

## Example

```python
from flowhunt.models.project_issue_search_response import ProjectIssueSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueSearchResponse from a JSON string
project_issue_search_response_instance = ProjectIssueSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueSearchResponse.to_json())

# convert the object into a dict
project_issue_search_response_dict = project_issue_search_response_instance.to_dict()
# create an instance of ProjectIssueSearchResponse from a dict
project_issue_search_response_from_dict = ProjectIssueSearchResponse.from_dict(project_issue_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


