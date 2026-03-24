# GitLabProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[GitLabProjectResponse]**](GitLabProjectResponse.md) |  | 

## Example

```python
from flowhunt.models.git_lab_projects_response import GitLabProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitLabProjectsResponse from a JSON string
git_lab_projects_response_instance = GitLabProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(GitLabProjectsResponse.to_json())

# convert the object into a dict
git_lab_projects_response_dict = git_lab_projects_response_instance.to_dict()
# create an instance of GitLabProjectsResponse from a dict
git_lab_projects_response_from_dict = GitLabProjectsResponse.from_dict(git_lab_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


