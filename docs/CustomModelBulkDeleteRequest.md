# CustomModelBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.custom_model_bulk_delete_request import CustomModelBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModelBulkDeleteRequest from a JSON string
custom_model_bulk_delete_request_instance = CustomModelBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(CustomModelBulkDeleteRequest.to_json())

# convert the object into a dict
custom_model_bulk_delete_request_dict = custom_model_bulk_delete_request_instance.to_dict()
# create an instance of CustomModelBulkDeleteRequest from a dict
custom_model_bulk_delete_request_from_dict = CustomModelBulkDeleteRequest.from_dict(custom_model_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


