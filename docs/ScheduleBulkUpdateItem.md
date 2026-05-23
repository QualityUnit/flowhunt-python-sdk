# ScheduleBulkUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | 
**frequency** | [**ScheduleFrequency**](ScheduleFrequency.md) |  | [optional] 

## Example

```python
from flowhunt.models.schedule_bulk_update_item import ScheduleBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBulkUpdateItem from a JSON string
schedule_bulk_update_item_instance = ScheduleBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(ScheduleBulkUpdateItem.to_json())

# convert the object into a dict
schedule_bulk_update_item_dict = schedule_bulk_update_item_instance.to_dict()
# create an instance of ScheduleBulkUpdateItem from a dict
schedule_bulk_update_item_from_dict = ScheduleBulkUpdateItem.from_dict(schedule_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


