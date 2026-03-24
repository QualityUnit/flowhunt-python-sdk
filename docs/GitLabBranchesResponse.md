# GitLabBranchesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[GitLabBranchResponse]**](GitLabBranchResponse.md) |  | 

## Example

```python
from flowhunt.models.git_lab_branches_response import GitLabBranchesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitLabBranchesResponse from a JSON string
git_lab_branches_response_instance = GitLabBranchesResponse.from_json(json)
# print the JSON string representation of the object
print(GitLabBranchesResponse.to_json())

# convert the object into a dict
git_lab_branches_response_dict = git_lab_branches_response_instance.to_dict()
# create an instance of GitLabBranchesResponse from a dict
git_lab_branches_response_from_dict = GitLabBranchesResponse.from_dict(git_lab_branches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


