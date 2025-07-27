# InstagramProfileInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Instagram profile name | 
**profile_pic_url** | **str** |  | [optional] 
**biography** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.instagram_profile_information_response import InstagramProfileInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramProfileInformationResponse from a JSON string
instagram_profile_information_response_instance = InstagramProfileInformationResponse.from_json(json)
# print the JSON string representation of the object
print(InstagramProfileInformationResponse.to_json())

# convert the object into a dict
instagram_profile_information_response_dict = instagram_profile_information_response_instance.to_dict()
# create an instance of InstagramProfileInformationResponse from a dict
instagram_profile_information_response_from_dict = InstagramProfileInformationResponse.from_dict(instagram_profile_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


