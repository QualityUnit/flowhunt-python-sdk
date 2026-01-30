# AirtableTableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**primary_field_id** | **str** |  | [optional] 
**fields** | [**List[AirtableFieldResponse]**](AirtableFieldResponse.md) |  | [optional] 
**views** | [**List[AirtableViewResponse]**](AirtableViewResponse.md) |  | [optional] 

## Example

```python
from flowhunt.models.airtable_table_response import AirtableTableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AirtableTableResponse from a JSON string
airtable_table_response_instance = AirtableTableResponse.from_json(json)
# print the JSON string representation of the object
print(AirtableTableResponse.to_json())

# convert the object into a dict
airtable_table_response_dict = airtable_table_response_instance.to_dict()
# create an instance of AirtableTableResponse from a dict
airtable_table_response_from_dict = AirtableTableResponse.from_dict(airtable_table_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


