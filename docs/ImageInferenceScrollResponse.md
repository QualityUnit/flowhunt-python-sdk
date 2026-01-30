# ImageInferenceScrollResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_after** | **List[object]** | The search_after parameter for the next page | [optional] 
**results** | [**List[ImageInferenceResponse]**](ImageInferenceResponse.md) | The list of inference results | 

## Example

```python
from flowhunt.models.image_inference_scroll_response import ImageInferenceScrollResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInferenceScrollResponse from a JSON string
image_inference_scroll_response_instance = ImageInferenceScrollResponse.from_json(json)
# print the JSON string representation of the object
print(ImageInferenceScrollResponse.to_json())

# convert the object into a dict
image_inference_scroll_response_dict = image_inference_scroll_response_instance.to_dict()
# create an instance of ImageInferenceScrollResponse from a dict
image_inference_scroll_response_from_dict = ImageInferenceScrollResponse.from_dict(image_inference_scroll_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


