# GitHubReposResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repos** | [**List[GitHubRepoResponse]**](GitHubRepoResponse.md) |  | 

## Example

```python
from flowhunt.models.git_hub_repos_response import GitHubReposResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubReposResponse from a JSON string
git_hub_repos_response_instance = GitHubReposResponse.from_json(json)
# print the JSON string representation of the object
print(GitHubReposResponse.to_json())

# convert the object into a dict
git_hub_repos_response_dict = git_hub_repos_response_instance.to_dict()
# create an instance of GitHubReposResponse from a dict
git_hub_repos_response_from_dict = GitHubReposResponse.from_dict(git_hub_repos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


