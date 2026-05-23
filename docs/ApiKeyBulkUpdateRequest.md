# ApiKeyBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ApiKeyBulkUpdateItem]**](ApiKeyBulkUpdateItem.md) |  | 

## Example

```python
from flowhunt.models.api_key_bulk_update_request import ApiKeyBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyBulkUpdateRequest from a JSON string
api_key_bulk_update_request_instance = ApiKeyBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiKeyBulkUpdateRequest.to_json())

# convert the object into a dict
api_key_bulk_update_request_dict = api_key_bulk_update_request_instance.to_dict()
# create an instance of ApiKeyBulkUpdateRequest from a dict
api_key_bulk_update_request_from_dict = ApiKeyBulkUpdateRequest.from_dict(api_key_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


