# DocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** | Document ID | 
**cat_id** | **str** | Category ID | 
**workspace_id** | **str** | Workspace ID | 
**doc_name** | **str** | Document name | 
**url** | **str** |  | [optional] 
**doc_type** | **str** | Document type | 
**user_status** | **str** | User status | 
**status** | **str** | Document status | 
**updated_at** | **datetime** | Document updated at | 

## Example

```python
from flowhunt.models.document_response import DocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponse from a JSON string
document_response_instance = DocumentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentResponse.to_json())

# convert the object into a dict
document_response_dict = document_response_instance.to_dict()
# create an instance of DocumentResponse from a dict
document_response_from_dict = DocumentResponse.from_dict(document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


