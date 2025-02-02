# SerpClusterKeywordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id** | **str** | Query ID | 
**keyword** | **str** | Query | 
**country** | **str** |  | [optional] 
**language** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.serp_cluster_keyword_response import SerpClusterKeywordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterKeywordResponse from a JSON string
serp_cluster_keyword_response_instance = SerpClusterKeywordResponse.from_json(json)
# print the JSON string representation of the object
print(SerpClusterKeywordResponse.to_json())

# convert the object into a dict
serp_cluster_keyword_response_dict = serp_cluster_keyword_response_instance.to_dict()
# create an instance of SerpClusterKeywordResponse from a dict
serp_cluster_keyword_response_from_dict = SerpClusterKeywordResponse.from_dict(serp_cluster_keyword_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


