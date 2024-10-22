# AppUrlInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parsed_url** | **List[object]** |  | [optional] 
**url** | **str** | The URL. | 

## Example

```python
from flowhunt-python-sdk.models.app_url_input import AppUrlInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppUrlInput from a JSON string
app_url_input_instance = AppUrlInput.from_json(json)
# print the JSON string representation of the object
print(AppUrlInput.to_json())

# convert the object into a dict
app_url_input_dict = app_url_input_instance.to_dict()
# create an instance of AppUrlInput from a dict
app_url_input_from_dict = AppUrlInput.from_dict(app_url_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


