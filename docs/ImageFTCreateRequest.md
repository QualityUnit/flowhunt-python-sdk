# ImageFTCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Fine tuning name | 
**trigger_word** | **str** | Trigger word | 
**steps** | **int** | Number of steps | [optional] [default to 1000]
**lora_rank** | **int** | Lora rank | [optional] [default to 16]
**training_images** | **List[str]** | Training images | 
**cover_image** | **str** | Cover image | 

## Example

```python
from flowhunt.models.image_ft_create_request import ImageFTCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFTCreateRequest from a JSON string
image_ft_create_request_instance = ImageFTCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ImageFTCreateRequest.to_json())

# convert the object into a dict
image_ft_create_request_dict = image_ft_create_request_instance.to_dict()
# create an instance of ImageFTCreateRequest from a dict
image_ft_create_request_from_dict = ImageFTCreateRequest.from_dict(image_ft_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


