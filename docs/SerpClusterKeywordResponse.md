# SerpClusterKeywordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | Unique ID | 
**keyword_id** | **str** | Query ID | 
**keyword** | **str** | Query | 
**country** | **str** | Country | [optional] 
**language** | **str** | Language | [optional] 
**is_negative** | **bool** | Is assigned as negative or positive to group | [optional] 
**match_type** | [**GoogleAdsMatchType**](GoogleAdsMatchType.md) | Match type | 
**campaign_id** | **str** | Campaign ID | 
**group_id** | **str** | Group ID | 
**search_engine** | [**SerpSearchEngineType**](SerpSearchEngineType.md) | Search engine | 

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


