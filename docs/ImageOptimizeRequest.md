# ImageOptimizeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** | The post back URL where to send the response in body | [optional] 
**image_url** | **str** | Image URL to optimize | 
**quality** | **int** | Image quality (10-100) | [optional] [default to 100]

## Example

```python
from flowhunt.models.image_optimize_request import ImageOptimizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOptimizeRequest from a JSON string
image_optimize_request_instance = ImageOptimizeRequest.from_json(json)
# print the JSON string representation of the object
print(ImageOptimizeRequest.to_json())

# convert the object into a dict
image_optimize_request_dict = image_optimize_request_instance.to_dict()
# create an instance of ImageOptimizeRequest from a dict
image_optimize_request_from_dict = ImageOptimizeRequest.from_dict(image_optimize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


