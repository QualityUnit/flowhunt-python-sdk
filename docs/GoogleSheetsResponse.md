# GoogleSheetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheets** | [**List[GoogleSheetResponse]**](GoogleSheetResponse.md) |  | 

## Example

```python
from flowhunt.models.google_sheets_response import GoogleSheetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSheetsResponse from a JSON string
google_sheets_response_instance = GoogleSheetsResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleSheetsResponse.to_json())

# convert the object into a dict
google_sheets_response_dict = google_sheets_response_instance.to_dict()
# create an instance of GoogleSheetsResponse from a dict
google_sheets_response_from_dict = GoogleSheetsResponse.from_dict(google_sheets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


