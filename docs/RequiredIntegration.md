# RequiredIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**purpose** | **str** |  | [optional] [default to '']

## Example

```python
from flowhunt.models.required_integration import RequiredIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredIntegration from a JSON string
required_integration_instance = RequiredIntegration.from_json(json)
# print the JSON string representation of the object
print(RequiredIntegration.to_json())

# convert the object into a dict
required_integration_dict = required_integration_instance.to_dict()
# create an instance of RequiredIntegration from a dict
required_integration_from_dict = RequiredIntegration.from_dict(required_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


