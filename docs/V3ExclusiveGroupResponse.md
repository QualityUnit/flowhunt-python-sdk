# V3ExclusiveGroupResponse

Response schema for an exclusive group definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Exclusive group identifier | 
**display_name** | **str** | Display name for UI | 
**description** | **str** | Group description | [optional] 

## Example

```python
from flowhunt.models.v3_exclusive_group_response import V3ExclusiveGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3ExclusiveGroupResponse from a JSON string
v3_exclusive_group_response_instance = V3ExclusiveGroupResponse.from_json(json)
# print the JSON string representation of the object
print(V3ExclusiveGroupResponse.to_json())

# convert the object into a dict
v3_exclusive_group_response_dict = v3_exclusive_group_response_instance.to_dict()
# create an instance of V3ExclusiveGroupResponse from a dict
v3_exclusive_group_response_from_dict = V3ExclusiveGroupResponse.from_dict(v3_exclusive_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


