# AirtableBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**permission_level** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.airtable_base_response import AirtableBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AirtableBaseResponse from a JSON string
airtable_base_response_instance = AirtableBaseResponse.from_json(json)
# print the JSON string representation of the object
print(AirtableBaseResponse.to_json())

# convert the object into a dict
airtable_base_response_dict = airtable_base_response_instance.to_dict()
# create an instance of AirtableBaseResponse from a dict
airtable_base_response_from_dict = AirtableBaseResponse.from_dict(airtable_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


