# ImageInferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the image | 
**date_created** | **datetime** | The date the image was created | 
**prompt** | **str** | The prompt used for the inference | 

## Example

```python
from flowhunt.models.image_inference_response import ImageInferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInferenceResponse from a JSON string
image_inference_response_instance = ImageInferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ImageInferenceResponse.to_json())

# convert the object into a dict
image_inference_response_dict = image_inference_response_instance.to_dict()
# create an instance of ImageInferenceResponse from a dict
image_inference_response_from_dict = ImageInferenceResponse.from_dict(image_inference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


