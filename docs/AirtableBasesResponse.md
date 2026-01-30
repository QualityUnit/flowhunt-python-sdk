# AirtableBasesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bases** | [**List[AirtableBaseResponse]**](AirtableBaseResponse.md) |  | 

## Example

```python
from flowhunt.models.airtable_bases_response import AirtableBasesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AirtableBasesResponse from a JSON string
airtable_bases_response_instance = AirtableBasesResponse.from_json(json)
# print the JSON string representation of the object
print(AirtableBasesResponse.to_json())

# convert the object into a dict
airtable_bases_response_dict = airtable_bases_response_instance.to_dict()
# create an instance of AirtableBasesResponse from a dict
airtable_bases_response_from_dict = AirtableBasesResponse.from_dict(airtable_bases_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


