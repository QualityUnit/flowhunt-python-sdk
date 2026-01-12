# ImageFTSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Fine tuning name | [optional] 

## Example

```python
from flowhunt.models.image_ft_search_request import ImageFTSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFTSearchRequest from a JSON string
image_ft_search_request_instance = ImageFTSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ImageFTSearchRequest.to_json())

# convert the object into a dict
image_ft_search_request_dict = image_ft_search_request_instance.to_dict()
# create an instance of ImageFTSearchRequest from a dict
image_ft_search_request_from_dict = ImageFTSearchRequest.from_dict(image_ft_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


