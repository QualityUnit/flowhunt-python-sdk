# AirtableViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from flowhunt.models.airtable_view_response import AirtableViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AirtableViewResponse from a JSON string
airtable_view_response_instance = AirtableViewResponse.from_json(json)
# print the JSON string representation of the object
print(AirtableViewResponse.to_json())

# convert the object into a dict
airtable_view_response_dict = airtable_view_response_instance.to_dict()
# create an instance of AirtableViewResponse from a dict
airtable_view_response_from_dict = AirtableViewResponse.from_dict(airtable_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


