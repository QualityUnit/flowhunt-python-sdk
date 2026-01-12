# PhotoAITemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cover_image** | **str** |  | 
**prompt** | **str** |  | 
**model** | **str** |  | 
**styles** | **List[str]** |  | 
**effects** | **List[str]** |  | 

## Example

```python
from flowhunt.models.photo_ai_template_response import PhotoAITemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhotoAITemplateResponse from a JSON string
photo_ai_template_response_instance = PhotoAITemplateResponse.from_json(json)
# print the JSON string representation of the object
print(PhotoAITemplateResponse.to_json())

# convert the object into a dict
photo_ai_template_response_dict = photo_ai_template_response_instance.to_dict()
# create an instance of PhotoAITemplateResponse from a dict
photo_ai_template_response_from_dict = PhotoAITemplateResponse.from_dict(photo_ai_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


