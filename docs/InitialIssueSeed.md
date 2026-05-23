# InitialIssueSeed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**type** | **str** |  | [optional] [default to 'normal']
**frequency** | **str** |  | [optional] 
**tag_refs** | **List[str]** |  | [optional] [default to []]

## Example

```python
from flowhunt.models.initial_issue_seed import InitialIssueSeed

# TODO update the JSON string below
json = "{}"
# create an instance of InitialIssueSeed from a JSON string
initial_issue_seed_instance = InitialIssueSeed.from_json(json)
# print the JSON string representation of the object
print(InitialIssueSeed.to_json())

# convert the object into a dict
initial_issue_seed_dict = initial_issue_seed_instance.to_dict()
# create an instance of InitialIssueSeed from a dict
initial_issue_seed_from_dict = InitialIssueSeed.from_dict(initial_issue_seed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


