# AirtableFieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | [optional] 
**options** | **object** |  | [optional] 

## Example

```python
from flowhunt.models.airtable_field_response import AirtableFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AirtableFieldResponse from a JSON string
airtable_field_response_instance = AirtableFieldResponse.from_json(json)
# print the JSON string representation of the object
print(AirtableFieldResponse.to_json())

# convert the object into a dict
airtable_field_response_dict = airtable_field_response_instance.to_dict()
# create an instance of AirtableFieldResponse from a dict
airtable_field_response_from_dict = AirtableFieldResponse.from_dict(airtable_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


