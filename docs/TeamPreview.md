# TeamPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_count** | **int** |  | 
**supervisor_label** | **str** |  | [optional] [default to 'Supervisor']
**avatars** | [**List[AvatarChip]**](AvatarChip.md) |  | 

## Example

```python
from flowhunt.models.team_preview import TeamPreview

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPreview from a JSON string
team_preview_instance = TeamPreview.from_json(json)
# print the JSON string representation of the object
print(TeamPreview.to_json())

# convert the object into a dict
team_preview_dict = team_preview_instance.to_dict()
# create an instance of TeamPreview from a dict
team_preview_from_dict = TeamPreview.from_dict(team_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


