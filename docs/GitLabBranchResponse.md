# GitLabBranchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Branch name | [optional] 
**web_url** | **str** | Branch web URL | [optional] 

## Example

```python
from flowhunt.models.git_lab_branch_response import GitLabBranchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitLabBranchResponse from a JSON string
git_lab_branch_response_instance = GitLabBranchResponse.from_json(json)
# print the JSON string representation of the object
print(GitLabBranchResponse.to_json())

# convert the object into a dict
git_lab_branch_response_dict = git_lab_branch_response_instance.to_dict()
# create an instance of GitLabBranchResponse from a dict
git_lab_branch_response_from_dict = GitLabBranchResponse.from_dict(git_lab_branch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


