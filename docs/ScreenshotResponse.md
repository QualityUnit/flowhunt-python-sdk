# ScreenshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Task ID | 
**status** | [**TaskStatus**](TaskStatus.md) | Task status | 
**result** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**original_size_url** | [**AppUrlOutput**](AppUrlOutput.md) |  | [optional] 
**thumbnail_url** | [**AppUrlOutput**](AppUrlOutput.md) |  | [optional] 
**original_size_url_full_page** | [**AppUrlOutput**](AppUrlOutput.md) |  | [optional] 
**thumbnail_url_full_page** | [**AppUrlOutput**](AppUrlOutput.md) |  | [optional] 
**timestamp** | **int** |  | [optional] 
**domain_id** | **str** |  | [optional] 
**url_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.screenshot_response import ScreenshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotResponse from a JSON string
screenshot_response_instance = ScreenshotResponse.from_json(json)
# print the JSON string representation of the object
print(ScreenshotResponse.to_json())

# convert the object into a dict
screenshot_response_dict = screenshot_response_instance.to_dict()
# create an instance of ScreenshotResponse from a dict
screenshot_response_from_dict = ScreenshotResponse.from_dict(screenshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


