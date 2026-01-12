# ImageInferenceScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_id** | **str** | The ID of the inference | 

## Example

```python
from flowhunt.models.image_inference_schedule_response import ImageInferenceScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInferenceScheduleResponse from a JSON string
image_inference_schedule_response_instance = ImageInferenceScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(ImageInferenceScheduleResponse.to_json())

# convert the object into a dict
image_inference_schedule_response_dict = image_inference_schedule_response_instance.to_dict()
# create an instance of ImageInferenceScheduleResponse from a dict
image_inference_schedule_response_from_dict = ImageInferenceScheduleResponse.from_dict(image_inference_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


