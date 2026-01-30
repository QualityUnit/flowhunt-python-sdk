# ImageConvertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** | The post back URL where to send the response in body | [optional] 
**image_url** | **str** | Image URL to convert | 
**format** | **str** | Image format to convert to | 
**quality** | **int** | Image quality (10-100) | [optional] [default to 75]

## Example

```python
from flowhunt.models.image_convert_request import ImageConvertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageConvertRequest from a JSON string
image_convert_request_instance = ImageConvertRequest.from_json(json)
# print the JSON string representation of the object
print(ImageConvertRequest.to_json())

# convert the object into a dict
image_convert_request_dict = image_convert_request_instance.to_dict()
# create an instance of ImageConvertRequest from a dict
image_convert_request_from_dict = ImageConvertRequest.from_dict(image_convert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


