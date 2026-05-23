# FaqBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FaqBulkUpdateItem]**](FaqBulkUpdateItem.md) |  | 

## Example

```python
from flowhunt.models.faq_bulk_update_request import FaqBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FaqBulkUpdateRequest from a JSON string
faq_bulk_update_request_instance = FaqBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FaqBulkUpdateRequest.to_json())

# convert the object into a dict
faq_bulk_update_request_dict = faq_bulk_update_request_instance.to_dict()
# create an instance of FaqBulkUpdateRequest from a dict
faq_bulk_update_request_from_dict = FaqBulkUpdateRequest.from_dict(faq_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


