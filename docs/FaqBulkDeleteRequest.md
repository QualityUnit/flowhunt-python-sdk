# FaqBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.faq_bulk_delete_request import FaqBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FaqBulkDeleteRequest from a JSON string
faq_bulk_delete_request_instance = FaqBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(FaqBulkDeleteRequest.to_json())

# convert the object into a dict
faq_bulk_delete_request_dict = faq_bulk_delete_request_instance.to_dict()
# create an instance of FaqBulkDeleteRequest from a dict
faq_bulk_delete_request_from_dict = FaqBulkDeleteRequest.from_dict(faq_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


