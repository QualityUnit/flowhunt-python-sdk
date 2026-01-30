# CommunityImageGenerationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_image** | **str** |  | 
**prompt** | **str** |  | 

## Example

```python
from flowhunt.models.community_image_generations_response import CommunityImageGenerationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityImageGenerationsResponse from a JSON string
community_image_generations_response_instance = CommunityImageGenerationsResponse.from_json(json)
# print the JSON string representation of the object
print(CommunityImageGenerationsResponse.to_json())

# convert the object into a dict
community_image_generations_response_dict = community_image_generations_response_instance.to_dict()
# create an instance of CommunityImageGenerationsResponse from a dict
community_image_generations_response_from_dict = CommunityImageGenerationsResponse.from_dict(community_image_generations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


