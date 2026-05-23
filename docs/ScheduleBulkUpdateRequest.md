# ScheduleBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ScheduleBulkUpdateItem]**](ScheduleBulkUpdateItem.md) |  | 

## Example

```python
from flowhunt.models.schedule_bulk_update_request import ScheduleBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBulkUpdateRequest from a JSON string
schedule_bulk_update_request_instance = ScheduleBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleBulkUpdateRequest.to_json())

# convert the object into a dict
schedule_bulk_update_request_dict = schedule_bulk_update_request_instance.to_dict()
# create an instance of ScheduleBulkUpdateRequest from a dict
schedule_bulk_update_request_from_dict = ScheduleBulkUpdateRequest.from_dict(schedule_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


