# AvatarChip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial** | **str** |  | 
**bg** | **str** |  | 
**fg** | **str** |  | 
**role** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.avatar_chip import AvatarChip

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarChip from a JSON string
avatar_chip_instance = AvatarChip.from_json(json)
# print the JSON string representation of the object
print(AvatarChip.to_json())

# convert the object into a dict
avatar_chip_dict = avatar_chip_instance.to_dict()
# create an instance of AvatarChip from a dict
avatar_chip_from_dict = AvatarChip.from_dict(avatar_chip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


