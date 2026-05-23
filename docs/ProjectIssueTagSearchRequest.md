# ProjectIssueTagSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Search by name | [optional] 
**limit** | **int** | Limit results | [optional] [default to 25]
**pagination** | [**Pagination**](Pagination.md) | Pagination | [optional] 

## Example

```python
from flowhunt.models.project_issue_tag_search_request import ProjectIssueTagSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIssueTagSearchRequest from a JSON string
project_issue_tag_search_request_instance = ProjectIssueTagSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectIssueTagSearchRequest.to_json())

# convert the object into a dict
project_issue_tag_search_request_dict = project_issue_tag_search_request_instance.to_dict()
# create an instance of ProjectIssueTagSearchRequest from a dict
project_issue_tag_search_request_from_dict = ProjectIssueTagSearchRequest.from_dict(project_issue_tag_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


