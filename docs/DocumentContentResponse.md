# DocumentContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Task ID | 
**status** | [**TaskStatus**](TaskStatus.md) | Task status | 
**result** | [**DocumentContent**](DocumentContent.md) | Document content | [optional] 
**error_message** | **str** | Error message | [optional] 

## Example

```python
from flowhunt.models.document_content_response import DocumentContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContentResponse from a JSON string
document_content_response_instance = DocumentContentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentContentResponse.to_json())

# convert the object into a dict
document_content_response_dict = document_content_response_instance.to_dict()
# create an instance of DocumentContentResponse from a dict
document_content_response_from_dict = DocumentContentResponse.from_dict(document_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


