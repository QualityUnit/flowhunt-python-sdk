# GitHubRepoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Repo Name | [optional] 
**private** | **bool** | Is Private Repo | [optional] 
**html_url** | **str** | Repo URL | [optional] 

## Example

```python
from flowhunt.models.git_hub_repo_response import GitHubRepoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubRepoResponse from a JSON string
git_hub_repo_response_instance = GitHubRepoResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubRepoResponse.to_json())

# convert the object into a dict
git_hub_repo_response_dict = git_hub_repo_response_instance.to_dict()
# create an instance of GitHubRepoResponse from a dict
git_hub_repo_response_from_dict = GitHubRepoResponse.from_dict(git_hub_repo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


