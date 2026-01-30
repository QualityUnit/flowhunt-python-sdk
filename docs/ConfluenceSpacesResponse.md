# ConfluenceSpacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spaces** | [**List[ConfluenceSpaceResponse]**](ConfluenceSpaceResponse.md) |  | 

## Example

```python
from flowhunt.models.confluence_spaces_response import ConfluenceSpacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfluenceSpacesResponse from a JSON string
confluence_spaces_response_instance = ConfluenceSpacesResponse.from_json(json)
# print the JSON string representation of the object
print(ConfluenceSpacesResponse.to_json())

# convert the object into a dict
confluence_spaces_response_dict = confluence_spaces_response_instance.to_dict()
# create an instance of ConfluenceSpacesResponse from a dict
confluence_spaces_response_from_dict = ConfluenceSpacesResponse.from_dict(confluence_spaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


