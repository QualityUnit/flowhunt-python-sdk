# DocumentCategorySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | [optional] 
**cat_name** | **str** | Category name | [optional] 
**limit** | **int** | Limit | [optional] [default to 100]
**cat_type** | [**CategoryType**](CategoryType.md) | Category type | [optional] 

## Example

```python
from flowhunt.models.document_category_search_request import DocumentCategorySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategorySearchRequest from a JSON string
document_category_search_request_instance = DocumentCategorySearchRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCategorySearchRequest.to_json())

# convert the object into a dict
document_category_search_request_dict = document_category_search_request_instance.to_dict()
# create an instance of DocumentCategorySearchRequest from a dict
document_category_search_request_from_dict = DocumentCategorySearchRequest.from_dict(document_category_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


