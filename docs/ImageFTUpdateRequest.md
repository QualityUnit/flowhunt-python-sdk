# ImageFTUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Fine tuning name | 
**steps** | **int** |  | [optional] 
**lora_rank** | **int** |  | [optional] 
**training_images** | **List[str]** | Training images | 
**cover_image** | **str** | Cover image | 

## Example

```python
from flowhunt.models.image_ft_update_request import ImageFTUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFTUpdateRequest from a JSON string
image_ft_update_request_instance = ImageFTUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ImageFTUpdateRequest.to_json())

# convert the object into a dict
image_ft_update_request_dict = image_ft_update_request_instance.to_dict()
# create an instance of ImageFTUpdateRequest from a dict
image_ft_update_request_from_dict = ImageFTUpdateRequest.from_dict(image_ft_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


