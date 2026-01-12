# GoogleSheetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet_id** | **int** | Sheet ID | 
**title** | **str** | Sheet title | 

## Example

```python
from flowhunt.models.google_sheet_response import GoogleSheetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSheetResponse from a JSON string
google_sheet_response_instance = GoogleSheetResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleSheetResponse.to_json())

# convert the object into a dict
google_sheet_response_dict = google_sheet_response_instance.to_dict()
# create an instance of GoogleSheetResponse from a dict
google_sheet_response_from_dict = GoogleSheetResponse.from_dict(google_sheet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


