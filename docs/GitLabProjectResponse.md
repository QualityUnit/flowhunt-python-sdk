# GitLabProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project ID | [optional] 
**name** | **str** | Project name | [optional] 
**path_with_namespace** | **str** | Full path including namespace | [optional] 
**web_url** | **str** | Project web URL | [optional] 
**visibility** | **str** | Project visibility | [optional] 
**default_branch** | **str** | Default branch name | [optional] 

## Example

```python
from flowhunt.models.git_lab_project_response import GitLabProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitLabProjectResponse from a JSON string
git_lab_project_response_instance = GitLabProjectResponse.from_json(json)
# print the JSON string representation of the object
print(GitLabProjectResponse.to_json())

# convert the object into a dict
git_lab_project_response_dict = git_lab_project_response_instance.to_dict()
# create an instance of GitLabProjectResponse from a dict
git_lab_project_response_from_dict = GitLabProjectResponse.from_dict(git_lab_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


