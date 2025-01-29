# ImageFTCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Fine tuning name | 
**model_name** | [**ImageFTModelName**](ImageFTModelName.md) | Model name | 

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


