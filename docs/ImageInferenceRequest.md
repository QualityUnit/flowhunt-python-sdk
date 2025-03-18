# ImageInferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_model** | [**BaseFoundationModel**](BaseFoundationModel.md) | The base model to use for inference | 
**prompt** | **str** | The prompt to use for inference | 
**image_fts** | **List[str]** | The list of image FTs to use for inference | 
**number_of_outputs** | **int** | The number of outputs to generate | [optional] [default to 1]
**aspect_ratio** | [**AspecRatio**](AspecRatio.md) | The aspect ratio of the output images | [optional] 
**steps** | **int** | The number of steps to take in the inference process | [optional] [default to 28]
**guidance_scale** | **float** | The guidance scale to use in the inference process | [optional] [default to 3.5]
**styles** | **List[str]** |  | [optional] 
**effects** | **List[str]** |  | [optional] 
**use_ai_agent** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.image_inference_request import ImageInferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInferenceRequest from a JSON string
image_inference_request_instance = ImageInferenceRequest.from_json(json)
# print the JSON string representation of the object
print(ImageInferenceRequest.to_json())

# convert the object into a dict
image_inference_request_dict = image_inference_request_instance.to_dict()
# create an instance of ImageInferenceRequest from a dict
image_inference_request_from_dict = ImageInferenceRequest.from_dict(image_inference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


