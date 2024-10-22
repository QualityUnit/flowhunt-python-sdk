# DocumentCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**cat_id** | **str** | Category ID | 
**cat_name** | **str** | Category name | 
**cat_color** | **str** | Category color | 

## Example

```python
from flowhunt-python-sdk.models.document_category_response import DocumentCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryResponse from a JSON string
document_category_response_instance = DocumentCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryResponse.to_json())

# convert the object into a dict
document_category_response_dict = document_category_response_instance.to_dict()
# create an instance of DocumentCategoryResponse from a dict
document_category_response_from_dict = DocumentCategoryResponse.from_dict(document_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


