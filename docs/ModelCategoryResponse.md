# ModelCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**models** | [**List[ModelResponse]**](ModelResponse.md) |  | 

## Example

```python
from flowhunt.models.model_category_response import ModelCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCategoryResponse from a JSON string
model_category_response_instance = ModelCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCategoryResponse.to_json())

# convert the object into a dict
model_category_response_dict = model_category_response_instance.to_dict()
# create an instance of ModelCategoryResponse from a dict
model_category_response_from_dict = ModelCategoryResponse.from_dict(model_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


