# AirtableTablesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[AirtableTableResponse]**](AirtableTableResponse.md) |  | 

## Example

```python
from flowhunt.models.airtable_tables_response import AirtableTablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AirtableTablesResponse from a JSON string
airtable_tables_response_instance = AirtableTablesResponse.from_json(json)
# print the JSON string representation of the object
print(AirtableTablesResponse.to_json())

# convert the object into a dict
airtable_tables_response_dict = airtable_tables_response_instance.to_dict()
# create an instance of AirtableTablesResponse from a dict
airtable_tables_response_from_dict = AirtableTablesResponse.from_dict(airtable_tables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


