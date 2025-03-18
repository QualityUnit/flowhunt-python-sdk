# ImageInferenceResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ImageInferenceResponse**](ImageInferenceResponse.md) |  | [optional] 
**status** | **str** | Whether the inference is completed | 
**error_message** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.image_inference_result_response import ImageInferenceResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInferenceResultResponse from a JSON string
image_inference_result_response_instance = ImageInferenceResultResponse.from_json(json)
# print the JSON string representation of the object
print(ImageInferenceResultResponse.to_json())

# convert the object into a dict
image_inference_result_response_dict = image_inference_result_response_instance.to_dict()
# create an instance of ImageInferenceResultResponse from a dict
image_inference_result_response_from_dict = ImageInferenceResultResponse.from_dict(image_inference_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


