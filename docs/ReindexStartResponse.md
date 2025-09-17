# ReindexStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**task_id** | **str** |  | 

## Example

```python
from flowhunt.models.reindex_start_response import ReindexStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReindexStartResponse from a JSON string
reindex_start_response_instance = ReindexStartResponse.from_json(json)
# print the JSON string representation of the object
print(ReindexStartResponse.to_json())

# convert the object into a dict
reindex_start_response_dict = reindex_start_response_instance.to_dict()
# create an instance of ReindexStartResponse from a dict
reindex_start_response_from_dict = ReindexStartResponse.from_dict(reindex_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


