# ApiKeyBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.api_key_bulk_delete_request import ApiKeyBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyBulkDeleteRequest from a JSON string
api_key_bulk_delete_request_instance = ApiKeyBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApiKeyBulkDeleteRequest.to_json())

# convert the object into a dict
api_key_bulk_delete_request_dict = api_key_bulk_delete_request_instance.to_dict()
# create an instance of ApiKeyBulkDeleteRequest from a dict
api_key_bulk_delete_request_from_dict = ApiKeyBulkDeleteRequest.from_dict(api_key_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


