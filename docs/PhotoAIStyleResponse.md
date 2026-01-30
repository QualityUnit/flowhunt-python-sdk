# PhotoAIStyleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**cover_image** | **str** |  | 
**prompt** | **str** |  | 
**featured** | **bool** |  | [optional] [default to False]

## Example

```python
from flowhunt.models.photo_ai_style_response import PhotoAIStyleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhotoAIStyleResponse from a JSON string
photo_ai_style_response_instance = PhotoAIStyleResponse.from_json(json)
# print the JSON string representation of the object
print(PhotoAIStyleResponse.to_json())

# convert the object into a dict
photo_ai_style_response_dict = photo_ai_style_response_instance.to_dict()
# create an instance of PhotoAIStyleResponse from a dict
photo_ai_style_response_from_dict = PhotoAIStyleResponse.from_dict(photo_ai_style_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


