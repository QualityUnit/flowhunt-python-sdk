# AsanaProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_gid** | **str** |  | 
**project_name** | **str** |  | 
**archived** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.asana_project_response import AsanaProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsanaProjectResponse from a JSON string
asana_project_response_instance = AsanaProjectResponse.from_json(json)
# print the JSON string representation of the object
print(AsanaProjectResponse.to_json())

# convert the object into a dict
asana_project_response_dict = asana_project_response_instance.to_dict()
# create an instance of AsanaProjectResponse from a dict
asana_project_response_from_dict = AsanaProjectResponse.from_dict(asana_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


