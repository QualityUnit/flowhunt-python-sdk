# ThridPartyLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**email** | **str** |  | 
**avatar_url** | **str** |  | [optional] 
**name** | **str** |  | 
**plan_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.thrid_party_login_request import ThridPartyLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThridPartyLoginRequest from a JSON string
thrid_party_login_request_instance = ThridPartyLoginRequest.from_json(json)
# print the JSON string representation of the object
print(ThridPartyLoginRequest.to_json())

# convert the object into a dict
thrid_party_login_request_dict = thrid_party_login_request_instance.to_dict()
# create an instance of ThridPartyLoginRequest from a dict
thrid_party_login_request_from_dict = ThridPartyLoginRequest.from_dict(thrid_party_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


