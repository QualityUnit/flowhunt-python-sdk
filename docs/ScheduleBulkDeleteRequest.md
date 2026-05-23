# ScheduleBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.schedule_bulk_delete_request import ScheduleBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBulkDeleteRequest from a JSON string
schedule_bulk_delete_request_instance = ScheduleBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleBulkDeleteRequest.to_json())

# convert the object into a dict
schedule_bulk_delete_request_dict = schedule_bulk_delete_request_instance.to_dict()
# create an instance of ScheduleBulkDeleteRequest from a dict
schedule_bulk_delete_request_from_dict = ScheduleBulkDeleteRequest.from_dict(schedule_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


