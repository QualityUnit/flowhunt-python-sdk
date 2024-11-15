# GrigCell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**col_id** | **str** | Column ID | 
**value_text** | **str** |  | [optional] 
**value_number** | **float** |  | [optional] 
**value_date** | **float** |  | [optional] 
**status** | [**GridCellStatus**](GridCellStatus.md) | Status | [optional] 
**status_updated** | **float** | Status Updated, timestamp | [optional] [default to 0]

## Example

```python
from flowhunt.models.grig_cell import GrigCell

# TODO update the JSON string below
json = "{}"
# create an instance of GrigCell from a JSON string
grig_cell_instance = GrigCell.from_json(json)
# print the JSON string representation of the object
print(GrigCell.to_json())

# convert the object into a dict
grig_cell_dict = grig_cell_instance.to_dict()
# create an instance of GrigCell from a dict
grig_cell_from_dict = GrigCell.from_dict(grig_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


