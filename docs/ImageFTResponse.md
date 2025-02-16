# ImageFTResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ft_type** | [**FTType**](FTType.md) | Fine tuning type | 
**ft_id** | **str** | Fine tuning id | 
**name** | **str** | Fine tuning name | 
**steps** | **int** | Number of steps | 
**lora_rank** | **int** | Lora rank | 
**trigger_word** | **str** | Trigger word | 
**training_images** | **List[str]** | Training images | 
**status** | [**FTStatus**](FTStatus.md) | Status | 
**cover_image** | **str** | Cover image | 

## Example

```python
from flowhunt.models.image_ft_response import ImageFTResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFTResponse from a JSON string
image_ft_response_instance = ImageFTResponse.from_json(json)
# print the JSON string representation of the object
print(ImageFTResponse.to_json())

# convert the object into a dict
image_ft_response_dict = image_ft_response_instance.to_dict()
# create an instance of ImageFTResponse from a dict
image_ft_response_from_dict = ImageFTResponse.from_dict(image_ft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


