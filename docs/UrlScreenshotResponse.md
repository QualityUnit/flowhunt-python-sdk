# UrlScreenshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_image** | **str** |  | 
**thumbnail_image** | **str** |  | 

## Example

```python
from flowhunt-python-sdk.models.url_screenshot_response import UrlScreenshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UrlScreenshotResponse from a JSON string
url_screenshot_response_instance = UrlScreenshotResponse.from_json(json)
# print the JSON string representation of the object
print(UrlScreenshotResponse.to_json())

# convert the object into a dict
url_screenshot_response_dict = url_screenshot_response_instance.to_dict()
# create an instance of UrlScreenshotResponse from a dict
url_screenshot_response_from_dict = UrlScreenshotResponse.from_dict(url_screenshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


