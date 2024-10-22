# TagSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.tag_search_request import TagSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagSearchRequest from a JSON string
tag_search_request_instance = TagSearchRequest.from_json(json)
# print the JSON string representation of the object
print(TagSearchRequest.to_json())

# convert the object into a dict
tag_search_request_dict = tag_search_request_instance.to_dict()
# create an instance of TagSearchRequest from a dict
tag_search_request_from_dict = TagSearchRequest.from_dict(tag_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


