# ScreenshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**url** | **str** | URL to take screenshot | 
**validity** | **datetime** |  | [optional] 
**use_proxy** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.screenshot_request import ScreenshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotRequest from a JSON string
screenshot_request_instance = ScreenshotRequest.from_json(json)
# print the JSON string representation of the object
print(ScreenshotRequest.to_json())

# convert the object into a dict
screenshot_request_dict = screenshot_request_instance.to_dict()
# create an instance of ScreenshotRequest from a dict
screenshot_request_from_dict = ScreenshotRequest.from_dict(screenshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


