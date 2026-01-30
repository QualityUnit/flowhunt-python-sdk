# WixMembersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[WixMemberResponse]**](WixMemberResponse.md) |  | 

## Example

```python
from flowhunt.models.wix_members_response import WixMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WixMembersResponse from a JSON string
wix_members_response_instance = WixMembersResponse.from_json(json)
# print the JSON string representation of the object
print(WixMembersResponse.to_json())

# convert the object into a dict
wix_members_response_dict = wix_members_response_instance.to_dict()
# create an instance of WixMembersResponse from a dict
wix_members_response_from_dict = WixMembersResponse.from_dict(wix_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


