# SerpClusterKeywordIntersectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id** | **str** | Keyword ID, if not provided it will be generated | [optional] 
**keyword** | **str** | Keyword to search | 
**language** | **str** | Language to search | [optional] [default to 'en']
**country** | **str** | Country to search from | [optional] [default to 'us']
**search_engine** | [**SerpSearchEngineType**](SerpSearchEngineType.md) | Search engine to analyze keyword clusters | [optional] 
**customer_id** | **str** | Customer ID of cluster | 
**campaign_id** | **str** | Campaign ID of cluster | [optional] 
**group_id** | **str** | Group ID of cluster | [optional] 
**min_cluster_strength** | **int** | Minimum cluster strength | [optional] [default to 1]

## Example

```python
from flowhunt.models.serp_cluster_keyword_intersections_request import SerpClusterKeywordIntersectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterKeywordIntersectionsRequest from a JSON string
serp_cluster_keyword_intersections_request_instance = SerpClusterKeywordIntersectionsRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterKeywordIntersectionsRequest.to_json())

# convert the object into a dict
serp_cluster_keyword_intersections_request_dict = serp_cluster_keyword_intersections_request_instance.to_dict()
# create an instance of SerpClusterKeywordIntersectionsRequest from a dict
serp_cluster_keyword_intersections_request_from_dict = SerpClusterKeywordIntersectionsRequest.from_dict(serp_cluster_keyword_intersections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


