# ImageInferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_model** | [**BaseFoundationModel**](BaseFoundationModel.md) | The base model to use for inference | 
**prompt** | **str** | The prompt to use for inference | 
**image_fts** | **List[str]** | The list of image FTs to use for inference | 
**number_of_outputs** | **int** | The number of outputs to generate | [optional] [default to 1]
**aspect_ratio** | [**AspecRatio**](AspecRatio.md) | The aspect ratio of the output images | [optional] 
**steps** | **int** | The number of steps to take in the inference process | [optional] 
**guidance_scale** | **float** | The guidance scale to use in the inference process | [optional] 
**styles** | **List[str]** | The list of styles to use in the inference process | [optional] 
**effects** | **List[str]** | The list of effects to use in the inference process | [optional] 
**use_ai_agent** | **bool** | Whether to use the AI agent in the inference process | [optional] 
**reference_images** | **List[str]** | URLs of reference images for models that support them (GPT-IMAGE-1, NANO_BANANA, GEMINI_2_5_FLASH) | [optional] 
**reference_videos** | **List[str]** | URLs of reference videos for models that support them. | [optional] 
**duration** | **int** | Duration in seconds for video models | [optional] 
**resolution** | **str** | Resolution for video models, e.g., &#39;480p&#39;, &#39;720p&#39;, &#39;1080p&#39; | [optional] 
**generate_audio** | **bool** | Whether to generate audio for video models that support it | [optional] 
**start_image** | **List[str]** | URLs of start images for image-to-video models | [optional] 
**last_frame** | **List[str]** | URLs of last frames for image-to-video models that support it | [optional] 

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


